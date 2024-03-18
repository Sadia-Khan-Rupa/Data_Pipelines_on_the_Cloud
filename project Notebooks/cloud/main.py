import functions_framework
import pandas as pd
import sqlalchemy
import requests
from datetime import date, timedelta, datetime
from pytz import timezone



@functions_framework.http
def insert(request):
  
    connection_string = connection()
    cities_df = get_cities_data(connection_string)
    weather_df = get_weather_data(cities_df)
    airport_df = pd.read_sql('airport', con= connection_string)
    flight_df = get_flight_data(airport_df)
    send_flight_data(flight_df, connection_string)
    send_weather_data(weather_df, connection_string)
    return 'Data successfully added'
    
  

def connection():
  connection_name = "tidy-reporter-417111:europe-west1:wbs-mysql-db"
  db_user = "root"
  db_password = "LC<yhhu,8'4'7B1q"
  schema_name = 'sql_challenge1'

  driver_name = 'mysql+pymysql'
  query_string = {"unix_socket": f"/cloudsql/{connection_name}"}

  db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
          drivername = driver_name,
          username = db_user,
          password = db_password,
          database = schema_name,
          query = query_string,
      )
  )
  return db





def get_cities_data(connection_string):
    sql_table = pd.read_sql('cities', con=connection_string)
    return sql_table

#now we want to find all the info we are interested into
def  get_weather_data(cities_df):

    API_key = '604e1cbac36da59a07db3121dfea7d95'
    berlin_timezone = timezone('Europe/Berlin')
    weather_items = []
    
    for city_name in cities_df['city_name']:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=metric"
        json_response = requests.get(url).json()

        #taking city_id from city dataframe
        city_id = cities_df.loc[cities_df["city_name"] == city_name, "city_id"].values[0]

        retrieval_time =datetime.now(berlin_timezone).strftime("%Y-%m-%d %H:%M:%S")

        for item in json_response["list"]:
                weather_item = {
                    "city_id": city_id,
                    "forecast_time": item.get("dt_txt", None),
                    "temperature": item["main"].get("temp", None),
                    "forecast": item["weather"][0].get("main", None),
                    "rain_in_last_3h": item.get("rain", {}).get("3h", 0),
                    "wind_speed": item["wind"].get("speed", None),
                    "data_retrieved_on": retrieval_time
                }
                weather_items.append(weather_item)
    weather_df = pd.DataFrame(weather_items)
    weather_df["forecast_time"] = pd.to_datetime(weather_df["forecast_time"])
    weather_df["data_retrieved_on"] = pd.to_datetime(weather_df["data_retrieved_on"])
    print(weather_df.info())
    return weather_df

def send_weather_data(weather_df, connection_string):
  weather_df.to_sql('weather',
                    if_exists='append',
                    con=connection_string,
                    index=False)

def get_flight_data(airport_df):
    present_day = date.today()
    tomorrow= present_day + timedelta(1)

    
    flight_list = []
    
    for icao_code in airport_df['icao']:
        times = [['00:00', '11:59'], ['12:00', '23:59']]

        for time in times:

            url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{icao_code}/{tomorrow}T{time[0]}/{tomorrow}T{time[1]}"

            querystring = {"withLeg":"true","withCancelled":"true","withCodeshared":"true","withCargo":"true","withPrivate":"true","withLocation":"false"}

            headers = {
                "X-RapidAPI-Key": "14a44098c8mshe4536a007985112p1e3b4bjsn8fd805eb6bd4",
                "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
            }

            response_arrivals1 = requests.get(url, headers=headers, params=querystring)
            arrivals = response_arrivals1.json()
            icao_list = airport_df["icao"].tolist()

            
            for item in arrivals['departures']:
                flight_item = {
                #extracting arrival icao
                'arrival_icao': icao_list[0],
                #extracting departure icao
                'departure_icao': item['airline'].get('icao', None),
                #extracting arrival city
                'arrival_city': item['arrival']['airport']['name'],
                #Extracting flight number
                'flight_number': item.get('number', None),
                #extracting arrival time
                'arrival_time': item['departure']['scheduledTime']['local']
                }
                
                flight_list.append(flight_item)
                flight_df = pd.DataFrame(flight_list)

            flight_df['arrival_time'] =  flight_df['arrival_time'].str[:-6] #getting rid of +01:00 from arrival_time
            flight_df['arrival_time'] = pd.to_datetime(flight_df['arrival_time'])
            
    print (flight_df.info())
    return flight_df

def send_flight_data(flight_df, connection_string):
  flight_df.to_sql('flight',
                    if_exists='append',
                    con=connection_string,
                    index=False)
  

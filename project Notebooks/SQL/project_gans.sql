DROP DATABASE IF EXISTS sql_challenge1;

create database sql_challenge1;

use sql_challenge1;



-- Create 'cities' table

create table cities(
     city_id int auto_increment,
     city_name varchar(255) not null,
     primary key(city_id)
);
INSERT INTO cities (city_name)
VALUES
("Berlin"),
("Munich");
select * from cities;

drop table populations;
/***************************
Creating the second table
***************************/
-- https://www.w3schools.com/sql/sql_datatypes.asp (for sql data type)
create table populations(
     city_id int, 
     population int,
     year_data  year,
     FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

select *from populations;
drop table weather;
create table weather(
	   id int auto_increment, 
	   city_id int,
       forecast_time datetime,
       temperature float,
       forecast varchar(255),
       rain_in_last_3h float,
       wind_speed float,
       data_retrieved_on datetime,
       primary key(id),
       foreign key (city_id) references cities(city_id)
       );
       
INSERT INTO weather(city_id, forecast_time, temperature, forecast, rain_in_last_3h, wind_speed, data_retrieved_on)
VALUES(1, '2024-03-13 12:00:00', 13.2, 'clear', 0.0, 3.5, '2024-03-13 12:00:00');


select *from weather;

drop table airport;
create table airport(
       icao varchar(255),
       name varchar(255),
       primary key(icao)

);

INSERT INTO airport (icao, name)
VALUES
("EDDB", "Berlin Brandenburg");

select * from airport;

drop table cities_airports;
create table cities_airports(
	   city_id int, 
       airport_icao varchar(255),
       foreign key (city_id) references cities(city_id),
       foreign key (airport_icao) references airport(icao)
       );
select * from cities_airports;

drop table flight;

create table flight(
       flight_id int auto_increment, 
       arrival_icao varchar(255),
       departure_icao varchar(255),
       arrival_city varchar(255),
       flight_number varchar(255),
       arrival_time datetime,
       primary key(flight_id),
       foreign key(arrival_icao) references airport(icao)
       );
       
INSERT INTO flight(arrival_icao, departure_icao, arrival_city, flight_number, arrival_time)
VALUES
("EDDB", "EWG", "Stuttgart", "EW 3001", "2024-03-12 00:21");


select *from flight;
       
     
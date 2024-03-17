DROP DATABASE IF EXISTS sql_challenge ;

create database sql_challenge;

use sql_challenge;



-- Create 'cities' table

create table cities(
     city_id int auto_increment,
     city_name varchar(255) not null,
     primary key(city_id)
);

select * from cities;


/***************************
Creating the second table
***************************/
-- https://www.w3schools.com/sql/sql_datatypes.asp (for sql data type)
create table populations(
     city_id int auto_increment, 
     population int,
     year_data  year,
     FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

select *from populations;

create table weather(
	   city varchar(255) not null,
       country varchar(255),
       forecast_time varchar(255),
       weather_outlook varchar(255),
       weather_details varchar(255),
       temperature float,
       feels_like_temperature float,
       humidity int,
       wind_speed float,
       rain float,
       snow float
       
       );
select *from weather;

create table airport(
       icao varchar(255) not null,
       name varchar(255)

);
select * from airport;

create table flight(
       flight_id int auto_increment, 
       arrival_icao varchar(255),
       departure_icao varchar(255),
       arrival_city varchar(255),
       flight_number varchar(255),
       arrival_time varchar(255)
       primary key(flight_id)
       );
select *from flight;
       
     
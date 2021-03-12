# sqlalchemy-challenge

This project's goal is to leverage Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database. 

The first part of the project is precipitation analysis and station analysis. The goal of precipitation analysis is to find the most recent date in the data set and use that date to find the lasts 12 months of precipitation data by querying the 12 preceding months of data. The data is then converted into Pandas DataFrame to print the summary statistics for the precipitation data and create a plot out of it. 

Moving on to station analysis, it starts by designing a query to calculate the total number of stations and the most active station in the dataset to find out which station id has the highest number of observations and to calculate the min, average, and max. Lastly, the goal of the station analysis is to design a query to retrieve the last 12 months of temperature observation data, and make a filter and plot out of it. 

The second part of the project is called the climate app, where the goal is to design a Flask API based on the queries that are developed in part 1. There are 6 routes designed in total, which consist of home, precipitation, stations, TOBS, and lastly the start and start/end, where it accept a date or a range of date to return a list of the min, average, and max temperature of that particular date. 

The bonus part of the project is to apply SQLAlchemy and Python to a real-life example, where the goal of the first part is to do an analysis of the temperature and precipitation of Hawaii in the month of June and December to see if there is any difference between the temperature. 

The second part of the bonus is to calculate the daily rainfall average per weather station to find out which station, along with its name, latitude, longitude, and elevation has the highest average rainfall. The function called calc_temps is used to calculate the min, avg, and max temperatures for the trip using the matching dates from a previous year to find out if it is going to rain during the trip. 

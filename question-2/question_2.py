# Question 2
# Create a program that analyses temperature data collected from multiple weather
# stations in Australia. The data is stored in multiple CSV files under a "temperatures"
# folder, with each file representing data from one year. Process ALL .csv files in the
# temperatures folder. Ignore missing temperature values (NaN) in calculations.
# Main Functions to Implement:
# Seasonal Average: Calculate the average temperature for each season across ALL
# stations and ALL years. Save the results to "average_temp.txt".
# •
# •
# Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (Jun-
# Aug), Spring (Sep-Nov)
# Output format example: "Summer: 28.5°C"
# Temperature Range: Find the station(s) with the largest temperature range (difference
# between the highest and lowest temperature ever recorded at that station). Save the
# results to "largest_temp_range_station.txt".
# •
# •
# Output format example: "Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)"
# If multiple stations tie, list all of them
# Temperature Stability: Find which station(s) have the most stable temperatures
# (smallest standard deviation) and which have the most variable temperatures (largest
# standard deviation). Save the results to "temperature_stability_stations.txt".
# •
# •
# Output format example:
# o "Most Stable: Station XYZ: StdDev 2.3°C"
# o "Most Variable: Station DEF: StdDev 12.8°C"
# If multiple stations tie, list all of them

import pandas as pandas
import glob
import os
import numpy as np

# Defining folder for temperatures
TEMPERATURE_DATA_FOLDER = "temperatures"

# Sorting months on the basis of seasons
AUSTRALIAN_SEASON = {"Summer": ["December", "January", "February"],
                     "Autumn": ["March", "April", "May"],
                     "Winter": ["June", "July", "August"],
                     "Spring": ["September", "October", "November"]}

#Reading all the csv files from the temperatures folder
all_csv_files = glob.glob(os.path.join(TEMPERATURE_DATA_FOLDER, "*.csv"))

temperature_dataframes = []

#Appending csv to the created panda dataframe
for temperature_csv_file in all_csv_files:
    dataframe = pandas.read_csv(temperature_csv_file)
    temperature_dataframes.append(dataframe)

#Concatinating each files to a single data frame
temperature_data_single_frame = pandas.concat(temperature_dataframes, ignore_index=True)

seasonal_average = {}

for season, months in AUSTRALIAN_SEASON.items():
    # Flatten all temperature values for these months across all stations and years
    temperatures = temperature_data_single_frame[months].to_numpy().flatten()
    # Convert to numeric and ignore NaN
    temperatures = pandas.to_numeric(temperatures, errors='coerce')
    seasonal_average[season] = np.nanmean(temperatures)

# We write seasonal average to the file which names 'average_temperature.txt' where 'w' gives the 'write' permission
with open("average_temperature.txt", "w") as f:
    for season, avg in seasonal_average.items():
        f.write(f"{season}: {avg:.1f}°C\n")

# Finding the largest temperature range
station_ranges = []

for idx, row in temperature_data_single_frame.iterrows():
    # Combinng all the monthly stations for a particular station
    temperatures = row[list(
        AUSTRALIAN_SEASON["Summer"] + AUSTRALIAN_SEASON["Autumn"] + AUSTRALIAN_SEASON["Winter"] + AUSTRALIAN_SEASON[
            "Spring"])]
    temperatures = pandas.to_numeric(temperatures, errors='coerce')
    max_temp = np.nanmax(temperatures)
    min_temp = np.nanmin(temperatures)
    temp_range = max_temp - min_temp
    station_ranges.append((row['STATION_NAME'], temp_range, max_temp, min_temp))

# Finding the stations with the largest temperature
max_range = max(station_ranges, key=lambda x: x[1])[1]
largest_range_stations = [s for s in station_ranges if s[1] == max_range]

# Writing the result in the file with the name 'largest_temperature_range_station.txt' where "w" is the 'write' permission
with open("largest_temperature_range_station.txt", "w") as f:
    for name, r, mx, mn in largest_range_stations:
        f.write(f"Station {name}: Range {r:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

# Finding the Temperature Stability by measuring the standard deviation
stations_standard_deviation = []

for idx, row in temperature_data_single_frame.iterrows():
    temperatures = row[list(AUSTRALIAN_SEASON["Summer"] + AUSTRALIAN_SEASON["Autumn"] + AUSTRALIAN_SEASON["Winter"] + AUSTRALIAN_SEASON["Spring"])]
    temperatures = pandas.to_numeric(temperatures, errors='coerce')
    std = np.nanstd(temperatures)
    stations_standard_deviation.append((row['STATION_NAME'], std))

min_std = min(stations_standard_deviation, key=lambda x: x[1])[1]
max_std = max(stations_standard_deviation, key=lambda x: x[1])[1]

most_stable = [s for s in stations_standard_deviation if s[1] == min_std]
most_variable = [s for s in stations_standard_deviation if s[1] == max_std]

# Writing the results in the file named 'temperature_stability_stations.txt' where 'w' is the 'write' permission
with open("temperature_stability_stations.txt", "w") as f:
    for name, std in most_stable:
        f.write(f"Most Stable: Station {name}: StdDev {std:.1f}°C\n")
    for name, std in most_variable:
        f.write(f"Most Variable: Station {name}: StdDev {std:.1f}°C\n")

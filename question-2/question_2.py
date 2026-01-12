import pandas as pandas
import glob
import os
import numpy as np

TEMPERATURE_DATA_FOLDER = "temperatures"

AUSTRALIAN_SEASON = {"Summer": ["December", "January", "February"],
                     "Autumn": ["March", "April", "May"],
                     "Winter": ["June", "July", "August"],
                     "Spring": ["September", "October", "November"]}

all_csv_files = glob.glob(os.path.join(TEMPERATURE_DATA_FOLDER, "*.csv"))

temperature_dataframes = []

for temperature_csv_file in all_csv_files:
    dataframe = pandas.read_csv(temperature_csv_file)
    temperature_dataframes.append(dataframe)

temperature_data_single_frame = pandas.concat(temperature_dataframes, ignore_index=True)

seasonal_average = {}

for season, months in AUSTRALIAN_SEASON.items():
    # Flatten all temperature values for these months across all stations and years
    temps = temperature_data_single_frame[months].to_numpy().flatten()
    # Convert to numeric and ignore NaN
    temps = pandas.to_numeric(temps, errors='coerce')
    seasonal_average[season] = np.nanmean(temps)

# Write seasonal averages to file
with open("average_temp.txt", "w") as f:
    for season, avg in seasonal_average.items():
        f.write(f"{season}: {avg:.1f}°C\n")

# -------------------- 2) LARGEST TEMPERATURE RANGE --------------------
station_ranges = []

for idx, row in temperature_data_single_frame.iterrows():
    # Combine all monthly temperatures for this station
    temps = row[list(
        AUSTRALIAN_SEASON["Summer"] + AUSTRALIAN_SEASON["Autumn"] + AUSTRALIAN_SEASON["Winter"] + AUSTRALIAN_SEASON[
            "Spring"])]
    temps = pandas.to_numeric(temps, errors='coerce')
    max_temp = np.nanmax(temps)
    min_temp = np.nanmin(temps)
    temp_range = max_temp - min_temp
    station_ranges.append((row['STATION NAME'], temp_range, max_temp, min_temp))

# Find stations with the largest range
max_range = max(station_ranges, key=lambda x: x[1])[1]
largest_range_stations = [s for s in station_ranges if s[1] == max_range]

# Write to file
with open("largest_temp_range_station.txt", "w") as f:
    for name, r, mx, mn in largest_range_stations:
        f.write(f"Station {name}: Range {r:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

# -------------------- 3) TEMPERATURE STABILITY --------------------
station_stddev = []

for idx, row in temperature_data_single_frame.iterrows():
    temps = row[list(AUSTRALIAN_SEASON["Summer"] + AUSTRALIAN_SEASON["Autumn"] + AUSTRALIAN_SEASON["Winter"] + AUSTRALIAN_SEASON["Spring"])]
    temps = pandas.to_numeric(temps, errors='coerce')
    std = np.nanstd(temps)
    station_stddev.append((row['STATION NAME'], std))

min_std = min(station_stddev, key=lambda x: x[1])[1]
max_std = max(station_stddev, key=lambda x: x[1])[1]

most_stable = [s for s in station_stddev if s[1] == min_std]
most_variable = [s for s in station_stddev if s[1] == max_std]

# Write to file
with open("temperature_stability_stations.txt", "w") as f:
    for name, std in most_stable:
        f.write(f"Most Stable: Station {name}: StdDev {std:.1f}°C\n")
    for name, std in most_variable:
        f.write(f"Most Variable: Station {name}: StdDev {std:.1f}°C\n")

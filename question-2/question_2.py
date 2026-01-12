import pandas as pandas
import glob
import os

TEMPERATURE_DATA_FOLDER = "temperatures"

all_csv_files = glob.glob(os.path.join(TEMPERATURE_DATA_FOLDER, "*.csv"))

temperature_dataframes = []

for temperature_csv_file in all_csv_files:
    dataframe = pandas.read_csv(temperature_csv_file)
    temperature_dataframes.append(dataframe)

temperature_data_single_frame = pandas.concat(temperature_dataframes, ignore_index=True)

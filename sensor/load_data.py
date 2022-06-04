import os
import glob
import csv

def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(),"datasets","*.csv"))
    for file in sensor_files:
        with open(file) as data_file:
            data_reader = csv.DictReader(data_file,delimiter=',')
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data
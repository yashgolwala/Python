import pandas
import os
import time

while True:
    if os.path.exists("original.csv"):

        #for reading the data from the file
        data = pandas.read_csv("original.csv")
        #printing the data object which is of type dataFrame
        print(data)
        print(data.mean())
        #for getting data mean value for the st1 column
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(5)
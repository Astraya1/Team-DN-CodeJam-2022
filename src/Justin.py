import csv
import json

class load:
    def __init__(self, load_id, origin_city, origin_state, origin_latitude, origin_longitude, destination_city, destination_state, destination_latitude, destination_longitude, amount, pickup_date_time) -> None:
        self.load_id = load_id
        self.origin_city = origin_city
        self.origin_state = origin_state
        self.origin_latitude = origin_latitude
        self.origin_longitude = origin_longitude
        self.destination_city = destination_city
        self.destination_state = destination_state
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.amount = amount
        self.pickup_date_time = pickup_date_time

def readcsv(csvfile): #Variable 'csvfile' should be the file name of the data sheet ie. dataset.csv
    with open(csvfile, 'r') as csv_file:
        csvfile = csv.reader(csv_file)

        paths = []
        for line in csvfile: #Creates a list which contains all truck route requests, with information stored as attributes given by the request class.
            paths.append(load(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))
        
        return paths

def readinput(): 
    with open("input.json", 'w') as json_file:
        input = json.load(json_file)
    return input

#Assumes that the input is a list as such: [{"input_trip_id":101,"load_ids":[123123,12312]},{"input_trip_id":102,"load_ids":[123,12311,598234]}]
def createoutput(results):
    with open('output.json','w') as json_file:
        json.dump(results, json_file)
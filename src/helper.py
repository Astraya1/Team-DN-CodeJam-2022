from cmath import inf
from datetime import *
import math
import json
import csv

class Load:
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
        self.pickup_date_time = datetime.strptime(pickup_date_time, "%Y-%m-%d %H:%M:%S") #Converts the date and time into a datetime object so that we can calculate the time delta between pickup and delivery date.
        self.pickupHour = 0

class Edge:
    def __init__(self, source, destination, gascost, loads, time):
        self.source = source
        self.destination = destination
        self.gascost = gascost
        self.loads = loads
        self.time = time

    def get(self, source, destination):
        if self.source == source and self.destination == destination:
            return self
        else:
            return None

    def addLoad(self, load):
        self.loads.append(load)

    def create_Edge_From_Trucker(self, trucker, load, destination):
        if(self.get(0,destination) == None):
            milesDist = findDistance(trucker.start_latitude,trucker.start_longitude,load.origin_latitude,load.origin_longitude)
            time = calculateTimeOfTrip(milesDist)
            gasCost = money(milesDist, load.amount)
            load.pickupHour = deadline
            self.loads = [load]
            return Edge(0,destination,gasCost,self.loads,time)

        else:
            deadline = pickUpHour(load,trucker)
            load.pickupHour = deadline
            edge = self.get(0,destination)
            edge.addLoad(load)
            return edge

    def create_Edge(self, trucker, load, source, destination):
        if(self.get(source,destination) == None):
            milesDist = findDistance(load.origin_latitude,load.origin_longitude, load.destination_latitude,load.destination_longitude)
            time = calculateTimeOfTrip(milesDist)
            gasCost = money(milesDist, load.amount)
            load.pickupHour = deadline
            self.loads = [load]
            return Edge(0,destination,gasCost,self.loads,time)

        else:
            deadline = pickUpHour(load,trucker)
            load.pickupHour = deadline
            edge = self.get(source,destination)
            edge.addLoad(load)
            return edge

class Trucker: #Read from json input
    def __init__(self, trip_id, start_latitude, start_longitude, start_time, max_destination_time):
        self.trip_id = trip_id
        self.start_latitude = start_latitude
        self.start_longitude = start_longitude
        self.start_time = start_time
        self.max_destination_time = max_destination_time
        self.maxRoadTime = ((start_time - max_destination_time).total_seconds())/60/60

def findDistance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = lat1 * math.pi/180
    phi2 = lat2 * math.pi/180
    deltaPhi = (lat2 - lat1) * math.pi/180
    deltaLambda = (lon2 - lon1) * math.pi/180

    a = math.sin(deltaPhi/2) * math.sin(deltaPhi/2) + math.cos(phi1) + \
        math.cos(phi2) * math.sin(deltaLambda/2) * math.sin(deltaLambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    metresDist = R * c
    milesDist = metresDist/1609.344
    return milesDist

def calculateTimeOfTrip(milesDist):
    driveTime = milesDist/55
    return driveTime


def money(milesDist, profit):
    price = -(milesDist * 0.4) + profit
    return price


def pickUpHour(load, trucker):
    pickUpDate = load.pickup_date_time
    truckerStartTime = trucker.start_time
    difference = pickUpDate - truckerStartTime
    total_seconds = difference.total_seconds()
    hours = total_seconds/60/60
    return hours



def readcsv(csvfile): #Variable 'csvfile' should be the file name of the data sheet ie. dataset.csv
    with open(csvfile, 'r') as csv_file:
        csvfile = csv.reader(csv_file)

        paths = []
        for i, line in enumerate(csvfile): #Creates a list which contains all truck route requests, with information stored as attributes given by the request class.
            if i > 0:
                paths.append(Load(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))
        return paths

def readinput(): 
    with open("input.json", 'w') as json_file:
        input = json.load(json_file)
    return input

#Assumes that the input is a list as such: [{"input_trip_id":101,"load_ids":[123123,12312]},{"input_trip_id":102,"load_ids":[123,12311,598234]}]
def createoutput(results):
    with open('output.json','w') as json_file:
        json.dump(results, json_file)
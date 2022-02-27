from cmath import inf
from datetime import *
import math
from Justin import *

    # find distance between 2 locations in miles

def calculateDistance():
    return 2

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


def main():
    trucker = Trucker(datetime.fromisoformat('2011-11-04 05:00:00'))
    load = Load(datetime.fromisoformat('2011-11-04 06:00:00'))
    print(pickUpHour(load, trucker))

main()
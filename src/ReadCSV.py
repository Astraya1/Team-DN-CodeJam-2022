import csv

class request:
    def __init__(self, id, ogcity, ogstate, oglat, oglong, destcity, deststate, destlat, destlong, amount, timedate) -> None:
        self.id = id
        self.ogcity = ogcity
        self.ogstate = ogstate
        self.oglat = oglat
        self.oglong = oglong
        self.destcity = destcity
        self.deststate = deststate
        self.destlat = destlat
        self.destlong = destlong
        self.amount = amount
        self.timedate = timedate

def readcsv(csvfile): #Variable 'csvfile' should be the file name of the data sheet ie. dataset.csv
    with open(csvfile, 'r') as csv_file:
        csvfile = csv.reader(csv_file)

        paths = []
        for line in csvfile: #Creates a list which contains all truck route requests, with information stored as attributes given by the request class.
            paths.append(request(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))
        
        return paths
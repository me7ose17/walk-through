# Establish safety perception sequence of streets, buffer radius r

import sys
import csv
from geopy.distance import geodesic
import numpy as np

# Buffer radius: 150
r = 150
result = {}

# Calculate the distance between two points
def distance(point1, point2):
    distance = geodesic((point1[1], point1[0]), (point2[1], point2[0])).m
    return distance


# Read sample points of streets
sample_streets = {}
rfile1 = 'F:\\StreetSimilarity\\new\\road_sample.csv'
rf1 = open(rfile1, 'r')
reader = csv.reader(rf1)

for row in reader:
    sample_streets[row[0]] = []
    for i in range(1, len(row)):
        if row[i] == '':
            break
        str_point = row[i][1:-2].split(",")
        point = (float(str_point[0]), float(str_point[1]))
        sample_streets[row[0]].append(point)
rf1.close()
print("Sample points read!")


# Read safety perception scores
mapdic = {}
map_location_dic = {}
streetmap = {}

rfile = 'F:\\StreetSimilarity\\new1\\safe_in_road.csv'
rf = open(rfile, 'r')
for line in rf:
    listline = line[:-1].split(",")
    
    # Mapping street view point coordinates
    map_location_dic[listline[2]] = [listline[3], listline[4]]

    # Mapping street to street view points
    if listline[0] not in streetmap.keys():
        streetmap[listline[0]] = []
    streetmap[listline[0]].append(listline[2])

    score = listline[5]
    if score == 'score':
        continue
    mapdic[listline[2]] = float(score)

rf.close()
print("Scores read!")


# Calculate safety perception sequence for each street
for street in streetmap.keys():
    if street == 'osm_id':
        continue
    result[street] = []
    # All street view point IDs on the street
    maps = streetmap[street]
    # All sample points on the street
    samples = sample_streets[street]

    for sample in samples:
        k = 0
        # Safety score for the sample point
        score = 0
        # Iterate through each street view ID
        for map in maps:
            if distance(map_location_dic[map], sample) < r:
                score = score + mapdic[map]
                k = k + 1
        if k > 0:
            result[street].append(score / k)
    print(street)


# Write the safety perception sequence to a CSV file
wf = open('F:\\StreetSimilarity\\new1\\SafetyPerceptionSequence.csv', 'w', newline="")
csv_writer = csv.writer(wf)

for street in result.keys():
    score = [street, ]
    score.extend(result[street])
    csv_writer.writerow(score)
wf.close()

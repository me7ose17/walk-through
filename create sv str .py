# -*- coding:utf-8 -*-

# Create the landscape sequence of the street, with buffer radius r
# Implementation method: First convert the string to decimal int()
# Then perform the "|" operation in decimal
# Convert the result to a string format( *,'014b') for storage (not implemented)

import sys
import csv
from geopy.distance import geodesic
r = 150

# Calculate the distance between two points
def distance(point1, point2):
    distance = geodesic((point1[1], point1[0]), (point2[1], point2[0])).m
    return distance

# Read the sampling points of the street
sample_streets = {}
result = {}
rfile1 = 'F:\\Street Similarity\\new\\road_sample.csv'
rf = open(rfile1, 'r')
reader = csv.reader(rf)

for row in reader:
    sample_streets[row[0]] = []
    for i in range(1, len(row)):
        if row[i] == '':
            break
        str_point = row[i][1:-2].split(",")
        point = (float(str_point[0]), float(str_point[1]))
        sample_streets[row[0]].append(point)
rf.close()
print("read sample!")

mapdic = {}
map_location_dic = {}
streetmap = {}
rfile = 'F:\\Street Similarity\\new\\sv_in_buffer.csv'
rf = open(rfile, 'r')
for line in rf:
    listline = line[:-1].split(",")
    # Mapping street view point coordinates
    map_location_dic[listline[2]] = [listline[3], listline[4]]
    # Mapping street to street view points
    if listline[0] not in streetmap.keys():
        streetmap[listline[0]] = []
    streetmap[listline[0]].append(listline[2])
    # Mapping co-occurrence of street view elements
    # "".join(listline[5:]) converts the list to a string
    mapdic[listline[2]] = "".join(listline[5:])
rf.close()
print("read streetmap!")

for street in streetmap.keys():
    if street == 'osm_id':
        continue
    result[street] = []
    # All street view point IDs on the street
    maps = streetmap[street]
    # All sampling points on the street
    samples = sample_streets[street]

    for sample in samples:
        # Co-occurrence of street view elements near the sampling point
        pattern = 0
        # For a specific street view ID
        for map in maps:
            if distance(map_location_dic[map], sample) < r:
                pattern = pattern | int(mapdic[map], 2)
        # par = format(result[pattern], '014b')
        if pattern > 0:
            result[street].append(pattern)
    print(street)

wf = open('F:\\Street Similarity\\new\\landscape_sequence_no_empty.csv', 'w', newline="")
csv_writer = csv.writer(wf)
for street in result.keys():
    pattern = [street, ]
    # par = format(result[amap], '014b')
    pattern.extend(result[street])
    csv_writer.writerow(pattern)
wf.close()

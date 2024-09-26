# Establish the functional sequence of streets, buffer radius r

# Buffer radius: 150
radio = 150
result = {}

# Calculate the distance between two points
def distance(point1, point2):
    distance = geodesic((point1[1], point1[0]), (point2[1], point2[0])).m
    return distance

# Return the character that appears most frequently in a string
def most_frequent_char(s):
    if len(s) == 0:
        return ''
    # Initialize a dictionary to store the count of each character
    dic = {}
    # Iterate through each character in the string
    for char in s:
        # If the character is not in the dictionary, add it with a value of 1
        if char not in dic:
            dic[char] = 1
        # If the character is in the dictionary, increment its value by 1
        else:
            dic[char] += 1
    # Sort the dictionary items by value in descending order
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    # Return the character that appears most frequently
    return sorted_dic[0][0]

# Read the sample points of the streets
sample_streets = {}
rfile1 = 'F:\\街道的相似性\\new\\road_sample.csv'
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
print("read sample!")

# Read poi classification
poidic = {}  # Store the types of poi points
map_location_dic = {}  # Store the coordinates of poi points
streetmap = {}  # Store the poi points on the streets

rfile = 'F:\\街道的相似性\\new\\poi_in_buffer_with_class.csv'
rf = open(rfile, 'r')
for line in rf:
    listline = line[:-1].split(",")
    # Map street view point coordinates
    map_location_dic[listline[2]] = [listline[3], listline[4]]
    # Map street view points
    if listline[0] not in streetmap.keys():
        streetmap[listline[0]] = []
    streetmap[listline[0]].append(listline[2])
    poi_class = listline[5]
    if poi_class == 'class':
        continue
    poidic[listline[2]] = listline[5]
rf.close()
print("read class!")

for street in streetmap.keys():
    if street == 'osm_id':
        continue
    result[street] = []
    # All street view point ids on the street
    pois = streetmap[street]
    # All sample points on the street
    samples = sample_streets[street]

    for sample in samples:
        k = 0
        # Classification of the sample point
        poi_class = ''
        # A certain poi id
        for poi in pois:
            if distance(map_location_dic[poi], sample) < radio:
                poi_class = poi_class + poidic[poi]
        if len(poi_class) > 0:
            result[street].append(most_frequent_char(poi_class))

wf = open('F:\\街道的相似性\\new\\功能序列_去空.csv', 'w', newline="")
csv_writer = csv.writer(wf)

for stree in result.keys():
    score = [stree, ]
    score.extend(result[stree])
    csv_writer.writerow(score)
wf.close()

import csv
streets = {}

# Define the path to the CSV file
rfile = 'F:\\街道的相似性\\new\\sample.csv'
rf = open(rfile, 'r')

# Read the CSV file line by line
for line in rf:
    listline = line[:-1].split(",")  # Remove the newline and split the line by commas
    x = listline[1]  # Get the second column (longitude)
    
    # Skip the header line
    if x == 'POINT_X':
        continue
    
    # If the street is not already in the dictionary, add it
    if listline[0] not in streets.keys():
        streets[listline[0]] = []
    
    # Convert the second and third columns to float (longitude, latitude)
    point = (float(x), float(listline[2]))
    
    # Append the point to the corresponding street's list
    streets[listline[0]].append(point)

rf.close()

# Write the results to a new CSV file
wf = open('F:\\街道的相似性\\new\\road_sample.csv', 'w', newline="")
csv_writer = csv.writer(wf)

# Write each street and its associated points to the CSV file
for stre in streets.keys():
    partten = [stre, ]  # Start with the street identifier
    partten.extend(streets[stre])  # Add the list of points
    csv_writer.writerow(partten)  # Write the row to the file

wf.close()

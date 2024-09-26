import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Read the line feature shapefile containing road geometries
roads = gpd.read_file('F:\\街道的相似性\\new\\map_data\\road.shp')

# Read the road attribute data from a CSV file
road_attrs = pd.read_csv('F:\\街道的相似性\\new\\similarity\\road_501540617_no.csv')

# Normalize three similarity features to the range of 0-255 for RGB channel values
road_attrs['R'] = np.interp(road_attrs['similarity_SV'], (0, 1), (0, 255))
road_attrs['G'] = np.interp(road_attrs['similarity_function'], (0, 1), (0, 255))
road_attrs['B'] = np.interp(road_attrs['similarity_safe'], (0, 1), (0, 255))

# Convert 'osm_id' to string type for merging
road_attrs['osm_id'] = road_attrs['osm_id'].astype(str)

# Merge the road attributes (including RGB values) with the road geometries based on 'osm_id'
roads = roads.merge(road_attrs[['osm_id', 'R', 'G', 'B']], on='osm_id')

# Set the plotting style to a dark background
plt.style.use('dark_background')

# Create a figure and axis for plotting with a specified size
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_facecolor('black')  # Set the background color of the axis

# Highlight the road with a specific 'osm_id'
highlighted_road = roads.loc[roads['osm_id'] == '501540617']
# Plot the highlighted road with a thicker line and its corresponding color
highlighted_road.plot(ax=ax, color=highlighted_road[['R', 'G', 'B']].values / 255, linewidth=4)

# Plot all roads with their respective colors and thinner lines
roads.plot(ax=ax, color=roads[['R', 'G', 'B']].values / 255, linewidth=0.8)

# Remove axis for a cleaner visualization
ax.set_axis_off()
ax.autoscale(tight=True)  # Adjust the axis limits to fit the data tightly

# Save the resulting plot as a PNG file with high resolution
plt.savefig(f'F:\\街道的相似性\\new\\similarity\\501540617_no.png', dpi=400)

# Display the plot
plt.show()

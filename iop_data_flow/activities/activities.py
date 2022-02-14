# We need to import numpy and matplotlib library

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
import contextily as cx

# Using data from 2021
#activities = pd.read_csv('../../data/studio/activities/sort_activities.csv')
# Read only 1000 rows
activities = pd.read_csv('../../data/studio/activities/sort_activities.csv', nrows=1000)

# Select only empty coordinates
activities_invalid = activities[(activities['COORD_X'].isna()) | (activities['COORD_Y'].isna())]

# Filtering empty coordinates
activities_clean = activities[(activities['COORD_X'].notna()) & (activities['COORD_Y'].notna())]

# Filtering values for relative humidity and precipitation
# eixample_activities = activities[activities['DISTRITO'].isin(['Eixample'])]
# Note: This is cleaner when you want to filter on only value
eixample_activities = activities_clean[activities_clean['DISTRITO'] == 'Eixample']

print(eixample_activities)

crs = {'init': 'epsg:4326'}
geometry = [Point(xy) for xy in zip(eixample_activities["COORD_X"], eixample_activities["COORD_Y"])]
eixample_activities_geo = geopandas.GeoDataFrame(eixample_activities, crs=crs, geometry=geometry)

print(eixample_activities_geo)

ax = eixample_activities_geo.plot()
cx.add_basemap(ax, crs=eixample_activities_geo.crs)
plt.show()

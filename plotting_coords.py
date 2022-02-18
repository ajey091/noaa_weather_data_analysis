import pandas as pd
import numpy as np
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt


locations = {'Tokyo':'476620-99999',
             'Bangalore':'427056-99999',
             'Shanghai':'583620-99999',
             'Paris':'071570-99999',
             'Mexico_City':'766800-99999',
             'Cairo':'623660-99999',
             'Chicago':'725300-94846',
             'San_Francisco':'724940-23234',
             'Miami':'722040-12838',
             'Buenos_Aires':'875850-99999'}


isd_history = pd.read_csv('isd-history.csv')

lat = []
long = []

for city in locations:
    id = locations[city]
    id1,id2 = id.split('-')
    long.append(isd_history.loc[(isd_history['USAF'] == id1)]['LAT'].values[0])
    lat.append(isd_history.loc[(isd_history['USAF'] == id1)]['LON'].values[0])
    # print (lat,long)

df = pd.DataFrame(np.transpose(np.array([lat,long])),columns=['lat','long'])


geometry = [Point(xy) for xy in zip(df['lat'],df['long'])]
gdf = GeoDataFrame(df, geometry=geometry)

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=20);
plt.show()

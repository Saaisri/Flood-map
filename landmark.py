from sklearn.neighbors import DistanceMetric
from math import radians
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

# cities_df = pd.read_csv('landmark.csv')

cities = pd.DataFrame(data={
   'City': ['Denver', 'Miami', 'Chicago'],
   'Lat' : [39.7645187, 25.7825453, 41.8339037],
   'Lon' : [-104.9951948, -80.2994985, -87.8720471]
})

# cities_df['lat'] = np.radians(cities_df['lat'])
# cities_df['lon'] = np.radians(cities_df['lon'])

# cities_df.head()

start_lat, start_lon = 	40.6976637, -74.1197643

distances_km = []

for row in cities.itertuples(index=False):
   distances_km.append(haversine(start_lat, start_lon, row.Lat, row.Lon))

print(distances_km)
cities['DistanceFromNY'] = distances_km
# author: github.com/teo113
# desc: This script loads a geopandas dataframe from file and plots the data.

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
#import pyproj

csv_file = r'data/pandas_locs.csv'

# use pandas to read a csv file in as a data frame (df)
df = pd.read_csv(f'{csv_file}', index_col='id', dtype={'id': 'uint32',
                                                       'rv_loc': 'string',
                                                       'notes': 'string',
                                                       'xco': 'float64',
                                                       'yco': 'float64',
                                                       'gtype': 'string',
                                                       'srid': 'uint16'
                                                       })
print(df)

# create geodataframe
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.xco, df.yco), crs='EPSG:27700')
print(gdf.head())

# define projections OLD?
#wgs84 = pyproj.Proj(init='epsg:4326')
#bng = pyproj.Proj(init='epsg:27700')

# get country boundary data
gb_map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
gb_map.crs
gb_map = gb_map.to_crs('EPSG:27700')

# restrict map to UK
ax = gb_map[gb_map.name == 'United Kingdom'].plot(
    color='white', edgecolor='black')

# plot map
gdf.plot(ax=ax, color='red')
plot.show()

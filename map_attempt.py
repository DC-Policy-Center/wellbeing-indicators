# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:37:04 2017

@author: mwatson
"""

# Import the necessary modules

fname = r'Ward from 2012\Ward_from_2012.shp'

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import geoviews as gv
'''
ax = plt.axes(projection=ccrs.LambertConformal())
shape_feature = ShapelyFeature(Reader(fname).geometries(),
                                ccrs.PlateCarree(), edgecolor='black')



ax.background_patch.set_visible(False)
ax.outline_patch.set_visible(False)
ax.add_feature(shape_feature)
plt.show()
'''
shapefile = "Ward from 2012/Ward_from_2012.shp"
gv.Shape.from_shapefile(shapefile, crs=ccrs.PlateCarree())
####################################################################
# File name: map1.py                                               #
# Author: Hedaya Khalif                                            #
# Description: Interactive Web Mapping of Volcanoes and Population  #
####################################################################

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt") #loads csv into pandas dataframe
lat = list(data["LAT"]) #creates list of latitude objects
lon = list(data["LON"]) #creates list of longtitude objects
elev = list(data["ELEV"]) #creates list of elevation objects

#function classifies marker color based on elevation
def color_producer(elevation):
    if elevation <1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#creates centre of map object to Kansas with a zoom factor and terrain map features
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

#creates volcano feature group
fgv = folium.FeatureGroup(name="Volcanoes")

#adds volcano marker layer from list to map with dynamic popup message and elevation color classification
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup= str(el) +" m",
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

#creates population feature group
fgp = folium.FeatureGroup(name="Population")

#adds polygon layer to map with color classification based on population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

#adds layer control to map to turn on/off marker and polygon layers
map.add_child(folium.LayerControl())
#renders python into html
map.save("Map1.html")

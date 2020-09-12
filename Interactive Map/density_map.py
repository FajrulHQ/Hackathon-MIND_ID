import pandas as pd
import utm
import folium
from folium.plugins import MarkerCluster, HeatMap
import numpy as np
from folium import plugins
import matplotlib.pyplot as plt

df = pd.read_csv('database.csv',encoding='latin1', quotechar='"')

def plot_density(source):
    map = folium.Map([source.LAT.mean(), source.LON.mean()], tiles='Stamen Terrain',zoom_start=10)
    HeatMap(data=source[['LAT','LON']], radius=20).add_to(map)
    
    def PlotDot(point):
        folium.Circle(location=[point.LAT, point.LON],
                        radius=4,
                        popup=point.MINERAL_POTENTIAL,
                        color='#7FFF5F'
                        ).add_to(map)

    source.apply(PlotDot,axis=1)
    map.fit_bounds(map.get_bounds())
    map.save(r'D:\Fajrul\Internship\Hackathon MIND ID\Interactive Map\Map {}.html'.format(source.MINERAL_POTENTIAL.values[0]))

for i in range(26):
    data = df[df.MINERAL_CODE == i+1]
    plot_density(data)
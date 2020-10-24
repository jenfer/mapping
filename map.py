import folium
import pandas

data = pandas.read_csv("resource/Volcanoes.txt")
nam = list(data["NAME"])
typ = list(data["TYPE"])
lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s volcano%%22" target="_blank">%s</a> <br>
Type: %s <br>
Elevation: %s
"""


map = folium.Map(location=[48.7767982, -121.8109970], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, tp, el in zip(lat, lon, nam, typ, ele):
    # marker = f"Name:{nm}\nElevation:{el}"
    iframe = folium.IFrame(html=html % (nm, nm, tp, el), width=200, height=150)
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)


map.save("map.html")
# Mapping
A basic html generated in Python using folium

## Setup for Windows
Get the code:

```
git clone https://github.com/jenfer/mapping.git
```

Download and install Python 3.6 or higher. You can also install via Microsoft Store

```
http://python.org
```


Install folium
```
pip install folium
```

Open python shell
```
>>> import folium
>>> map = folium.Map(location=[37.756648, -122.429375])
>>> map.save("map.html")
```
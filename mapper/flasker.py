from flask import Flask, render_template, request
import geemap.foliumap  as gm
from geemap import folium as fm

class Map:
    def __init__(self, latitude, longitude, zoom=19.4, basemap='Esri.WorldImagery'):
        self.M = gm.Map(center=(latitude, longitude),zoom=zoom)
        self.M.add_basemap(basemap=basemap)
        self.M.add_text(text= f'Lat:{latitude} Lon: {longitude}', fontsize=15, position= 'bottomleft')

    def addmarker(self,name, latitude, longitude, sz=(45,50)):
        # myicon=Icon(icon_url=f"mapIcons/{name}",icon_size=sz,)
        # marker = Marker(location=(latitude, longitude), icon=myicon)
        fmicon = fm.CustomIcon(icon_image=f"mapIcons/{name}", icon_size=sz)
        self.M.add_marker(location=(latitude,longitude), icon=fmicon, draggable=True,)
    
    def show(self):
        #gm.ee_export_image(ee.Image(self.M), 'map.png')
        return self.M.to_html()

app = Flask(__name__)
# change this value when adding new icon
n = 8

@app.route('/', methods=['GET', 'POST'])
def index():
    isShowing = False
    if request.method == 'POST':
        # Get values from the form
        lat = float(request.form.get('text_field1'))
        lon = float(request.form.get('text_field2'))
        map_type = request.form.get('text_field3')
        icons = request.form.getlist('multi_select')
        icon_count = [int(request.form.get(f'text_fieldop{i}')) if request.form.get(f'text_fieldop{i}')!="" else 0 for i in range(1,n+1)]
        icon_dict = {}
        # Perform actions with the form values
        # For this example, we'll just print them
        print("Text Field 1:", lat)
        print("Text Field 2:", lon)
        print("Multi-Select:", icons)
        print("icons: ", icon_count)

        for key, value in zip(icons, icon_count):
            icon_dict[key] = value
        
        webmap = Map(lat, lon, basemap=map_type)

        for icon in icon_dict.keys():
            for i in range(icon_dict[icon]):
                webmap.addmarker(name=f'{icon}.png', latitude=lat, longitude=lon,)

        if ~isShowing:
            return webmap.M.to_html()
            isShowing = ~isShowing

    return render_template('owo.html')

if __name__ == '__main__':
    app.run(debug=True)

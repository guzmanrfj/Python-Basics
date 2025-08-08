#Ejemplo de como geenrar un mapa mediante folium en python

import folium

def generar_mapa():
        latitud: 20.671661421692075
        longitud:-103.34432713013703
        
        mapa = folium.Map(location=[latitud,longitud], zoom_start = 13)

        mapa.save("mapa.html")

generar_mapa

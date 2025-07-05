# ruta_ciudades.py
import requests

def calcular_ruta(origen, destino, transporte):
    url = "https://graphhopper.com/api/1/route"
    parametros = {
        "point": [origen, destino],
        "vehicle": transporte,
        "locale": "es",
        "instructions": "true",
        "key": "TU_API_KEY"
    }

    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()

    distancia_km = datos['paths'][0]['distance'] / 1000
    tiempo_minutos = datos['paths'][0]['time'] / 60000
    instrucciones = datos['paths'][0]['instructions']

    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Tiempo estimado: {tiempo_minutos:.2f} minutos")
    print("Ruta sugerida:")
    for paso in instrucciones:
        print("-", paso['text'])

while True:
    origen = input("Ingrese la ciudad de origen (o 's' para salir): ")
    if origen.lower() == 's':
        break
    destino = input("Ingrese la ciudad de destino: ")
    transporte = input("Ingrese medio de transporte (car, bike, foot): ")
    calcular_ruta(origen, destino, transporte)

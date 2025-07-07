 from geopy.distance import geodesic

# Diccionario de ciudades con sus coordenadas (Latitud, Longitud)
ciudades = {
    "Santiago": (-33.4489, -70.6693),
    "Valparaíso": (-33.0472, -71.6127),
    "Buenos Aires": (-34.6037, -58.3816),
    "Mendoza": (-32.8908, -68.8272),
    "Córdoba": (-31.4201, -64.1888),
    "Rosario": (-32.9442, -60.6505)
}

# Velocidades promedio por medio de transporte (km/h)
velocidades = {
    "Auto": 90,
    "Avión": 800,
    "Caminando": 5
}

while True:
    print("\n--- Calculadora de Distancias Chile-Argentina ---")
    origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ").title()
    if origen.lower() == 's':
        break
    destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ").title()
    if destino.lower() == 's':
        break

    if origen not in ciudades or destino not in ciudades:
        print("Una o ambas ciudades no están disponibles en la base de datos.")
        continue

    distancia_km = geodesic(ciudades[origen], ciudades[destino]).kilometers
    distancia_millas = distancia_km * 0.621371

    print("\nSeleccione el medio de transporte:")
    print("1. Auto")
    print("2. Avión")
    print("3. Caminando")
    opcion = input("Ingrese el número de su elección (o 's' para salir): ")

    if opcion.lower() == 's':
        break

    transporte = {
        "1": "Auto",
        "2": "Avión",
        "3": "Caminando"
    }.get(opcion, None)

    if transporte is None:
        print("Opción no válida.")
        continue

    duracion_horas = distancia_km / velocidades[transporte]

    print(f"\nDistancia entre {origen} y {destino}:")
    print(f"- {distancia_km:.2f} km")
    print(f"- {distancia_millas:.2f} millas")
    print(f"- Duración estimada del viaje en {transporte}: {duracion_horas:.2f} horas.")
    print(f"\nNarrativa del viaje:")
    print(f"Desde {origen} hasta {destino}, recorrerás aproximadamente {distancia_km:.2f} km en {transporte}.")

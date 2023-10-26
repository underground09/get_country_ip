import requests
import json

def get_location(ip_address, access_token):
    try:
        url = f"https://ipinfo.io/{ip_address}/json?token={access_token}"
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return {"ip": ip_address, "error": "IP no válida"}

# Tu token de acceso para ipinfo.io
access_token = "1b61cb5a375f95"

# Leer las direcciones IP desde el archivo y almacenarlas en una lista
with open("ip.txt", "r") as file:
    ip_addresses = file.readlines()

# Almacenar la información de geolocalización para cada IP
geolocation_data = []

for ip in ip_addresses:
    ip = ip.strip()  # Eliminar espacios en blanco y saltos de línea
    if ip:  # Solo procesar la IP si no está vacía
        location_data = get_location(ip, access_token)
        print(f"Información de geolocalización para la IP {ip}:")
        print(f"Pais: {location_data.get('country', 'Desconocido')}")
        print(f"Región: {location_data.get('region', 'Desconocido')}")
        print(f"Ciudad: {location_data.get('city', 'Desconocido')}")
        geolocation_data.append(location_data)

# Escribir toda la información en un archivo JSON
with open("geolocation_data.json", "w") as json_file:
    json.dump(geolocation_data, json_file, indent=4)

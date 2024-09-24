import requests
import time

# URL del endpoint donde se recibirán las coordenadas
url = 'http://127.0.0.1:5000/sms'

# Lista de coordenadas simuladas (latitud, longitud)
coordinates_list = [
    {'Body': 'lat: -34.6037, lon: -58.3816'},  # Coordenadas iniciales (Buenos Aires)
    {'Body': 'lat: -34.6038, lon: -58.3820'},  # Movimiento 1
    {'Body': 'lat: -34.6039, lon: -58.3825'},  # Movimiento 2
    {'Body': 'lat: -34.6040, lon: -58.3830'},  # Movimiento 3
    {'Body': 'lat: -34.6041, lon: -58.3835'},  # Movimiento 4
]

for coords in coordinates_list:
    # Enviar la solicitud POST al servidor
    response = requests.post(url, data=coords)
    
    # Imprimir la respuesta del servidor
    print(response.text)
    
    # Esperar 2 segundos antes de enviar la próxima coordenada
    time.sleep(2)

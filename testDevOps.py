import requests

# URL a la que se va a hacer la solicitud
url = 'https://exercism.org/tracks/python'

# Hacer la solicitud GET
response = requests.get(url)

# Mostrar el código de estado de la respuesta
print(response.status_code)

# Mostrar el contenido de la respuesta
print(response.text)
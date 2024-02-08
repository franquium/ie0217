import requests

# Ejemplo GET

# Definir los parametros para la peticion GET
payload = {'clave1': 'valor1', 'clave2': 'valor2'}
# Realizamos la peticion GET con los parametros
response = requests.get('https://ejemplo.com/ruta', params = payload)
# Mostrar el texto de la respuesta
print(response.text)

# Ejemplo POST

# Definir el cuerpo de la peticion POST
payload = {'usuario': 'juan', 'contrasena': 'secreta'}
# Realizar la peticion POST con el payload de la peticion
response = requests.post('https://ejemplo.com/login', data = payload)
# Mostrar el texto de la respuesta
print(response.text)

# En este ejemplo se realiza una peticion POST enviando el payload como JSON
payload = {'usuario': 'juan', 'contrasena': 'secreta'}
response = requests.post('https://ejemplo.com/login', json  =payload)
print(response.text)

import requests

# Ejemplo 1

# Realizamos una peticion GET a la URL proporcionada
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Imprimime el tipo de objeto de 'response'
print("Tipo: ", type(response))

# Muestra el objeto de respuesta completo
print("Respuesta: ", response)

# Muestra el texto de la respuesta
print("Respuesta text: ", response.text)

# Muestra todo lo que venia en el dict de la respuesta
print("Respuesta:", response.__dict__)


# Ejm 2: Google

url = "https://www.google.com"

response2 = requests.get(url)

print(response2.text)
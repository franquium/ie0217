import requests

# Manejo de Errores
try:
    response = requests.get('https://ejemplo.com/pagina-inexistente')
    response.raise_for_status()  # Genera una excepcion si hay un error HTTP
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")
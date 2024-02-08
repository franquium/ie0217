import requests

# Paso 1. Realizar una solicitud para obtener datos de usuarios

users_response = requests.get('https://jsonplaceholder.typicode.com/users')
users_data = users_response.json()

# Paso 2. Realizar una solicitud para obtener datos de publicaciones

posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
# El metodo .json() convierte la respuesta de la pagina web de formato JSON 
# a un objeto Python: una lista de diccionarios
posts_data = posts_response.json()

# Paso 3. Procesar los datos para obtener informacion relevante
# Un diccionario vacio para almacenar las publicaciones de cada usuario
user_posts = {}

# llenar el diccionario con los datos de los usuarios
for user in users_data:
    user_posts[user['id']] = []

# Iterar sobre cada post y se agrega al usuario correspondiente.
for post in posts_data:
    # Usar .get() para evitar KeyError
    user_id = post.get('userId')  
    if user_id in user_posts:
        user_posts[user_id].append({
            'title': post['title'],     # Agregar titulo del post
            'body': post['body']     # Agregar cuerpo del post
        })

# Paso 4. Mostrar los resultados
# Iterar sobre usuario
for user_id, posts in user_posts.items():
    # next() devuelve el primer resultado del generador
    user = next((user for user in users_data if user['id'] == user_id), None)
    if user:
        print(f"\nPublicaciones de {user['name']} ({user['email']}):\n")
        for post in posts:
            print(f"Title: {post['title']}\nBody: {post['body']}\n")
    else:
        # Si no se encuentra el usuario imprime este mensaje
        print(f"No se encontraron datos para el usuario con ID {user_id}")

import aiohttp
import asyncio

# Lista de endpoints públicos (JSONPlaceholder)
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

# Función asincrónica que hace una petición HTTP y extrae el título
async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        print(f"{url} → Título: {data['title']}")

async def main():
    # Usamos una sesión HTTP reutilizable
    async with aiohttp.ClientSession() as session:
        # Creamos una lista de tareas
        tareas = [fetch(session, url) for url in urls]
        # Ejecutamos todas las tareas concurrentemente
        await asyncio.gather(*tareas)

# Lanza el programa
asyncio.run(main())

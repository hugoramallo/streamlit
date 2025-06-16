# SOLUCIONES - EJERCICIOS DE ASINCRONÍA EN PYTHON (VARIANTE)

import asyncio
import aiohttp

# EJERCICIO 1
async def iniciar_sesion():
    print("Inicio")
    await asyncio.sleep(1.5)
    print("Sesión iniciada")

# asyncio.run(iniciar_sesion())


# EJERCICIO 2
async def tarea_lenta():
    await asyncio.sleep(3)
    print("Tarea lenta lista")

async def tarea_media():
    await asyncio.sleep(2)
    print("Tarea media lista")

async def tarea_rapida():
    await asyncio.sleep(1)
    print("Tarea rápida lista")

async def ejecutar_tareas():
    await asyncio.gather(tarea_lenta(), tarea_media(), tarea_rapida())

asyncio.run(ejecutar_tareas())


# EJERCICIO 3
async def obtener_dato(session, url):
    async with session.get(url) as response:
        data = await response.json()
        print(f"Nombre: {data['name']}")

asyncio.run(obtener_dato(aiohttp.ClientSession(), "https://jsonplaceholder.typicode.com/users/1"))


# EJERCICIO 4
async def obtener_nombres(urls):
    async with aiohttp.ClientSession() as session:
        tareas = [obtener_dato(session, url) for url in urls]
        await asyncio.gather(*tareas)

urls = [f"https://jsonplaceholder.typicode.com/users/{i}" for i in range(1, 4)]
asyncio.run(obtener_nombres(urls))


# EJERCICIO 5
async def operacion_lenta():
    await asyncio.sleep(4)

async def con_timeout():
    try:
        await asyncio.wait_for(operacion_lenta(), timeout=2)
    except asyncio.TimeoutError:
        print("Tiempo agotado")

# asyncio.run(con_timeout())


# EJERCICIO 6
async def tarea_cancelable():
    try:
        await asyncio.sleep(5)
        print("Tarea terminada")
    except asyncio.CancelledError:
        print("Tarea cancelada")

async def ejecutar_cancelacion():
    tarea = asyncio.create_task(tarea_cancelable())
    await asyncio.sleep(1)
    tarea.cancel()
    await tarea

asyncio.run(ejecutar_cancelacion())



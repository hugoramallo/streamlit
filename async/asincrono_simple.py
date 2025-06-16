import asyncio

# Definimos una función asincrónica con 'async def'
async def saludar():
    print("Hola")
    # 'await' espera 1 segundo sin bloquear otras tareas
    await asyncio.sleep(1)
    print("Adiós")

# Ejecutamos la función asincrónica con asyncio.run()
asyncio.run(saludar())



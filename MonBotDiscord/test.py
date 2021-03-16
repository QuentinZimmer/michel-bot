from datetime import datetime
import asyncio
async def message():
    while True:
        await asyncio.sleep(0.5)
        print(1)



async def message_2():
    while True:
        await asyncio.sleep(2)
        print(2)

asyncio.run(message_2())
asyncio.run(message())
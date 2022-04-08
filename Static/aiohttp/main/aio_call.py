import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup as BS

async def GetEp():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://gogoanime.film/category/detective-conan') as response:

           ## print("Status:", response.status)
           ## print("Content-type:", response.headers['content-type'])

            #html = str(response.text)
            json_data = await response.text()
            json_data = json.dumps(json_data)
            with open('EpDataJson.txt', 'w', encoding='utf-8') as f:
               f.write(json_data)
               f.close()
            Html_code = BS(await response.text(),features="lxml")
            with open("EpDataBS.txt","w+",encoding="utf-8") as f:
                f.write(str(Html_code).replace("><",">\n<"))
                f.close()


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://gogoanime.film/category/detective-conan') as response:

           ## print("Status:", response.status)
           ## print("Content-type:", response.headers['content-type'])

            #html = str(response.text)
            json_data = await response.text()
            json_data = json.dumps(json_data)
            print(json_data)
            #print(json_data)
            with open('html_data.txt', 'w', encoding='utf-8') as f:
               f.write(json_data)
               f.close()

async def main2():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(GetEp())
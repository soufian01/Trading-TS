import aiohttp
import asyncio
import time
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd

apiKey = "4a5b0f1569f2e6952a07de4043845c54"

async def get_sp500_symbols():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                table = soup.find("table", {"id": "constituents"})
                if table:
                    symbols = []
                    rows = table.find_all("tr")[1:]  # Skipping header row
                    for row in rows:
                        symbol = row.find_all("td")[0].text.strip()
                        symbols.append(symbol)
                    return symbols
                else:
                    print("Table not found on the page.")
            else:
                print("Failed to fetch page. Status code:", response.status)

async def getStockData(session, apiKey, dataType):
    url = f"https://financialmodelingprep.com/api/v3/stock_market/{dataType}?apikey={apiKey}"
    async with session.get(url) as response:
        json_data = await response.json()
        return json_data

async def main():
    async with aiohttp.ClientSession() as session:
        return (
            await getStockData(session, apiKey, "gainers"),
            await getStockData(session, apiKey, "losers"),
            await getStockData(session, apiKey, "actives")
        )

def getTest(sessio, apiKey, dataType):
    url = f"https://financialmodelingprep.com/api/v3/stock_market/{dataType}?apikey={apiKey}"
    response = sessio.get(url)
    json_data = response.json()
    return json_data
from flask import Flask, request, jsonify
from .functions import main
from . import stocks
import yfinance as yf
import asyncio

@stocks.route('/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    # Simula il recupero dei dati degli stock basati sul simbolo fornito
    data = yf.download(symbol, start="2019-01-01", end="2024-01-01")
    data.reset_index(inplace=True)  # Reimposta l'indice per includere la colonna "Date"
    json_data = data.to_json(orient="records")
    print(json_data)
    return json_data

@stocks.route('/stock', methods=['GET'])
async def get_data():
    gainers, losers, most_active = await main()
    print(gainers)
    return jsonify({"gainers": gainers, "losers": losers, "most_active": most_active})



# Codice del backend Flask

from flask import Flask, request, jsonify
from .functions import *
from . import stocks
import yfinance as yf
import asyncio
import json

app = Flask(__name__)

@stocks.route('/stock/<symbol>', methods=['GET'])
async def get_stock(symbol):
    # Simula il recupero dei dati degli stock basati sul simbolo fornito
    data = yf.download(symbol, start="2019-01-01", end="2024-01-01")
    data.reset_index(inplace=True)  # Reimposta l'indice per includere la colonna "Date"
    json_data = data.to_json(orient="records")
    info = get_company_profile(symbol)
    return jsonify({"data": json.loads(json_data), "info": info}) # Modificato per convertire il DataFrame in JSON

@stocks.route('/stock', methods=['GET'])
async def get_data():
    gainers, losers, most_active = await main()
    return jsonify({"gainers": gainers, "losers": losers, "most_active": most_active})

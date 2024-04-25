from flask import Flask, request, jsonify
from . import main

@main.route('/data', methods=['GET'])
def get_data():
    # Logica per ottenere dati dal backend
    return jsonify({"message": "Dati ottenuti con successo"})

@main.route('/data', methods=['POST'])
def post_data():
    data = request.json
    # Logica per elaborare i dati inviati dal frontend
    return jsonify({"message": "Dati ricevuti con successo"})

from flask import Flask, request, jsonify
from flask_cors import CORS
from app.main.routes import main
from app.stocks.routes import stocks
from flask_caching import Cache

app = Flask(__name__)



app.config['SECRET'] = 'secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

CORS(app)


app.register_blueprint(main)
app.register_blueprint(stocks)
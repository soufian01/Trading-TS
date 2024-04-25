from flask import Blueprint
from flask_caching import Cache

stocks = Blueprint('stocks', __name__, template_folder='templates')
cache = Cache(config={'CACHE_TYPE': 'simple'})

from . import routes

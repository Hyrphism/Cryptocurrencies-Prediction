from product import Product
from db import Database

from flask import Flask, request
from flask import render_template
from flask import jsonify

KEYSPACE = "crytocurrencies"

app = Flask(__name__)

cass_db = Database()
product = Product(KEYSPACE, 'bitcoin')
product.save_to_db()

@app.route('/')
def index():
  pass

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0',port=5555)
import pandas as pd

from product import Product
from db import Database
from graph import *

from flask import Flask
from flask import render_template
from flask import jsonify

KEYSPACE = "crytocurrencies"

cass_db = Database()
btc_product = Product(KEYSPACE, table_name='bitcoin', ticker='BTC-USD')
btc_product.save_to_db()

app = Flask(__name__)

@app.route('/keyspaces/', methods=['GET'])
def get_keyspaces_info():
  query = "SELECT JSON * FROM system_schema.keyspaces;"
  keyspaces =  [keyspace for keyspace in cass_db.execute(query).all()]
  try:
    return jsonify(keyspaces)
  except:
    return 'An exception occurred while retrieving keyspaces', 500

@app.route('/keyspaces/<keyspace_name>/', methods=['DELETE'])
def delete_keyspace(keyspace_name):
  try:
    if cass_db.delete_keyspace(keyspace_name):
      return jsonify({
                'message': f'Deleted keyspace {keyspace_name}'
            }), 200
    return f'Keyspace {keyspace_name} not found', 404
  except:
    return f'An exception occurred while deleting the keyspace: {keyspace_name}', 500

@app.route('/keyspaces/<keyspace_name>/tables/', methods=['GET'])
def get_tables_info(keyspace_name):
  query = f"SELECT JSON table_name FROM system_schema.tables WHERE keyspace_name = '{keyspace_name}';"
  tables =  [table for table in cass_db.execute(query).all()]
  try:
    return jsonify(tables)
  except:
    return 'An exception occurred while retrieving tables', 500

@app.route('/keyspaces/<keyspace_name>/tables/<table_name>', methods=['DELETE'])
def delete_table(keyspace_name, table_name):
  try:
    cass_db.set_keyspace(keyspace_name)
    if cass_db.delete_table(table_name):
      return jsonify({
                'message': f'Deleted table {table_name}'
            }), 200
    return f'Table {table_name} not found', 404
  except:
    return f'An exception occurred while deleting the table: {table_name}', 500

@app.route('/bitcoin/all/', methods=['GET'])
def get_bitcoin_all():
  try:
    products = [product.json for product in btc_product.find_all(json=True)]
    return jsonify(products)
  except:
    return 'An exception occurred while retrieving all products', 500

@app.route('/bitcoin/now/', methods=['GET'])
def get_bitcoin_now():
  try:
    products = [product.json for product in btc_product.find_now(json=True)]
    return jsonify(products)
  except:
    return 'An exception occurred while retrieving all products', 500

@app.route('/bitcoin/line_chart/', methods=['GET'])
def bitcoin_line_chart():
  data = btc_product.find_now()
  df = pd.DataFrame(data).sort_values(by='datetime')
  line_chart(df, file_name='bitcoin')
  return render_template('bitcoin.html')

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0',port=5555)
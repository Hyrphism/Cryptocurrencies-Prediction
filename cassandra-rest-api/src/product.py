from datetime import datetime

from db import Database
import yfinance as yf

class Product:
  def __init__(self, keyspace, table_name, ticker) -> None:
    self.table_name = table_name
    self.data = yf.download(tickers=ticker, period='1d', interval='1m').reset_index()

    self.session = Database()
    self.session.create_keyspace(keyspace)
    self.session.set_keyspace(keyspace)
    self.session.create_table(table_name, 
                              column_and_type_list='datetime TIMESTAMP, open DOUBLE, high DOUBLE, low DOUBLE, close DOUBLE',
                              primary_key_list='datetime')

  @property
  def column_names(self):
    return "datetime, open, high, low, close"

  def save_to_db(self):
    datetime = self.data['Datetime']
    open = self.data['Open']
    high = self.data['High']
    low = self.data['Low']
    close = self.data['Close']

    for i in range(len(self.data)):
      values = f"'{datetime[i]}', {open[i]}, {high[i]}, {low[i]}, {close[i]}"
      self.session.insert_table(self.table_name, self.column_names, values)

    print(f"Save {len(self.data)} rows to table")

  def find_all(self, json=False):
    if json:
      query = "SELECT JSON * FROM %s" % self.table_name
    else:
      query = "SELECT * FROM %s" % self.table_name
    return self.session.execute(query).all()

  def find_now(self, json=False):
    date = datetime.now().date()
    if json:
      query = "SELECT JSON * FROM %s WHERE datetime > '%s' ALLOW FILTERING;" % (self.table_name, date)
    else:
      query = "SELECT * FROM %s WHERE datetime > '%s' ALLOW FILTERING;" % (self.table_name, date)
    return self.session.execute(query).all()

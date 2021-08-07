from cassandra.cluster import Cluster

class Database:
  def __init__(self) -> None:
    self.session = Cluster().connect()

  def execute(self, query):
    try:
      return self.session.execute(query)
    except Exception as e:
      print(e)

  def set_keyspace(self, keyspace):
    return self.session.set_keyspace(keyspace)
  
  def create_keyspace(self, keyspace):
    query = '''
               CREATE KEYSPACE IF NOT EXISTS %s 
               WITH replication={'class': 'SimpleStrategy', 'replication_factor': '2'}
            ''' % keyspace
    self.execute(query)

  def delete_keyspace(self, keyspace):
    query = "DROP KEYSPACE IF EXISTS %s" % keyspace
    self.execute(query)

  def create_table(self, table_name, column_and_type_list, primary_key_list):
    query =  '''
                CREATE TABLE IF NOT EXISTS %s (%s, PRIMARY KEY (%s))
             ''' % (table_name,column_and_type_list,primary_key_list)
    self.execute(query)

  def delete_table(self, table_name):
    query = "DROP KEYSPACE IF EXISTS %s" % table_name
    self.execute(query)

  def insert_table(self, table_name, column_names, values):
    query = "INSERT INTO %s (%s) VALUES (%s) IF NOT EXISTS;" % (table_name, column_names, values)
    self.execute(query)

  def update_data(self, table_name, column, value, constraint):
    query = "UPDATE %s SET %s = %s WHERE %s" %(table_name, column, value, constraint)
    self.execute(query)

  def close(self):
    self.session.shutdown()

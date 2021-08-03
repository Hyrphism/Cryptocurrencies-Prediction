from cassandra.cluster import Cluster
 
cluster = Cluster(["172.23.17.242"])
session = cluster.connect('crytocurrencies')

rows = session.execute('SELECT keyspace_name FROM system_schema.keyspaces').all()
print(rows[0][0])
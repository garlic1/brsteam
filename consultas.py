# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import psycopg2 as ps

conn = ps.connect('dbname=brsteam user=postgres password=123')
cur = conn.cursor()

cur.execute('SELECT * FROM Biblioteca')
print(cur.fetchall())

conn.close()

#! /usr/bin/env python

##	Dumps the Ottawa Parks SQLite Db to a Json file
#	@author	Thomas J Bradley <hey@thomasjbradley.ca>

import sqlite3
import json

dbconn = sqlite3.connect('ottawaparks.sqlite')
cur = dbconn.cursor()
cur.execute('SELECT * FROM ottawaparks ORDER BY name ASC')

parks = []

for row in cur:
	parks.append({
		'id': row[0],
		'name': row[1],
		'address': row[2],
		'neighbourhood': row[3],
		'latitude': row[4],
		'longitude': row[5],
		'dogs': row[6],
		'leashed': row[7],
		'restrictions': row[8],
		'notes': row[9]
	})
	
dbconn.close()

f = open('export/ottawaparks.json', 'w')
json.dump(parks, f, indent=2, separators=(',', ':'))
f.write('\n')
f.close()

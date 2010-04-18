#! /usr/bin/env python

##	Dumps the Ottawa Parks SQLite Db to a Csv file
#	@author	Thomas J Bradley <hey@thomasjbradley.ca>

import sqlite3

dbconn = sqlite3.connect('ottawaparks.sqlite')
cur = dbconn.cursor()
cur.execute('SELECT * FROM ottawaparks ORDER BY name ASC')

parks = ['"GUID","Name","Address","Neighbourhood","Latitude","Longitude","Dogs","Leashed","Restrictions","Notes"']

for row in cur:
	parks.append('"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"' % row)
	
dbconn.close()

f = open('export/ottawaparks.csv', 'w')
f.write('\n'.join(parks).encode('utf-8'))
f.write('\n')
f.close()

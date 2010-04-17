#! /usr/bin/env python

import sqlite3

dbconn = sqlite3.connect('ottawaparks.sqlite')
cur = dbconn.cursor()
cur.execute('SELECT * FROM ottawaparks ORDER BY name ASC')

parks = ['"Id","Name","Address","Neighbourhood","Latitude","Longitude","Dogs","Leashed","Restrictions","Notes"']

for row in cur:
	parks.append('"%d","%s","%s","%s","%s","%s","%s","%s","%s","%s"' % row)
	
dbconn.close()

f = open('export/ottawaparks.csv', 'w')
f.write('\n'.join(parks).encode('utf-8'))
f.write('\n')
f.close()

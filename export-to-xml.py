#! /usr/bin/env python

##	Dumps the Ottawa Parks SQLite Db to a Xml file
#	@author	Thomas J Bradley <hey@thomasjbradley.ca>

import sqlite3
from xml.dom.minidom import Document

dbconn = sqlite3.connect('ottawaparks.sqlite')
cur = dbconn.cursor()
cur.execute('SELECT * FROM ottawaparks ORDER BY name ASC')

doc = Document()
parks = doc.createElement('parks')
doc.appendChild(parks)

for row in cur:
	park = doc.createElement('park')
	park.setAttribute('guid', row[0])
	park.setAttribute('name', row[1])
	park.setAttribute('address', row[2])
	park.setAttribute('neighbourhood', row[3])
	park.setAttribute('latitude', str(row[4]))
	park.setAttribute('longitude', str(row[5]))
	park.setAttribute('dogs', str(row[6]))
	park.setAttribute('leashed', str(row[7]))
	park.setAttribute('restrictions', str(row[8]))
	
	if(row[9] != ''):
		notes = doc.createTextNode(row[9])
		park.appendChild(notes)
		
	parks.appendChild(park)
	
dbconn.close()

f = open('export/ottawaparks.xml', 'w')
f.write(doc.toprettyxml(encoding='utf-8'));
f.close()

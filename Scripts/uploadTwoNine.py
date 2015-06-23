import os
import psycopg2
import urlparse
import csv
from schoolName import * 
from existingNames import *
from connectDB  import *

# new_names = []

def pluck_all(props, reader):
    map(lambda row: pluck(props, row), reader)

def pluck(props, row):
    return [row[prop] for prop in props ]

# Upload 2009.csv data

# with open('2009.csv','rb') as twoNine:
# 	twoNineReader = csv.DictReader(twoNine)
# 	# values = map(lambda x: pluck(['LA number', 'institution name', 'institution type'], x), twoNineReader)
# 	for value in twoNineReader:
# 		if value['institution name'] != "":
# 			print(value['LA number'],value['institution name'])
# 			cursor.execute(
#             	"""INSERT INTO twothousandandnine (school_name,school_type)
#             	VALUES (%s, %s);""",
#             	(value['institution name'],value['institution type']))

with open('../2010.csv','rb') as twoNine:
	twoNineReader = csv.DictReader(twoNine)
	# values = map(lambda x: pluck(['LA number', 'institution name', 'institution type'], x), twoNineReader)
	for value in twoNineReader:
		if value['SchoolName'] != "":
			print(value['LACode'],value['SchoolName'])
			cursor.execute(
            	"""INSERT INTO twothousandandnine (school_name,school_type)
            	VALUES (%s, %s);""",
            	(value['SchoolName'],value['SchoolType']))

# with open('2010.csv','rb') as twoTen:
# 	twoTenReader = csv.DictReader(twoTen)
# 	for value in twoTenReader:
# 		if value['SchoolName']:		
# 			new_names.append(value['SchoolName'])




# found = False 

# reader = get_reader('../2010.csv')
# twoTenNames = get_schoolNames(reader,find_columnName(reader,schoolName_columnNames))

conn.commit()
cursor.close()
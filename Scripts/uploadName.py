from connectDB import *
from schoolName import *
from existingNames import *

# Uploaded for KS4 2009,2010,2005_Main,2005_Special,2006_Main,2006_Special,2007_KS4_Main_UTF,2007_KS4_Special
# 2008_KS4_Main,2008_KS4_Special + Karina's Master School Total DISTINCT COUNT from postgres 13261 @22/06/15

# 2008 Main has schools which are suppose to only be in 2008 Special e.g Chalcot & Swiss Cottage 

# filepath = "../Karinas_Master_List_UTF.csv"
# table_name = "two_thousand_fourteen"

# reader = get_reader(filepath)
# column_name = find_columnName(reader,schoolName_columnNames)
# new_names = get_schoolNames(reader,column_name)

# dE = doesntExist(new_names,existing_names)
# dropped = droppedNames(existing_names,new_names)

# print "\n\nTaking school names from file: " + filepath + "\n"
# print "School Names that don't currently exist in the database but do in this list\n"
# print dE
# print '\n####################################################################################################\n' 
# # print "School names that are in the database but not in this list\n"
# # print dropped

# print "\nInserting these names to the master list\n"
# for schn in dE:
# 	print schn
# 	cursor.execute(
#             		"""INSERT INTO masterschoollist (school_name)
#             		VALUES (%s);""",
#             		(schn,))

# # measure_file_reader = get_reader(filepath)

# print "\nInserting these names and measures into respective year tables\n"
# with open(filepath) as source:
# 	sreader = csv.DictReader(source)
# 	table_string_format = "INSERT INTO " + table_name + "(school_name,school_type) "
# 	# values = map(lambda x: pluck(['LA number', 'institution name', 'institution type'], x), sreader)
# 	for value in sreader:
# 		if value['SCHNAME'] != "":
# 			print(value['URN'],value['SCHNAME'])
# 			cursor.execute(table_string_format + 
#             	"""VALUES (%s,%s);""",
#             	(value['SCHNAME'],value['NFTYPE']))

conn.commit()
cursor.close()
conn.close()








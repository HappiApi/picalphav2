from connectDB import *

# Use existing_names to access all school names in master table

existing_names = []

cursor.execute("""SELECT school_name FROM masterschoollist;""")

# temp is a list of tuples in the form ('NAME',)
temp = cursor.fetchall()

for tup in temp:
	existing_names.append(tup[0])



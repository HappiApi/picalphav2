import csv

schoolName_columnNames = ['institution name', 'SchoolName', 'SCHNAME','School name']
schoolType_columnNames = []

def get_reader(file_name,mode='rb'):
	try:
		file_object = open(file_name,mode)
	except:
		print "Failed to load file"
		raise SystemExit

	file_reader = csv.DictReader(file_object)
	return file_reader

def get_schoolNames(file_reader,column_name):
	schoolName_list = []
	for record in file_reader:
		if record[column_name]:
			schoolName_list.append(record[column_name])
	return schoolName_list

# def get_measure(file_reader,measure_column_name,school_column_name):
	

def find_columnName(file_reader,schoolName_columnNames):
	column_name = ""
	for schoolName_columnName in schoolName_columnNames:
			try:
				for fieldname in file_reader.fieldnames:
					if schoolName_columnName == fieldname:
							column_name = schoolName_columnName
							print "School Column is named " + schoolName_columnName
							return column_name
			except TypeError:
				print "Field names are empty"
				raise SystemExit
				
			print "School Column is not named " + schoolName_columnName

# For each new name check if already exist, if not print them
def doesntExist(new_names,existing_names):
	dE = []
	for newname in new_names:
		if not(newname in existing_names):
			dE.append(newname)
	return dE

# For each existing name check if in new names, if not print them
def droppedNames(existing_names,new_names):
	dN = []
	for existingname in existing_names:
		if not(existingname in new_names):
			dN.append(existingname)
	return dN


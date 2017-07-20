import sqlite3

connection = sqlite3.connect('pathways.db')

# Erase all data from the three tables
connection.execute('DELETE FROM path_enzyme')
connection.execute('DELETE FROM path')
connection.execute('DELETE FROM enzyme')

# Save the deletions
connection.commit()


import csv

# Read the pathways from the file from module 3
f = open('metabolic_pathways.csv')
paths = csv.reader(f, delimiter=',')
next(paths) 

# For each pathway, insert its information into the database
for path in paths:
	# Extract the pathway information from the `path` variable
	path_id = path[0]
	path_name = path[1]
	path_class = path[2]
	
	# Insert into the database
	# Notice that we create a generic SQL command using the `?` notation
	# and give the parameters of the command as a tuple
	connection.execute('''
		INSERT INTO path (id, name, class)
		VALUES (?, ?, ?)
	''', (path_id, path_name, path_class))

# Close the file
f.close()

# Save the changes
connection.commit()

# Now do the same for the enzymes
f = open('sequences.csv')
enzymes = csv.reader(f, delimiter=',')

enzymes_inserted = [] # Keep a list of the enzymes already inserted

for enzyme in enzymes:
	enzyme_id = enzyme[0]
	enzyme_sequence = enzyme[1]
	
	# Check to see if the enzyme has been added before
	if enzyme_id not in enzymes_inserted:
		connection.execute('''
			INSERT INTO enzyme (id, sequence)
			VALUES (?, ?)
		''', (enzyme_id, enzyme_sequence))
		
		# Add this enzyme to the list of enzymes already inserted
		enzymes_inserted.append(enzyme_id)

# Close the file
f.close()

# Save the changes
connection.commit()

# Which file do we need to read in order to relate pathways with enzymes?
f = open('metabolic_pathways.csv')

paths = csv.reader(f, delimiter=',')
next(paths)

for path in paths:
	path_id = path[0]
	enzyme_list = path[3].split('|')
	
	# For each enzyme, we need to add one line to the `path_enzyme` table
	for enzyme_id in enzyme_list:
		connection.execute('''
			INSERT INTO path_enzyme (path_id, enzyme_id)
			VALUES (?, ?)
		''', (path_id, enzyme_id))

f.close()
connection.commit()




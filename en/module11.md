# Module 11 -- Access a database {#module11}

## Objectives:
- Insert data from CSV file into the database
- Query the database and save it to a CSV file

## Input:
- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - created in module 2
- File: [sequences.csv](files/sequences.csv)
    - created in module 6
- File: [pathways.db](files/pathways.db)
    - created in module 9

## Output:
- File: `selected_paths.csv`

## Steps:

1. Open your Personal Area on your computer and create a folder named module11.
Save the three input files in the previous folder. Open the application `IDLE (Python 3...)`.


2. Create a new Python script that opens the database `pathways.db` created in the previous module with Python and removes the entries in the tables.
```python
import sqlite3

connection = sqlite3.connect('pathways.db')

# Erase all data from the three tables
connection.execute('DELETE FROM path_enzyme')
connection.execute('DELETE FROM path')
connection.execute('DELETE FROM enzyme')

# Save the deletions
connection.commit()
```
Save the file as `module11.py` in the previous folder, and click on `Run` and then `Run Module`.

3. Add the following code to the previous script, which will read the data from each pathway and add them to the database:
```python
	import csv

	# Read the pathways from the file from module 3
	f = open('metabolic_pathways.csv')
	paths = csv.reader(f, delimiter='???')
	next(paths) 
	
	# For each pathway, insert its information into the database
	for path in paths:
		# Extract the pathway information from the `path` variable
		path_id = path[0]
		path_name = path[???]
		path_class = path[???]
		
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
```
Again, run the code, and open the application [DB Browser for SQLite](http://sqlitebrowser.org/),
and check the results on the database `pathways.db`. 

**Note**: Replace all the green question mark place-holders (`???`) with appropriate Python or SQL code.


4. Add the following code to the previous script, which will read the data from each enzyme and add them to the database:
```python
	# Now do the same for the enzymes
	f = open('sequences.csv')
	enzymes = csv.reader(f, delimiter='???')

	enzymes_inserted = [] # Keep a list of the enzymes already inserted

	for enzyme in enzymes:
		enzyme_id = enzyme[???]
		enzyme_sequence = enzyme[???]
		
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
```
Again, run the code, and check the database.

5. Add the following code to the previous script, which will insert into the database the information that will allow us to associate pathways with enzymes:
```python
	# Which file do we need to read in order to relate pathways with enzymes?
	f = open('???')

	paths =  csv.reader(f, delimiter='???')
	next(paths) 

	for path in paths:
		path_id = path[0]
		enzyme_list = path[3].split('???')
		
		# For each enzyme, we need to add one line to the `path_enzyme` table
		for enzyme_id in enzyme_list:
			connection.execute('''
				INSERT INTO path_enzyme (path_id, enzyme_id)
				VALUES (?, ?)
			''', (path_id, enzyme_id))

	f.close()
	connection.commit()
```

6. Create a new Python script that opens the database `pathways.db` and executes the SQL query that associates the enzyme sequences with the name of each pathway created in the previous module.

```python
	import sqlite3

	connection = sqlite3.connect('pathways.db')

	rows = connection.execute('''
		SELECT path.id, path.name
		FROM path, enzyme, path_enzyme
		WHERE path.id = path_enzyme.path_id
		AND enzyme.id = path_enzyme.enzyme_id
		AND enzyme.sequence LIKE "%EA%"
		GROUP BY path_id
		HAVING COUNT(enzyme_id) >= ???
		''')

	# For each selected pathway, print the id and the name of the pathway
	for row in rows:
		path_id = row[???]
		path_name = row[???]
		print ('Path ' + path_id + ' is named "' + path_name + '"')
```

Again, run the code, and observe the output.

7. Change the code above to save the enzyme identifiers and sequences to a file named `selected_paths.csv` instead of printing them to the screen.
Refer to module 7, step 4 to refresh your memory on how to write a CSV file.

Again, run the code, and open the `selected_paths.csv` in Excel or in a text editor.
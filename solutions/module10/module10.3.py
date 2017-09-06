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


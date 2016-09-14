#!/usr/bin/env python

import sqlite3
import csv

connection = sqlite3.connect('pathways.db')

# Erase all data from the three tables
connection.execute('DELETE FROM path_enzyme')
connection.execute('DELETE FROM paths')
connection.execute('DELETE FROM enzymes')

# Read the pathways from the file from module 3
f = open('selected2.csv')
paths = csv.reader(f, delimiter=',')

# For each pathway, insert its information into the database
for path in paths:
    # Extract the pathway information from the `path` variable
    path_id = path[0]
    path_name = path[1]
    path_class = path[2]
    
    # Insert into the database using the `?` notation
    connection.execute('''
        INSERT INTO paths (id, name, class)
        VALUES (?, ?, ?)
    ''', (path_id, path_name, path_class))


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
            INSERT INTO enzymes (id, sequence)
            VALUES (?, ?)
        ''', (enzyme_id, enzyme_sequence))
        
        # Add this enzyme to the list of enzymes already inserted
        enzymes_inserted.append(enzyme_id)

# Which file do we need to read in order to relate pathways with enzymes?
f = open('selected2.csv')
paths =  csv.reader(f, delimiter=',')

for path in paths:
    path_id = path[0]
    enzyme_list = path[3].split('|')
    
    # For each enzyme, we need to add one line to the `path_enzyme` table
    for enzyme_id in enzyme_list:
        connection.execute('''
            INSERT INTO path_enzyme (path_id, enzyme_id)
            VALUES (?, ?)
        ''', (path_id, enzyme_id))

# Save the changes
connection.commit()

# Let's open file `results_1.csv` in write mode
f = open('results_1.csv', 'w')
w = csv.writer(f, delimiter=???)

rows = connection.execute('SELECT id, name FROM enzymes')

# For each selected pathway, save it to the file
for row in rows:
    w.writerow(row)


f = open('results_2.csv', 'w')
w = csv.writer(f, delimiter=???)

rows = connection.execute('SELECT id FROM enzymes WHERE id LIKE "Q%"')
for row in rows:
    w.writerow(row)


f = open('results_3.csv', 'w')
w = csv.writer(f, delimiter=???)

rows = connection.execute(
    'SELECT paths.name, enzymes.sequence '
    'FROM paths, enzymes, path_enzyme '
    'WHERE paths.id = path_enzyme.path_id '
    '  AND enzymes.id = path_enzyme.enzyme_id')
for row in rows:
    w.writerow(row)


f = open('results_4.csv', 'w')
w = csv.writer(f, delimiter=???)

rows = connection.execute(
    'SELECT paths.id, paths.name '
    'FROM paths, path_enzymes '
    'GROUP BY path_id HAVING COUNT(*) >= 15')
for row in rows:
    w.writerow(row)

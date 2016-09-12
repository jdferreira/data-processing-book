# Module 7 -- Inserting data from CSV {#module7}

## Objectives:
- Copy data from CSV into the database
- Query the database with complex selection criteria

## Input:
- File [selected2.csv](files/selected2.csv) from module 3
- File [sequences.csv](files/sequences.csv) from module 3
- File [pathways.db](files/pathways.db) from module 6

## Output:
- File: `pathways.db` with the complete database
- File: `results_1.csv`
- File: `results_2.csv`
- File: `results_3.csv`

## Steps:

1. Create a new Python script `module7.py` that opens the database `pathways.db` created in the previous module with Python and removes the entries in the tables.
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

2. The following commands read the pathway data from our files from previous modules and add them to the database.
Append this code to the script:
```python
    import csv
    
    # Read the pathways from the file from module 3
    f = open('selected2.csv')
    paths = csv.reader(f, delimiter=???)
    
    # For each pathway, insert its information into the database
    for path in paths:
        # Extract the pathway information from the `path` variable
        path_id = path[0]
        path_name = ???
        path_class = ???
        
        # Insert into the database using the `?` notation
        connection.execute('''
            INSERT INTO path (id, name, class)
            VALUES (?, ?, ?)
        ''', (path_id, path_name, path_class))
        
    # Save the changes
    connection.commit()
```

3. We will do the same thing for the enzymes:
```python
    # Now do the same for the enzymes
    f = open('sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    enzymes_inserted = [] # Keep a list of the enzymes already inserted
    
    for enzyme in enzymes:
        enzyme_id = enzyme[0]
        enzyme_sequence = ???
        
        # Check to see if the enzyme has been added before
        if enzyme_id not in enzymes_inserted:
            connection.execute('''
                INSERT INTO enzyme (id, sequence)
                VALUES (?, ?)
            ''', (enzyme_id, enzyme_seq))
            
            # Add this enzyme to the list of enzymes already inserted
            enzymes_inserted.append(enzyme_id)
    
    # Save the changes
    connection.commit()
```

4. And now it is time to insert into the database the information that will allow us to relate pathways with enzymes:
```python
    # Which file do we need to read in order to relate pathways with enzymes?
    f = open(???)
    
    paths =  csv.reader(f, delimiter=???)
    
    for path in paths:
        path_id = path[0]
        enzyme_list = path[3].split('|')
        
        # For each enzyme, we need to add one line to the `path_enzyme` table
        for enzyme_id in enzyme_list:
            connection.execute('''
                INSERT INTO path_enzyme (path_id, enzyme_id)
                VALUES (?, ?)
            ''', (path_id, enzyme_id))
    
    connection.commit()
```

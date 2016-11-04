# Module 7 -- Inserting data from CSV {#module7}

## Objectives:
- Copy data from CSV into the database
- Query the database with complex selection criteria

## Input:
- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - created in module 1
- File: [all_sequences.csv](files/all_sequences.csv)
    - similar to `sequences.csv` from module 3 but will the sequence of all the enzymes.
    See question 2 in the **After the class** section of that module.
- File: [pathways.db](files/pathways.db)
    - created in module 6

## Output:
- File: `results_1.csv`
- File: `results_2.csv`
- File: `results_3.csv`
- File: `results_4.csv`

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

2. Add the following code to the script, which will read the data from each pathway and add them to the database.
```python
    import csv
    
    # Read the pathways from the file from module 3
    f = open('metabolic_pathways.csv')
    paths = csv.reader(f, delimiter=???)
    
    # For each pathway, insert its information into the database
    for path in paths:
        # Extract the pathway information from the `path` variable
        path_id = path[0]
        path_name = ???
        path_class = ???
        
        # Insert into the database
        # Notice that we create a generic SQL command using the `?` notation
        # and give the parameters of the command as a tuple
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
    f = open('all_sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    enzymes_inserted = [] # Keep a list of the enzymes already inserted
    
    for enzyme in enzymes:
        enzyme_id = ???
        enzyme_sequence = ???
        
        # Check to see if the enzyme has been added before
        if enzyme_id not in enzymes_inserted:
            connection.execute('''
                INSERT INTO enzyme (id, sequence)
                VALUES (?, ?)
            ''', (enzyme_id, enzyme_sequence))
            
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

5. Let's use an SQL query to print the id and name of the pathways:
```python
    rows = connection.execute('SELECT ??? FROM ???')
    
    # For each selected pathway, print the id and the name of the pathway
    for row in rows:
        path_id = row[???]
        path_name = row[???]
        
        print 'Path ' + path_id + ' is named "' + path_name + '"'
```

6. Check that the output is
```text
    Path hsa00730 is named "Thiamine metabolism"
    Path hsa04122 is named "Sulfur relay system"
```

7. The code above prints the results to the screen.
Now we want to save them into the CSV file `results_1.csv`.
Replace the code from step 5 with this:
```python
    # Let's open file `results_1.csv` in write mode
    f = open(???, ???)
    w = csv.writer(f, delimiter=???)
    
    rows = connection.execute('SELECT ??? FROM ???')
    
    # For each selected pathway, save it to the file
    for row in rows:
        w.writerow(row)
    
    f.close()
```

8. Let's now select all the enzymes whose id starts with Q and save them to the file `results_2.csv`.
The code recipe is the same, changing only the file name and the query.
You can use the following query, changing where necessary:
```sql
    SELECT ??? FROM enzyme WHERE ??? LIKE "Q%"
```

9. Now we will cross the data in the tables.
Duplicate and adapt the same code from the previous step, using the following command SQL to select the enzyme sequences of each pathway, and save the results to `results_3.csv`:
```sql
    SELECT path.name, enzyme.???
    FROM path, enzyme, path_enzyme
    WHERE path.id = path_enzyme.path_id
      AND enzyme.id = path_enzyme.enzyme_id
```

10. SQL allows the use of complex queries.
Use this query to save the id and name of the pathways associated with at least 15 enzymes.
Save this to `results_4.csv`.
```sql
    SELECT path.id, path.name
    FROM path, path_enzyme
    WHERE path.id = path_enzyme.path_id
    GROUP BY path_id HAVING COUNT(*) >= 300
```

## After the class:

1. Determine the reason for using the list `enzymes_inserted` in step 3.<br>
**Hint**: try to remove the list from the script and observe that the code fails with a `constraint failed` exception.

2. Many of the steps in this module suffer from code repetition.
    
    a. Create a function `run_sql` that accepts two arguments: an SQL command and a file name.
    
    b. Implement this function so that it runs the SQL command and saves the results in a CSV file.
    
    c. Change today's code so that it uses the function, instead of repeating code<br>
    **Hint**: The steps 6 to 9 will each simply call the function once.

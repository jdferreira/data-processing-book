# Module 6 -- Create an SQL database {#module6}

## Objectives:
- Design a simple database schema to store information on the pathways
- Use foreign keys

## Input:
- None

## Output:
- Database file: `pathways.db`

## Steps:

1. We will start by creating an empty database in the file `pathways.db` which will contain three tables.
First create a new Python script `module6.py` with the following code:
```python
    # `sqlite3` is a package that can be used to create a file containing
    # a relational database. We use this package to create the database,
    # insert data in it and query the data.
    
    import sqlite3
    
    # To access a database, we need to connect to it. If the file does not
    # exist, one will be created
    connection = sqlite3.connect('pathways.db')
```

2. Now that we have an empty database, let's add the tables that we need to store the metabolic pathway data.
```python
    # This table will contain data about the pathways
    connection.execute('''
        CREATE TABLE path (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            class VARCHAR(255) NOT NULL
        )
    ''')
    
    # This table will contain data about the enzymes
    connection.execute('''
        CREATE TABLE enzyme (
            id VARCHAR(255) PRIMARY KEY,
            sequence TEXT NOT NULL
        )
    ''')
    
    # This table will associate each pathway with its enzymes
    connection.execute('''
        CREATE TABLE path_enzyme (
            path_id VARCHAR(255),
            enzyme_id VARCHAR(255),
            PRIMARY KEY (path_id, enzyme_id),
            FOREIGN KEY (path_id) REFERENCES path (id),
            FOREIGN KEY (enzyme_id) REFERENCES enzyme (id)
        )
    ''')
```

3. Now, we insert some data in these three tables.
We will only insert one pathway and two enzymes of that pathway.
If you need, consult the files from the previous modules to find the name, enzymes and sequences of the pathway `hsa00730`.
```python
    connection.execute('''
        INSERT INTO path (id, name, class)
        VALUES ('hsa00730', '???', '???')
    ''')
    
    connection.execute('''
        INSERT INTO enzyme (id, sequence)
        VALUES ('Q53FP3','???')
    ''')
    
    connection.execute('''
        INSERT INTO enzyme (id, sequence)
        VALUES ('???','???')
    ''')
    
    connection.execute('''
        INSERT INTO path_enzyme (path_id, enzyme_id)
        VALUES ('hsa00730','???')
    ''')
    
    connection.execute('''
        INSERT INTO path_enzyme (path_id, enzyme_id)
        VALUES ('???','???')
    ''')
    
    # Ensure that the data is saved
    connection.commit()
```

4. Finally, let's just make sure that the tables contain some data.
For that, we will select the sequences of each pathway.
```python
    rows = connection.execute('SELECT id, sequence FROM enzymes')
    for row in rows:
        enzyme_id = row[0]
        enzyme_sequence = row[1]
        
        print enzyme_id + ' starts with ' + enzyme_sequence[:5]
```

5. Ensure that the output on the screen is:
```text
    Q53FP3 starts with MLLRA
    Q9Y697 starts with MLLRA
```

6. Make sure you keep a copy of the `pathways.db` file to yourself, so that you can use it in the next module.
For example, send it to you by email or upload it to Dropbox.

## After the class:

1. Explain why the primary key of the table `path_enzyme` has two atributes.

2. Modify the database schema so that the database can store the name of the enzymes and also their position within the pathway (a whole number).

3. Change the code of step 4 so that you can also verify the contents of the  tables `paths` and `path_enzyme`.


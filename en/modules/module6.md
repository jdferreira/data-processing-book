# Module 6 -- Create an SQL database {#module6}

## Part I: A small example to get you going

### Objectives:
- Create a database in SQLite using Python
- Insert and query data in the database

### Input:
- None

### Output:
- Database file: `example.db`


### Steps:
1. First, create an empty database file using Python.
You can name this script <nobr>`example.py`.</nobr>
```python
    # `sqlite3` is a package that can be used to create a file containing
    # a relational database. We use this package to create the database,
    # insert data in it and query the data.
    
    import sqlite3
    
    # To access a database, we need to connect to it. If the file does not
    # exist, one will be created
    connection = sqlite3.connect('example.db')
```

2. Now that we have an empty database, let's add some tables and some data.
Add the following to your script:
```python
    # We can now emit SQL commands to the opened database
    
    # First create a table to store student information
    connection.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    
    # Then add information to that table
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (1, 'Alice', 20)
    ''')
    
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (2, 'Brock', 21)
    ''')
    
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (3, 'Chuck', 19)
    ''')
    
    # You can also insert data that is stored in variables
    student_id = 4
    student_name = 'Doris'
    student_age = 19
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (?, ?, ?)
    ''', (student_id, student_name, student_age))
    
    # Ensure that the data is saved
    connection.commit()
```

3. Finally make sure that the database actually contains the information you inserted:
```python
    # We can also emit SELECT commands which will return data back to Python
    
    rows = connection.execute('SELECT id, name, age FROM students')
    
    for row in rows:
        student_id = row[0]
        student_name = row[1]
        student_age = row[2]
        
        msg = student_name + ' is ' + str(student_age) + ' years old'
        msg = msg + ' and has id #' + str(student_id)
        
        print msg
```

4. Make sure that you get the following output:
```text
    Alice is 20 years old and has id #1
    Brock is 21 years old and has id #2
    Chuck is 19 years old and has id #3
    Doris is 19 years old and has id #4
```


## Part II: Now with real data

## Objectives:
- Design a simple database schema to store information on the pathways
- Create the database in SQLite
- Use foreign keys
- Insert data from the CSV file
- Query the data

## Input:
- None

## Output:
- File: `pathways.db`

## Steps:

1. Now that you know how to create a database and create its tables, we will make a database called `pathways.db` with three tables.
First create a new Python script `module6.py` with the following
```python
    import sqlite3
    
    connection = sqlite3.connect('pathways.db')
    
    # Let's create the three tables.
    
    # This contains information about the pathway
    connection.execute('''
        CREATE TABLE path (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            class VARCHAR(255) NOT NULL
        )
    ''')
    
    # This contains information about the enzymes
    connection.execute('''
        CREATE TABLE enzyme (
            id VARCHAR(255) PRIMARY KEY,
            sequence TEXT NOT NULL
        )
    ''')
    
    # This associates each pathway with its enzymes
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

2. Now, we insert some data in these three tables.
We will only insert one pathway and two enzymes of that pathway.
If you need, consult the files from the previous modules to find the name, enzymes and sequences of the pathway `hsa00730`.
```python
    connection.execute('''
        INSERT INTO path (id, name, class)
        VALUES ('hsa00730', '???', '???');
    ''')
    
    connection.execute('''
        INSERT INTO enzyme (id, sequence)
        VALUES ('Q53FP3','???');
    ''')
    
    connection.execute('''
        INSERT INTO enzyme (id, sequence)
        VALUES ('???','???');
    ''')
    
    connection.execute('''
        INSERT INTO path_enzyme (path_id, enzyme_id)
        VALUES ('hsa00730','???');
    ''')
    
    connection.execute('''
        INSERT INTO path_enzyme (path_id, enzyme_id)
        VALUES ('???','???');
    ''')
    
    # Ensure that the data is saved
    connection.commit()
```

3. Finally, let's just make sure that the tables contain some data.
For that, we will select the sequences of each table
```python
    rows = connection.execute('SELECT id, sequence FROM enzymes')
    for row in rows:
        enzyme_id = row[0]
        enzyme_sequence = row[1]
        
        print enzyme_id + ' starts with ' + enzyme_sequence[:5]
```
This should produce the oputput
```text
    Q53FP3 starts with MLLRA
    Q9Y697 starts with MLLRA
```

7. Make sure you keep a copy of the `pathways.db` file to yourself, so that you can use it in the next module.
For example, send it to you by email or upload it to Dropbox.


## After the class:
1. Verify that the primray key of the table `path_enzyme` has two atributes, and explain why that happens.

2. Modify the database schema so that the database can store the name of the enzymes and also their position within the pathway (a whole number).

3. Change the code of step 3 so that you can verify the contents of the other two tables.


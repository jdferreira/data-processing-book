#!/usr/bin/env python

# Part I

import sqlite3

connection = sqlite3.connect('example.db')

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

rows = connection.execute('SELECT * FROM students')
for row in rows:
    student_id = row[0]
    student_name = row[1]
    student_age = row[2]
    
    msg = student_name + ' is ' + str(student_age) + ' years old'
    msg = msg + ' and has id #' + str(student_id)
    
    print msg

connection.commit()
connection.close()

# Part II

import sqlite3

connection = sqlite3.connect('pathways.db')

# Let's create the three tables.

# This contains information about the pathway
connection.execute('''
    CREATE TABLE paths (
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        class VARCHAR(255) NOT NULL
    )
''')

# This contains information about the enzymes
connection.execute('''
    CREATE TABLE enzymes (
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

connection.execute('''
    INSERT INTO paths (id, name, class)
    VALUES ('hsa00730', 'Thiamine metabolism', 'Metabolism of cofactors and vitamins');
''')

connection.execute('''
    INSERT INTO enzymes (id, sequence)
    VALUES ('Q53FP3', 'MLLRAAWRRAAVAVTAAPGPKPAAPTRGLRLRVGDRAPQSAVPADTAAASEVGPVLRPLYMDVQATTPLDPRVLDAMLPYLINYYGNPHSRTHAYGWESEAAMERARQQVASLIGADPREIIFTSGATESNNIAIKGVARFYRSRKKHLITTQTEHKCVLDSCRSLEAEGFQVTYLPVQKSGIIDLKELEAAIQPDTSLVSVMTVNNEIGVKQPIAEIGRICSSRKVYFHTDAAQAVGKIPLDVNDMKIDLMSISGHKIYGPKGVGAIYIRRRPRVRVEALQSGGGQERGMRSGTVPTPLVVGLGAACEVAQQEMEYDHKRISKLSERLIQNIMKSLPDVVMNGDPKHHYPGCINLSFAYVEGESLLMALKDVALSSGSACTSASLEPSYVLRAIGTDEDLAHSSIRFGIGRFTTEEEVDYTVEKCIQHVKRLREMSPLWEMVQDGIDLKSIKWTQH');
''')

connection.execute('''
    INSERT INTO enzymes (id, sequence)
    VALUES ('Q9Y697', 'MLLRAAWRRAAVAVTAAPGPKPAAPTRGLRLRVGDRAPQSAVPADTAAAPEVGPVLRPLYMDVQATTPLDPRVLDAMLPYLINYYGNPHSRTHAYGWESEAAMERARQQVASLIGADPREIIFTSGATESNNIAIKGVARFYRSRKKHLITTQTEHKCVLDSCRSLEAEGFQVTYLPVQKSGIIDLKELEAAIQPDTSLVSVMTVNNEIGVKQPIAEIGRICSSRKVYFHTDAAQAVGKIPLDVNDMKIDLMSISGHKIYGPKGVGAIYIRRRPRVRVEALQSGGGQERGMRSGTVPTPLVVGLGAACEVAQQEMEYDHKRISKLSERLIQNIMKSLPDVVMNGDPKHHYPGCINLSFAYVEGESLLMALKDVALSSGSACTSASLEPSYVLRAIGTDEDLAHSSIRFGIGRFTTEEEVDYTVEKCIQHVKRLREMSPLWEMVQDGIDLKSIKWTQH');
''')

connection.execute('''
    INSERT INTO path_enzyme (path_id, enzyme_id)
    VALUES ('hsa00730', 'Q53FP3');
''')

connection.execute('''
    INSERT INTO path_enzyme (path_id, enzyme_id)
    VALUES ('hsa00730', 'Q9Y697');
''')

rows = connection.execute('SELECT id, sequence FROM enzymes')
for row in rows:
    enzyme_id = row[0]
    enzyme_sequence = row[1]
    
    print enzyme_id + ' starts with ' + enzyme_sequence[:5]

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect('pathways.db')

rows = connection.execute('''
	SELECT path.id, path.name
        FROM path, enzyme, path_enzyme
        WHERE path.id = path_enzyme.path_id
        AND enzyme.id = path_enzyme.enzyme_id
	AND enzyme.sequence LIKE "%EA%"
        GROUP BY path_id
	HAVING COUNT(enzyme_id) >= 2
	''')

# For each selected pathway, print the id and the name of the pathway
for row in rows:
    path_id = row[0]
    path_name = row[1]
    print ('Path ' + path_id + ' is named "' + path_name + '"')

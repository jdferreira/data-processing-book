import sqlite3

connection = sqlite3.connect('pathways.db')

# Erase all data from the three tables
connection.execute('DELETE FROM path_enzyme')
connection.execute('DELETE FROM path')
connection.execute('DELETE FROM enzyme')

# Save the deletions
connection.commit()

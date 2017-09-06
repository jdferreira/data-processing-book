import csv

f = open('metabolic_pathways.csv') # Open the file

paths = csv.reader(f, delimiter=',') # Create a CSV reader object

# We need to ignore the first row, which contains the headers of the
# columns, called the "metadata". We do it by calling the `next`
# function, which advances to the next line of the file
next(paths)

for path in paths: # For each pathway ...
    path_id = path[0] # Select the column for the ID
    path_name = path[1] # Select the column for the name

    if path_id == 'hsa03030':
        print(path_name) # ... print its name

# Close the file
f.close()

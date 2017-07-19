import csv
 
f = open('metabolic_pathways.csv') # Open the file

paths = csv.reader(f, delimiter=',') # Create a CSV reader object

next(paths) # ignore the first row, which contains the headers of the columns called "metadata" 
    
for path in paths: # For each pathway ...
    path_id = path[0]  # Select the column for the ID
    path_name = path[1]  # Select the column for the name
    
    if path_id == 'hsa03030':
       print(path_name)      # ... print its name
    
# Close the file
f.close()

import csv
        
f = open('metabolic_pathways.csv') # Open the file
        
paths = csv.reader(f, delimiter=',') # Create a CSV reader object
        
for path in paths: # For each pathway ...
    print(path[0])      # ... print its name
        
# Close the file
f.close()

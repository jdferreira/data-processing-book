import csv

f = open('metabolic_pathways.csv') # Open the file

paths = csv.reader(f, delimiter=',') # Create a CSV reader object

# We must ignore the first row, which contains the headers of the
# columns, called the "metadata" of our data. We do it by calling
# the `next` function which advances to the next line of the file
next(paths)

for path in paths:  # For each pathway ...
    print(path[1])  # ... print its name

# Close the file
f.close()

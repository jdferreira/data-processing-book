#!/usr/bin/env python

import csv

# Read the CSV file
f = open('sequences.csv')
enzymes = csv.reader(f, delimiter=',')

# Create an empty dictionary that we will populate as we read the CSV
# file
dict_sequences = {}

# For each of the enzymes in the file, associate the enzyme with its
# sequence
for enzyme in enzymes:
    enzyme_id = enzyme[0] # The ID of this enzyme
    seq = enzyme[1]       # The aminoacid sequence of this enzyme
    dict_sequences[enzyme_id] = seq


# Read the CSV file
f = open('selected2.csv')
paths = csv.reader(f, delimiter=',')

# Create an empty dictionary that we will populate as we read the CSV
# file
dict_paths = {}

# For each pathway in that file:
# - extract the list of enzymes in the pathway
# - associate the pathway with this list of enzymes
for path in paths:
    path_id = path[0] # The ID of the pathways
    enzymes = path[3] # The field of the enzymes
    
    # Break that information into a list
    enzyme_list = str.split(enzymes, '|')
    
    # Associate the pathway ID with the corresponding list of enzymes
    dict_paths[path_id] = enzyme_list

# Open a file to save the output
f = open('paths_enzymes.csv', 'bw')
w = csv.writer(f, delimiter=',')

# For each pathway and each enzyme that it contains
for path_id in dict_paths :
    # Let's print some debugging information
    print 'Processing pathway with ID ' + path_id
    
    # Retrieve the list of enzymes associated with this pathway
    enzyme_list = dict_paths[path_id]
    
    # Now that we have the list of enzymes, associate the pathway with each
    # aminoacid sequence
    for enzyme_id in enzyme_list:
        # Some more debugging information
        print '  enzyme = ' + enzyme_id
        
        # Retrieve the sequence associated with this enzyme
        seq = dict_sequences[enzyme_id]
        
        # Write this row to the CSV file
        w.writerow([path_id, seq])

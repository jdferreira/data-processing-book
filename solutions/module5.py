#!/usr/bin/env python

import csv
import re

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


# Open the file to save the output
f = open('relevant_sequences_1.csv', 'wb')
w = csv.writer(f, delimiter=',')

# Define here your regular expression
reg_expr = 'AAA'
# reg_expr = r'^[AFGILMPVW]{5}'  # For relevant_sequences_2
# reg_expr = r'M.[SP]'           # For relevant_sequences_3

# For each enzyme, retrieve their sequence and determine whether
# the sequence matches three consecutive alanines
for enzyme in dict_sequences:
    # Retrieve the aminoacid sequence
    seq = dict_sequences[enzyme]
    
    # Determine whether the sequence matches the pattern; if it does,
    # save the enzyme identifier and sequence
    if re.search(reg_expr, seq):
        w.writerow([enzyme, seq])

f.close()

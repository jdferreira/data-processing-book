#!/usr/bin/env python

import csv
import urllib # This module contains functions to read URLs

def get_sequence(ID):
    # Establish the URL to open
    url = 'http://www.uniprot.org/uniprot/' + ID + '.fasta'
    
    # Open the URL
    f = urllib.urlopen(url)
    
    # Read all the lines into a list
    lines = f.readlines()
    
    # Ignore the first line, which contains metadata
    del lines[0]
    
    # Join all the remaining lines into a single string
    sequence = str.join("", lines)
    
    # Remove the line ends (the "enter" used to start the next line)
    # This line end is represented as \n
    sequence = str.replace(sequence, '\n', '')
    
    # Return the sequence
    return sequence


# sequence1 = get_sequence('P12345')
# sequence2 = get_sequence('P17735')
# sequence3 = get_sequence('Q9Y697')

# print "SEQUENCE 1:\n" + sequence1 + "\n"
# print "SEQUENCE 2:\n" + sequence2 + "\n"
# print "SEQUENCE 3:\n" + sequence3 + "\n"

# Open the output file from the previous module
f = open('selected2.csv')
paths = csv.reader(f, delimiter=',')

# Start with an empty list of enzymes
enzymes = []

# Then:
# - read the information of each pathway,
# - extract the list of enzymes of each pathway, and
# - append each enzyme to the list of enzymes
for path in paths:
    enzymes_field = path[3] # the field of the enzymes
    
    # Split the enzymes into a list, as in module 2
    enzymes_in_this_path = str.split(enzymes_field, '|')
    
    # Append each one into the master enzyme list
    for e in enzymes_in_this_path:
        enzymes.append(e)

f = open('sequences.csv', 'wb')
w = csv.writer(f, delimiter=',')

for e in enzymes:
    seq = get_sequence(e)
    w.writerow([e, seq])

f.close()

#!/usr/bin/env python

import csv


def filter1(path):
    path_id = path[0] # select the column for the ID
    
    if path_id == 'hsa04210': # replace with the ID we are searching for
        return True
    else:
        return False

def filter2(path):
    field = path[3] # select the column for the list of enzymes
    
    # break that information into a list
    enzyme_list = str.split(field, '|')
    
    # enzyme_list is now a list of strings, such as follows:
    # ['H9EC08', 'P03905', 'G9LG04', 'P03901']
    
    # Return True if our selected enzyme is in that list
    if 'Q9Y697' in enzyme_list:
        return True
    else:
        return False


# Open the original file and read all pathways
file_to_read = open('metabolic_pathways.csv')
paths = csv.reader(file_to_read, delimiter=',')

# Open the file where we will save the selection
file_to_write = open('selected2.csv', 'w')
w = csv.writer(file_to_write, delimiter=',')

for path in paths:
    if filter2(path):
        w.writerow(path)

# Close the file
file_to_write.close()

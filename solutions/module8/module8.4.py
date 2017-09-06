import csv
   
file_sequences = open('sequences.csv')
enzymes = csv.reader(file_sequences, delimiter=',')

# Dictionary that associates each enzyme with its sequence
enzyme_sequence = {}

for enzyme in enzymes: # For each pathway ...
    enzyme_id = enzyme[0] # Select the column for the enzyme identifier
    sequence = enzyme[1] # Select the column for the sequence

    # associate the enzyme with its sequence
    enzyme_sequence[enzyme_id] = sequence

# Print debugging information
print('Sequence of enzyme P18440: ' + enzyme_sequence['P18440'])

file_sequences.close()

# We import the `re` module to handle regular expressions
import re

# Define here your regular expression
reg_expr = r'^[AM]{3}'

# Uncomment the following line for step 4b
# reg_expr = r'MM.[SP]'

# For each enzyme, retrieve their sequence and determine whether
# the sequence matches three consecutive alanines
for enzyme_id, sequence in enzyme_sequence.items():
    # Determine whether the sequence matches the pattern
    if re.search(reg_expr, sequence):
        print ('The enzyme ' + enzyme_id + ' matches the expression ' + reg_expr)

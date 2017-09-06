import csv

file_sequences = open('sequences.csv')
enzymes = csv.reader(file_sequences, delimiter=',')

# Dictionary that associates each enzyme with its sequence
enzyme_sequence = {}

for enzyme in enzymes: # For each pathway ...
    enzyme_id = enzyme[0] # Select the column for the enzyme identifier
    sequence = enzyme[1] # Select the column for the sequence

    # Associate the enzyme with its sequence
    enzyme_sequence[enzyme_id] = sequence

# Print debugging information
print('Sequence of enzyme P18440: ' + enzyme_sequence['P18440'])

file_sequences.close()

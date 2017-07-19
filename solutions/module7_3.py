import csv
   
file_paths = open('selected2.csv')
paths = csv.reader(file_paths, delimiter=',')

# Dictionary that associates each pathway with its list of enzymes 
path_enzyme = {}
	
for path in paths: # For each pathway ...
    path_id = path[0] # Select the column for the path identifier
    enzymes = path[3] # Select the column for the list of enzymes
            
    # Break that information into a list
    enzyme_list = str.split(enzymes, '|')

    # associate the path with its enzymes
    path_enzyme[path_id] = enzyme_list

# Print debugging information
print('Enzymes of pathway hsa00232 :' + str(path_enzyme['hsa00232']))

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
print('Sequence of enzyme P18440 :' + enzyme_sequence['P18440'])

file_paths.close()
file_sequences.close()

# For each pathway
for path_id, enzyme_list in path_enzyme.items():
    print('Processing path: ' + path_id)

    # for each enzyme of that pathway 
    for enzyme_id in enzyme_list:
        # Some more debugging information
        print('Processing enzyme: ' + enzyme_id)
        
        # Retrieve the sequence associated with this enzyme
        sequence = enzyme_sequence[enzyme_id]

        # Print the sequence associated to the path being processed
        print(path_id + ', ' + sequence)
            

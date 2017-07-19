import urllib.request
import csv
 
file_to_read = open('selected2.csv')
paths = csv.reader(file_to_read, delimiter=',')
    
for path in paths: # For each pathway ...
    enzymes = path[3] # Select the column for the list of enzymes
        
    # Break that information into a list
    enzyme_list = str.split(enzymes, '|')

    for enzyme_id in enzyme_list:
    
        # Establish the URL to open
        url = 'http://www.uniprot.org/uniprot/' + enzyme_id + '.fasta'

        # Open the URL
        response = urllib.request.urlopen(url)

        # Read all the lines into a list
        data = str(response.read())
        lines = str.split(data,'\\n')

        # Ignore the first line, which contains metadata
        del lines[0]

        # Join all the remaining lines into a single string
        sequence = str.join("", lines)

        # Remove the line ends (the "enter" used to start the next line)
        sequence = str.replace(sequence, '\n', '')
        # Remove the ' character ath the end of the string
        sequence = sequence.strip("'")

        # Prints the sequence
        print("Sequence of pathway " + enzyme_id + ":\n" + sequence)

import urllib.request
import csv
 
file_to_read = open('selected2.csv')
paths = csv.reader(file_to_read, delimiter=',')

file_to_write = open('sequences.csv', 'w', newline='')
w = csv.writer(file_to_write, delimiter=',')

# List of enzymes which sequence was alread saved
enzymes_saved = []
    
for path in paths: # For each pathway ...
    enzymes = path[3] # Select the column for the list of enzymes
        
    # Break that information into a list
    enzyme_list = str.split(enzymes, '|')

    for enzyme_id in enzyme_list:

        # Check if the sequence of this enzyme was not already saved
        if enzyme_id not in enzymes_saved:
        
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

            # Writes the sequence to the file
            w.writerow([enzyme_id, sequence])

            # Add the enzyme to the list of saved enzymes
            enzymes_saved.append(enzyme_id)

file_to_read.close()
file_to_write.close()

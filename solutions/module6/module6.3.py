import urllib.request # This module contains functions to read URLs

# Establish the URL to open
url = 'http://www.uniprot.org/uniprot/' + 'P18440' + '.fasta'

# Open the URL
response = urllib.request.urlopen(url)

# Read all the lines into a list
data = response.read().decode('ascii')
lines = str.split(data, '\n')

# Ignore the first line, which contains metadata
del lines[0]

# Join all the remaining lines into a single string
sequence = str.join('', lines)

# Remove the line ends (the "enter" used to start the next line)
sequence = str.replace(sequence, '\n', '')

# Prints the sequence
print(sequence)

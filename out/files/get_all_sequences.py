import csv
import urllib.request

def get_sequence(ID):
    # Establish the URL to open
    url = 'http://www.uniprot.org/uniprot/' + ID + '.fasta'
    
    # Open the URL
    f = urllib.request.urlopen(url)
    
    # Read all the lines into a list
    lines = f.readlines()
    
    # Ignore the first line, which contains metadata
    del lines[0]
    
    # Join all the remaining lines into a single string
    sequence = b''.join(lines)
    
    # Remove the line ends (the "enter" used to start the next line)
    # This line end is represented as \n
    sequence = sequence.replace(b'\n', b'')
    
    # Return the sequence
    return sequence.decode('utf8')


try:
    with open('all_sequences.csv') as f:
        previous = list(csv.reader(f))
        done = {line[0] for line in previous}
except FileNotFoundError:
    previous = []
    done = set()

with open('metabolic_pathways.csv') as f:
    lines = list(csv.reader(f))
    enzymes = {i for line in lines for i in line[3].split('|') if i}
    enzymes.difference_update(done)

with open('all_sequences.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    
    for line in previous:
        w.writerow(line)
    
    for e in enzymes:
        print(e)
        
        try:
            seq = get_sequence(e)
        except Exception as ex:
            print('ERROR: ' + '*' * 10 + str(ex))
            seq = ''
        
        w.writerow([e, seq])

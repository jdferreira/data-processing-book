# Module 6 -- Web services {#module6}

## Objectives:
- Recognize the importance of external sources of data
- Use a web service through Python code
- Process information coming from a web service

## Input:
- File: [selected2.csv](files/selected2.csv)
	- created in the previous module

## Output:
- File: `sequences.csv`
	- containing the aminoacid sequences for each enzyme

## Steps:

1. Go to <http://www.uniprot.org/uniprot/P18440.fasta> and study the FASTA format.
Change the identifier in the link from `P18440` to another one and study its content and how it is different from the previous one.

2. Open your Personal Area on your computer and create a folder named module6.
Save the file `selected2.csv` given as input in the previous folder.
Open the application `IDLE (Python 3...)`.

3. Create a Python script that prints the sequence of a given protein.
The script will open the URL mentioned above, read the content on that URL, and extracts the aminoacid sequence, and joins all the lines so that only a single string is returned.
Click on `File`, then on `New File`, and write

	```python
	import urllib.request # This module contains functions to read URLs

	# Establish the URL to open
	url = 'http://www.uniprot.org/uniprot/' + 'P18440' + '.fasta'

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
	print(sequence)
	```

Save the file as `module5.py` in the previous folder, and click on `Run` and then `Run Module` and observe the output.
	
4. Modify the previous code so it prints the sequences of other enzymes. 
	
5. Modify the previous code to read the enzymes in the `selected2.csv` file and perform a lookup of their aminoacid sequences: 

	```python
	import urllib.request
	import csv
	 
	file_to_read = open('selected2.csv')
	paths = csv.reader(file_to_read, delimiter='???')
		
	for path in paths: # For each pathway ...
		enzymes = path[???] # Select the column for the list of enzymes
			
		# Break that information into a list
		enzyme_list = str.split(enzymes, '???')

		for enzyme_id in enzyme_list:
		
			# Establish the URL to open
			url = 'http://www.uniprot.org/uniprot/' + ??? + '.fasta'

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
	```

Again, run the code, observe the output.

**Note**: Replace all the green question mark place-holders (`???`) with appropriate Python code.

6. Modify the previous code to write the output  to a file named `sequences.csv`:

	```python
	import urllib.request
	import csv
	 
	file_to_read = open('selected2.csv')
	paths = csv.reader(file_to_read, delimiter='???')
	
	file_to_write = open('sequences.csv', 'w', newline='')
	w = csv.writer(file_to_write, delimiter=',')
		
	for path in paths: # For each pathway ...
		enzymes = path[???] # Select the column for the list of enzymes
			
		# Break that information into a list
		enzyme_list = str.split(enzymes, '???')

		for enzyme_id in enzyme_list:
		
			# Establish the URL to open
			url = 'http://www.uniprot.org/uniprot/' + ??? + '.fasta'

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
	
	file_to_read.close()
	file_to_write.close()
	```

Again, run the code, observe the output, and open the `sequences.csv` in Excel or in a text editor.
Observe in `sequences.csv` that some enzymes appear more than once, and try to explain why?	


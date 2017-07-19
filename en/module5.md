# Module 5 -- Filter data {#module5}

## Objectives:
- Transform a selection criterion into actual Python code
- Implement the selection process in Python
- Save the selected information on a new file

## Input:
- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
	- created in the previous module (without the headers)

## Output:
- File: `selected1.csv`
	* containing the data of the pathway `hsa03030`.
- File: `selected2.csv`
	* containing the data of the pathways where the enzyme P18440 participates.
- File: `selected3.csv`
	* containing the data of the pathways with more than 500 enzymes.

	
## Steps:

1. Open your Personal Area on your computer and create a folder named module5.

2. Save the file `metabolic_pathways.csv` given as input in the previous folder.

3. Open the application `IDLE (Python 3...)`
**Note**: do not open version 2 of Python 

4. Create a Python script that prints the name of the pathway with the identifier `hsa03030`:
Click on `File`, then on `New File`, and write

	```python
	import csv
	 
	f = open('metabolic_pathways.csv') # Open the file
  
	paths = csv.reader(f, delimiter='???') # Create a CSV reader object
	
	next(paths) # ignore the first row, which contains the headers of the columns called "metadata" 
		
	for path in paths: # For each pathway ...
		path_id = path[???]  # Select the column for the ID
		path_name = path[???]  # Select the column for the name
		
		if path_id == '???':
		   print(path_name)      # ... print its name
		
	# Close the file
	f.close()
	```

Save the file as `module5.py` in the previous folder, and click on `Run` and then `Run Module` and observe the output.
	
**Note**: Replace all the green question mark place-holders (`???`) with appropriate Python code.
	

5. Replace the previous code so the output is saved to a CSV file named `selected1.csv`.
	
	```python
	import csv
	 
	# Open the original file to read all pathways
	file_to_read = open('metabolic_pathways.csv')
	paths = csv.reader(file_to_read, delimiter='???')
	next(paths) 
	
	# Open the file to save the selection
	# The 'w' instructs Python that we want to write on this file
	# The newline='' avoids blank lines between each row
	file_to_write = open('selected1.csv', 'w', newline='')
	w = csv.writer(file_to_write, delimiter='???')
		
	for path in paths: # For each pathway ...
		path_id = path[???]  
		
		if path_id == '???':
		   print("the pathway " + path_id + " was written to the file")      
		   w.writerow(path)      # write the pathway to the file
	 
	# Close the files
	file_to_read.close()
	file_to_write.close()
	```

Again, run the code, observe the output, and open the `selected1.csv` in Excel or in a text editor.

6. Replace the previous code so it selects the pathways where the enzyme P18440 participates and saves to a CSV file named `selected2.csv`.
	
	```python
	import csv
	 
	# Open the original file to read all pathways
	file_to_read = open('metabolic_pathways.csv')
	paths = csv.reader(file_to_read, delimiter=???)
	next(paths) 
	
	# Open the file to save the selection
	# The 'w' instructs Python that we want to write on this file
	# The newline='' avoids blank lines between each row
	file_to_write = open('selected2.csv', 'w', newline='')
	w = csv.writer(file_to_write, delimiter='???')
		
	for path in paths: # For each pathway ...
		path_id = path[0]
		enzymes = path[???] # Select the column for the list of enzymes
			
		# Break that information into a list
		enzyme_list = str.split(enzymes, '???')
		
		# `enzyme_list` is now a list of strings, such as follows:
		# ['H9EC08', 'P03905', 'G9LG04', 'P03901']
		
		if '???' in enzyme_list: # Check if our selected enzyme is in that list
		   print("the pathway " + path_id + " was written to the file")      
		   w.writerow(path)      # write the pathway to the file
	 
	# Close the files
	file_to_read.close()
	file_to_write.close()
	```

Again, run the code, observe the output, and open the `selected2.csv` in Excel or in a text editor.

7. Replace the previous code so it selects pathways containing more than 500 enzymes.
Tip: use the built-in function `len`. The documentation for this function can be found in <https://docs.python.org/2/library/functions.html#len>







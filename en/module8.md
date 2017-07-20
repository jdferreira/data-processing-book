# Module 8 -- Regular expressions {#module8}

## Objectives:

- Develop regular expressions that represent several selection criteria
- Use the `re` Python module to create the regular expressions
- Search for aminoacid motives in the enzyme sequences

## Input:

- File: [sequences.csv](files/sequences.csv)
    - created in module 6

## Output:

- File: `relevant_sequences.csv`

## Steps:

1. Open your Personal Area on your computer and create a folder named `module8`.
Save the file `selected2.csv` given as input in the previous folder.
Open the application `IDLE (Python 3...)`.

2. Like in the previous module, create a Python script that creates a dictionary that associates the enzymes with their sequence by reading the contents of file `sequences.csv`.
    ```python
    import csv
    
    file_sequences = open('sequences.csv')
    enzymes = csv.reader(file_sequences, delimiter=',')
    
    # Dictionary that associates each enzyme with its sequence
    enzyme_sequence = {}
    
    for enzyme in enzymes: # For each pathway ...
        enzyme_id = enzyme[???] # Select the column for the enzyme identifier
        sequence = enzyme[???] # Select the column for the sequence
        
        # Associate the enzyme with its sequence
        enzyme_sequence[enzyme_id] = sequence
    
    # Print debugging information
    print('Sequence of enzyme P18440 :' + enzyme_sequence['P18440'])
    
    file_sequences.close()
    ```
Save the file as `module8.py` in the previous folder, and click on `Run` and then `Run Module` and observe the output.
**Note**: Replace all the green question mark place-holders <span class="nobr">(`???`)</span> with appropriate Python code.

3. Add the following code after the previous script to search, using regular expressions, the enzymes whose aminoacid sequence matches a certain pattern.
Start by searching for all enzymes whose sequence contains three consecutive alanines `AAA`:
    ```python
    # (code from step 2)
    
    # We import the `re` module to handle regular expressions
    import re
    
    # Define here your regular expression
    reg_expr = r'AAA'
    
    # For each enzyme, retrieve their sequence and determine whether
    # the sequence matches three consecutive alanines
    for enzyme_id, sequence in enzyme_sequence.items():
        # Determine whether the sequence matches the pattern
        if re.search(reg_expr, ???):
            print ('The enzyme ' + enzyme_id + ' matches the expression ' + reg_expr)
    ```
Again, run the code, observe the output that should present 22 matches.

4. Refresh your memory on the usage of [regular expressions](https://pythonforbiologists.com/regular-expressions/) to change the regular expression in the previous Python script in order to find following matches:

    a. The 13 sequences where the first two aminoacids are a alanines or a methionine.
    
    b. The 7 sequences that contain a methionine, followed by any aminoacid, followed by either a serine or a proline.

5. Change the code above to save the enzyme identifiers and sequences to a file named `relevant_sequences.csv` instead of printing them to the screen.
Refer to module 7, step 4 to refresh your memory on how to write a CSV file.


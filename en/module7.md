# Module 7 -- Merging data {#module7}

## Objectives:

- Use dictionaries to associate information
- Merge data from different data sources

## Input:

- File: [selected2.csv](files/selected2.csv)
    - created in module 5
- File: [sequences.csv](files/sequences.csv)
    - created in module 6

## Output:

- File: `paths_enzymes.csv`

## Steps:

1. Open your Personal Area on your computer and create a folder named `module7`.
Save the file `selected2.csv` given as input in the previous folder.
Open the application `IDLE (Python 3...)`.

2. Create a Python script that creates two dictionaries, one that associates each pathway with its list of enzymes based on the contents of the file `selected2.csv`, and the other that associates each enzyme with its sequence based on the contents of the file `sequences.csv`:
    ```python
    import csv
    
    file_paths = open('selected2.csv')
    paths = csv.reader(file_paths, delimiter='???')
    
    # Dictionary that associates each pathway with its list of enzymes 
    path_enzyme = {}
    
    for path in paths: # For each pathway ...
        path_id = path[???] # Select the column for the path identifier
        enzymes = path[???] # Select the column for the list of enzymes
        
        # Break that information into a list
        enzyme_list = str.split(enzymes, '???')
        
        # associate the path with its enzymes
        path_enzyme[path_id] = enzyme_list
    
    # Print debugging information
    print('Enzymes of pathway hsa00232 :' + str(path_enzyme['hsa00232']))
    
    file_sequences = open('sequences.csv')
    enzymes = csv.reader(file_sequences, delimiter=',')
    
    # Dictionary that associates each enzyme with its sequence
    enzyme_sequence = {}
    
    for enzyme in enzymes: # For each pathway ...
        enzyme_id = enzyme[???] # Select the column for the enzyme identifier
        sequence = enzyme[???] # Select the column for the sequence
        
        # associate the enzyme with its sequence       
        enzyme_sequence[enzyme_id] = sequence
    
    # Print debugging information
    print('Sequence of enzyme P18440 :' + enzyme_sequence['P18440'])
    
    file_paths.close()
    file_sequences.close()
    ```
Save the file as `module7.py` in the previous folder, and click on `Run` and then `Run Module` and observe the output.
**Note**: Replace all the green question mark place-holders (`???`) with appropriate Python code.
    
3. Add the following code after the previous script to associate each pathway to the sequences of its enzymes.
    ```python
    # (code from step 2)
    
    # For each pathway
    for path_id, enzyme_list in path_enzyme.items():
        print('Processing path: ' + path_id)
        
        # for each enzyme of that pathway 
        for enzyme_id in enzyme_list:
            # Some more debugging information
            print('Processing enzyme: ' + enzyme_id)
            
            # Retrieve the sequence associated with this enzyme
            sequence = enzyme_sequence[???]
            
            # Print the sequence associated to the path being processed
            print(path_id + ', ' + sequence)
   ```
Again, run the code and observe the output.

4. Modify the previous code to save the output in a CSV file named `paths_enzymes.csv`:
    ```python
    # (code from step 2)
    
    file_to_write = open('paths_enzymes.csv', 'w', newline='')
    w = csv.writer(file_to_write, delimiter='???')
    
    # For each pathway
    for path_id, enzyme_list in path_enzyme.items():
        # Print debugging information
        print('Processing path: ' + path_id)
        
        # for each enzyme of that pathway 
        for enzyme_id in enzyme_list:
            # Print debugging information
            print('Processing enzyme: ' + enzyme_id)
            
            # Retrieve the sequence associated with this enzyme
            sequence = enzyme_sequence[???]
            
            # Print the sequence associated to the path being processed
            print(path_id + ', ' + sequence)
            
            # Write this row to the CSV file
            w.writerow([path_id, sequence])
    
    file_to_write.close()
    ```
Again, run the code, observe the output, and open the `paths_enzymes.csv` in Excel or in a text editor.


# Module 4 -- Crossing data from several sources {#module4}

## Objectives:
- Cross data from different data sources

## Input:
- File [selected2.csv](files/selected2.csv) from module 2
- File [sequences.csv](files/sequences.csv) from module 3

## Output:
- File: `paths_enzymes.csv`

## Steps:
1. Start by creating an empty `module4.py` file.

2. We will first read the file `sequences.csv` so that we can build a dictionary where each enzyme is associated with its own aminoacid sequence.
As such, add this to your `module4.py`, filling in the question marks:
```python
    import csv
    
    # Read the CSV file
    f = open('sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    # Create an empty dictionary that we will populate as we read the CSV
    # file
    dict_sequences = {}
    
    # For each of the enzymes in the file, associate the enzyme with its
    # sequence
    for enzyme in enzymes:
        enzyme_id = enzyme[???] # The ID of this enzyme
        seq = enzyme[???]       # The aminoacid sequence of this enzyme
        dict_sequences[enzyme_id] = seq
```

3. Then we will read the file `selected2.csv` and associate each pathway with the list of enzymes that are part of it.
We will also use a dictionary for this task:
```python
    # Read the CSV file
    f = open('selected2.csv')
    paths = csv.reader(f, delimiter=???)
    
    # Create an empty dictionary that we will populate as we read the CSV
    # file
    dict_paths = {}
    
    # For each pathway in that file:
    # - extract the list of enzymes in the pathway
    # - associate the pathway with this list of enzymes
    for path in paths:
        path_id = path[???] # The ID of the pathways
        enzymes = path[???] # The field of the enzymes
        
        # Break that information into a list
        enzyme_list = str.split(enzymes, ???)
        
        # Associate the pathway ID with the corresponding list of enzymes
        dict_paths[???] = ???
```

3. Now that we have the two dictionaries, we can go through each pathway and through each enzyme in it and create a CSV file that crosses the information, associating each pathway to the aminoacid sequences of its enzymes.
To do so, add this final piece of code to your script:
```python
    # Open a file to save the output
    f = open('paths_enzymes.csv', 'w')
    w = csv.writer(f, delimiter=???)
    
    # For each pathway and each enzyme that it contains
    for path_id in dict_paths :
        # Let's print some debugging information
        print 'Processing pathway with ID ' + path_id
        
        # Retrieve the list of enzymes associated with this pathway
        enzyme_list = dict_paths[???]
        
        # Now that we have the list of enzymes, associate the pathway with each
        # aminoacid sequence
        for enzyme_id in enzyme_list:
            # Some more debugging information
            print '  enzyme = ' + enzyme_id
            
            # Retrieve the sequence associated with this enzyme
            seq = dict_sequences[???]
            
            # Write this row to the CSV file
            w.writerow([path_id, seq])
```

4. Run the code and take notice of the file that was created (`paths_enzymes.csv`).
Does it correspond to what you were expecting to see?

5. Make sure you keep a copy of the `paths_enzymes.csv` file to yourself, so that you can use it in the next modules.
For example, send it to you by email or upload it to Dropbox.

6. Submit your code and the answers to the quiz below to moodle.



## After the class:
1. Change the selection criterion used to create the file `selected2.csv` (for example selecting only the pathways with at most 10 enzymes, as proposed in the quiz of module 2).
Then change the code of today's module to accommodate this change.


# Module 3 -- UniProt as a web service {#module3}

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

1. Go to <http://www.uniprot.org/uniprot/P12345.fasta> and study the FASTA format.
Change the identifier in the link from `P12345` to another one and study its content and how it is different from the previous one.

2. In a Python file named `module3.py`, create a function called `get_sequence` that takes as input the ID of a protein and returns its aminoacid sequence.
This function:

    a. opens the URL mentioned above,
    
    b. reads the content on that URL,
    
    c. extracts the aminoacid sequence, and
    
    d. joins all the lines so that only a single string is returned
    ```python
        import urllib # This module contains functions to read URLs

        def get_sequence(identifier):
            # Establish the URL to open
            url = 'http://www.uniprot.org/uniprot/' + ??? + '.fasta'
            
            # Open the URL
            f = urllib.urlopen(url)
            
            # Read all the lines into a list
            lines = f.readlines()
            
            # Ignore the first line, which contains metadata
            del lines[0]
            
            # Join all the remaining lines into a single string
            sequence = str.join("", lines)
            
            # Remove the line ends (the "enter" used to start the next line)
            # This line end is represented as `\n`
            sequence = str.replace(sequence, '\n', '')
            
            # Return the sequence
            return ???
    ```

3. Let's try our function on a couple of proteins.
To do that, add the following lines to the Python file (replace the `???` instances with any protein IDs you want):
```python
    sequence1 = get_sequence('P12345')
    sequence2 = get_sequence('???')
    sequence3 = get_sequence('???')
    
    print "SEQUENCE 1:\n" + sequence1 + "\n"
    print "SEQUENCE 2:\n" + sequence2 + "\n"
    print "SEQUENCE 3:\n" + sequence3 + "\n"
```

4. Now we are going to read the enzymes in the `selected2.csv` file and perform a lookup of their aminoacid sequences.
    
    a. Remove or comment the code from step 3.
    
    b. Replace it with this:
    ```python
        import csv
        
        # Open the output file from the previous module
        f = open('selected2.csv')
        paths = csv.reader(f, delimiter=???)
        
        # Start with an empty list of enzymes
        enzymes = []
        
        # Then:
        # - read the information of each pathway,
        # - extract the list of enzymes of each pathway, and
        # - append each enzyme to the list of enzymes
        for path in paths:
            enzymes_field = path[???] # The field of the enzymes
            
            # Split the enzymes into a list, as in module 2
            enzymes_in_this_path = str.split(enzymes_field, ???)
            
            # Append each one into the master enzyme list
            for e in enzymes_in_this_path:
                enzymes.append(e)
    ```

5. Now that we have a list of enzymes, we can use it and the function we created in the beginning to get the aminoacid sequence of each enzyme.
We will save this information into a new file.
Continue adding code to your `module3.py` file:
```python
    f = open('sequences.csv', 'wb')
    w = csv.writer(f, delimiter=???)
    
    for e in enzymes:
        seq = get_sequence(e)
        w.writerow([e, seq])
    
    f.close()
```

6. Run the code and take notice of the file that was created (`sequences.csv`).
Does it correspond to what you were expecting to see?

7. Make sure you keep a copy of the `sequences.csv` file to yourself, so that you can use it in the next modules.
For example, send it to you by email or upload it to Dropbox.


## After the class:

1. Observe in `sequences.csv` that some enzymes appear more than once, and try to explain why?

2. Change your code in order to find the sequence of all the enzymes in the metabolic pathways, and not only the enzymes in the pathways selected in the previous module.
Save the sequences into a file named `all_sequences.csv`.

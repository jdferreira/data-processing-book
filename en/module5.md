# Module 5 -- Information selection with regular expressions {#module5}

## Objectives:
- Develop regular expressions that represent several selection criteria
- Use the `re` Python module to create the regular expressions
- Search for aminoacid motives in the enzyme sequences

## Input:
- File: [sequences.csv](files/sequences.csv)
    - created in module 3

## Output:
- File: `relevant_sequences_1.csv`
- File: `relevant_sequences_2.csv`
- File: `relevant_sequences_3.csv`

## Steps:

1. In this module, we will search, using regular expressions, the enzymes whose aminoacid sequence matches a certain pattern.
    
    a. You can consult a [reference cheat sheet of regular expressions](http://www.cheat-sheets.org/saved-copy/regular_expressions_cheat_sheet.png).
    
    b. You can also find the correspondence between each aminoacid and their 1-letter code in this [chart](http://bio100.class.uic.edu/lectures/aminoacids01.jpg).
    
    c. Familiarize yourself these two charts.

2. We start by reading the file `sequences.csv` and creating a dictionary that associates the enzymes with their aminoacid sequence, just as we did in the previous module.
Start the `module5.py` script:
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

3. Now that we have the dictionary, let's search for all enzymes whose aminoacid sequence contains three consecutive alanines:
```python
    # We import the re module to handle regular expressions
    import re
    
    # Define here your regular expression
    reg_expr = r'???'
    
    # For each enzyme, retrieve their sequence and determine whether
    # the sequence matches three consecutive alanines
    for enzyme in dict_sequences:
        # Retrieve the aminoacid sequence
        seq = ???
        
        # Determine whether the sequence matches the pattern
        if re.search(reg_expr, seq):
            print 'The enzyme ' + ??? + ' matches the expression ' + reg_expr
```

4. Change the code above to save the enzyme identifiers and sequences to a file named `relevant_sequences_1.csv` instead of printing them to the screen.
Refer to module 3, step 5 to refresh your memory on how to write a CSV file.

5. Change the regular expression in the Python script in order to find other sequences.
For each of these patterns, save a new file named `relevant_sequences_2.csv` and `relevant_sequences_3.csv` respectively.
    
    a. Sequences where the first 5 aminoacids are non-polar.
    
    b. Sequences that contain a methionine, followed by any aminoacid, followed by either a serine or a proline.

6. Run the code and take notice of the files that were created.
Do they correspond to what you were expecting to see?

7. Make sure you keep a copy of the `relevant_sequences_1.csv`, `relevant_sequences_2.csv` and `relevant_sequences_3.csv` files to yourself, so that you can use them in the next modules.
For example, send it to you by email or upload it to Dropbox.


## After the class:
1. Write an alternative regular expression to the one of step 3 having the same meaning but using different regular expression elements.

2. Imagine you want to apply the first regular expression used in this module (three consecutive alanines) to the file `relevant_sequences_2.csv` instead of `sequences.csv`.
Change the Python script to accommodate this change.
Verify whether the result is equal to what you got in `relevant_sequences_1.csv`.

**Note**: To the students that want to explore regular expressions in more detail, we propose the following exercise:<br>
What regular expression describes a molecular group that connects to GTP?
This is a complex pattern that is composed of three subsequences (note that there is no aminoacid with the letter `X`; this letter is used to describe that any aminoacid can occur in that position):

- the first is `GXXXXGK`,
- the second is `DXXG`, and
- the third is `NKXD` or `NKXW`.

The first and second group are separated by either 40 to 80 aminoacids or 130 to 170 aminoacids; the second and third groups are separated by 40 to 80 aminoacids.
<small>[Source: Dever TE, Glynias MJ, Merrick WC (1987). PNAS 84(7), 1814-1818.]</small>

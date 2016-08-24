% Data processing for metabolic pathways
  using files, web services and databases
% João D. Ferreira; Francisco M. Couto
% August 2016

# Introduction

The aim of these exercises is to provide students the ability and competence to process data in an automatic fashion.
The main topic surrounding these exercises will be metabolic pathway data processing, with a closer focus on the proteins that catalyse the chemical reaction those pathways, also known as _enzymes_.
Despite working with metabolic pathways during the classes, the data processing methods that the students will learn in this class can be applied to many other types of data.

## Data

The following figure represents the first steps in the glycolysis, a metabolic pathway that decomposes glucose in smaller chemical compounds.
This figure includes a representation of five steps in this pathway, each one catalysed by a different enzyme.

![A Metabolic pathway](images/pathway.png "An example of a metabolic pathway")

For this class, we will provide [an Excel file](files/metabolic_pathways.xls) with information on 297 metabolic pathways.
Each line in this file contains:

- an identifier of the metabolic pathway;
- the name of the pathway;
- the class it belongs to;
- a list of the enzymes that participate in the pathway.

Therefore, the Excel file has 297 lines, plus another one for the column headers.

The following image shows a screenshot of the Excel file and its data

![A screenshot of the Excel file](images/excel.png "A screenshot showing part of the data in the Excel file")

This information comes from an online database called [Kyoto Encyclopedia of Genes and Genome](http://www.genome.jp/kegg/kegg2.html). The enzymes are referred by their UniProt code.
[UniProt](http://www.uniprot.org/) is a database of proteins that contain, among a vast amount of information, the aminoacid sequences of the proteins.

## Processing

Despite the data being provided to the students as an Excel file, the data processing operations will mostly be executed with a programming language.
In this class, we will use [Python](http://www.python.org)
Processing our data with Python instead of Excel offers several benefits:

- We can define a set of operations to be executed automatically, which in Excel would take a large amount of time, since it is mostly driven by user interaction rather than direct commands
- Programming languages can handle complex data types, while Excel is mostly oriented towards numeric computations

No deep knowledge of programming will be required for the class exercises, as we will provide most of the code.
In fact, the students will not directly learn the details of Python as a programming language, but will instead be given "recipes" that contain most of the necessary logic, with small snippets of missing code that the students need to fill.
However, we expect that the students familiarize themselves with Python syntax before the first module of this class by following some online courses.
For example, [Codecademy](https://www.codecademy.com/en/tracks/python) contains six modules that will help the students in this task:

- [Python Syntax](https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1?curriculum_id=4f89dab3d788890003000096)
- [Strings & Console Output](https://www.codecademy.com/courses/python-beginner-sRXwR/0/1?curriculum_id=4f89dab3d788890003000096)
- [Conditionals & Control Flow](https://www.codecademy.com/courses/python-beginner-BxUFN/0/1?curriculum_id=4f89dab3d788890003000096)
- [Python Lists and Dictionaries](https://www.codecademy.com/courses/python-beginner-en-pwmb1/0/1?curriculum_id=4f89dab3d788890003000096)
- [File Input/Output](https://www.codecademy.com/courses/python-intermediate-en-OGNHh/0/1?curriculum_id=4f89dab3d788890003000096)


# Module 1 -- Metabolic pathways data

## Part I: Notepad++ and Python

### Objectives:

- Open Notepad++, write some Python code and save the file
- Execute the file with Python

### Steps

1. In the Windows start menu, open `Notepad++`.

![Open Notepad++](images/open-notepad.png "Open Notepad++")

2. Write a small "Hello World!" program and save the file in the Desktop (or in whichever folder you want) with the name `test.py`.

![The small \"Hello World\" file](images/hello-world.png "The small \"Hello World\" file")

3. In the start menu, open the command line (`cmd`).

![Starting the command line](images/open-cmd.png "Starting the command line")

4. In the terminal (the command line window), we need to navigate to the Desktop folder and then instruct Python to run our `test.py`.
We do this by running the following commands:
```bash
    cd Desktop
    python test.py
```
![The \"Hello World\" output](images/hello-world-run.png "The \"Hello World\" output")

5. Observe the output produced by Python.


## Part II: Beginning data processing

### Objectives:
- Understand the CSV format
- Convert between the Excel format and CSV
- Understand the meaning of metadata
- Read CSV files with Python

### Input:
- File: [metabolic_pathways.xls](files/metabolic_pathways.xls)

### Output:
- File: `metabolic_pathways.csv`
- Console:
```awk
    Glycolysis / Gluconeogenesis
    Citrate cycle (TCA cycle)
    Pentose phosphate pathway
    Pentose and glucuronate interconversions
    ...
```

### Steps:

1. Open the Excel file.
Take special attention to the contents of this file and try to get familiar with the data it contains.
This step is one of the most important to data processing, as it allows us to gain intuition about the information that we're dealing with.

2. Remove the first row, which contains only the headers of the columns.
(This first row is called "metadata" since it explains the data contained in the file but is not itself actual data.)

3. Using Excel's functionalities, save the data in the CSV format using the name `metabolic_pathways.csv`.

4. Open the CSV file in a text editor (Notepad++) and study the file that you saved.
For example, determine what character is used to separate the various fields of the data, whether the fields are delimited and how, etc.

5. Let's create a Python script to read the CSV file and print the name of each pathway.
    a. Create an empty file and save it as `module1.py` on the same folder where the `metabolic_pathways.csv` file is.
    Do not forget the `.py` ending, as this instructs the computer that the file is a Python script.
    
    b. Copy and paste the following code to your file:
    ```python
        import csv
        
        f = open('metabolic_pathways.csv')   # Open the file
        
        paths = csv.reader(f, delimiter=???) # Create a CSV reader object
        
        for path in paths: # For each pathway ...
            print ???      # ... print its name
    ```
    
    c. Replace all the green question mark place-holders (`???`) with appropriate Python code.

6. Run the Python script and observe the output.
Does it correspond to what you were expecting to see?

7. Make sure you keep a copy of the `metabolic_pathways.csv` file to yourself, so that you can use it in the next modules.
For example, send it to you by email or upload it to Dropbox.

8. Submit your code and the answers to the quiz below to moodle.

### Quiz:
1. How would you change the Python code to print the class of each pathway instead of its name?

2. Explain why, in the CSV file, some fields are delimited by quotes (`"`) and other are not.


# Module 2 -- Simple selection and saving data on disk

## Objectives:
- Transform a selection criterion into actual Python code
- Implement the selection process in Python
- Save the selected information on a new file

## Input:
- File: [metabolic_pathways.csv](files/metabolic_pathways.xls)

## Output:
- File: `selected1.csv`
    * containing the data of the pathway `hsa04210`.
- File: `selected2.csv`
    * containing the data of the pathway `hsa00730` and `hsa04122`.

## Steps:
1. Let's create a Python function that determines whether the path ID of a pathway is `hsa04210`:
    a. Create an empty file and save it as `module2.py` on the same folder where the `metabolic_pathways.csv` file is.
    Do not forget the `.py` ending, as this instructs the computer that the file is a Python script.
    
    b. Copy and paste the following code to your file:
    ```python
        def filter1(path):
            path_id = path[???]  # Select the column for the ID
            
            if path_id == '???': # Replace with the ID we are searching for
                return True
            else:
                return False
    ```
    
    c. Replace the green question marks (`???`) with appropriate Python code.

2. The previous code is just a function that will run when we call it, but does not do anything on its own.
Let's add more code to the file so that we actually go through each pathway and use the filter on it.
```python
    import csv
    
    # ------------------------------------- #
    # PLACE THE FUNCTION DEFINED ABOVE HERE #
    # ------------------------------------- #
    
    # Open the original file and read all pathways
    file_to_read = open('metabolic_pathways.csv')
    paths = csv.reader(file_to_read, delimiter=???)
    
    # Open the file where we will save the selection
    file_to_write = open('selected1.csv', 'w')
    w = csv.writer(file_to_write, delimiter=???)
    
    for path in paths:
        if filter1(path):
            w.writerow(path)
    
    # Close the file
    file_to_write.close()
```

3. Run `module2.py` and study the file that was produced.
Make sure it corresponds to what you were expecting.

4. Edit the file `module2.py` by creating a new filter `filter2` which selects the pathways where the enzyme Q9Y697 participates.
If necessary, consult the documentation for the function `str.split` at <https://docs.python.org/2/library/stdtypes.html#str.split>.

    a. Create the new function `filter2`:
    ```python
        def filter2(path):
            field = path[???] # Select the column for the list of enzymes
            
            # Break that information into a list
            enzyme_list = str.split(field, ???)
            
            # enzyme_list is now a list of strings, such as follows:
            # ['H9EC08', 'P03905', 'G9LG04', 'P03901']
            
            # Return True if our selected enzyme is in that list
            if '???' in enzyme_list:
                return True
            else:
                return False
    ```
    
    b. Also change `'selected1.csv'` into `'selected2.csv'`.
    This ensures that the new output will not overwrite the previous one.

5. Run `module2.py` again and study the file that was produced.
Make sure it corresponds to what you were expecting; in particular, make sure all the selected pathways contain the enzyme Q9Y697.

6. Make sure you keep a copy of the `selected1.csv` and `selected2.csv` files to yourself, so that you can use them in the next modules.
For example, send it to you by email or upload it to Dropbox.

7. Submit your code and the answers to the quiz below to moodle.


## Quiz:
1. Create a new filter function `filter3` that selects the pathways that are part of the class "Human Diseases; Cancers".

2. Using the built-in function `len`, which returns the number of elements in a list, create a function `filter4` that selects pathways containing at most 10 enzymes.
The documentation for this function can be found in <https://docs.python.org/2/library/functions.html#len>

**Note**: to read and write CSV files in Python, we have been using the `csv` module.
This module allows us to specify the format of the file to read/write, _e.g._ which character to use to separate the fields and to delimit the fields.
You should familiarize yourself with this module by reading its documentation at <https://docs.python.org/2/library/csv.html>.


# Module 3 -- UniProt as a web service

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
Try to change the identifier in the link from `P12345` to another one.

2. In a Python file named `module3.py`, create a function called `get_sequence` that takes as input the ID of a protein and returns its aminoacid sequence.
This function:
    a. opens the URL mentioned above,
    b. reads the content on that URL,
    c. extracts the aminoacid sequence, and
    d. joins all the lines so that only a single string is returned
    ```python
        import urllib # This module contains functions to read URLs

        def get_sequence(ID):
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
            # This line end is represented as \n
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
    f = open('sequences.csv', 'w')
    w = csv.writer(f, delimiter=???)
    
    for e in enzymes:
        seq = get_sequence(e)
        w.writerow([e, seq])
    
    f.close()
```

6. Run the code and take notice of the output that was created (the `sequences.csv` file). Does it correspond to what you were expecting to see?

7. Make sure you keep a copy of the `sequences.csv` file to yourself, so that you can use it in the next modules.
For example, send it to you by email or upload it to Dropbox.

8. Submit your code and the answers to the quiz below to moodle.


## Quiz:
1. Observe in `sequences.csv` that some enzymes appear more than once.
Can you explain why?

2. Describe the code in step 5 line by line.


# Module 4 -- Crossing data from several sources

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

3. Then we will read the file `selected.csv` and associate each pathway with the list of enzymes that are part of it.
We will also use a dictionary for this task:
```python
    # Read the CSV file
    f = open('selected.csv')
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
        enzyme_list = str.split(field, ???)
        
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

4. Run the Python script and observe the output.
Does it correspond to what you were expecting to see?

5. Make sure you keep a copy of the `paths_enzymes.csv` file to yourself, so that you can use it in the next modules.
For example, send it to you by email or upload it to Dropbox.

6. Submit your code and the answers to the quiz below to moodle.



## Quiz:
1. Imagine you created the file `selected2.csv` based on a different selection criterion (for example selecting only the pathways with at most 10 enzymes, as proposed in the quiz of module 2).
Describe which modifications you would need to execute in the code of today's module to accommodate this change.

2. The output file `paths_enzymes.csv` contains some enzymes more than once.
Explain why.




# Module #

## Objectives:
- 
- 
- 

## Input:
- 
- 
- 

## Output:
- 
- 

## Steps:
1. 

2. 

3. 

4. 

## Quiz:
1. 

2. 

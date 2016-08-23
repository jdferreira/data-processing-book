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
- Convert between CSV and the Excel format
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

2. Using Excel's functionalities, save the data in the CSV format using the name `metabolic_pathways.csv`.

3. Open the CSV file in a text editor (Notepad++) and study the file that you saved.
For example, determine what character is used to separate the various fields of the data, whether the fields are delimited and how, etc.

4. Let's create a Python script to read the CSV file and print the name of each pathway.
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

5. Run the Python script and observe the output.
Does it correspond to what you were expecting to see?

6. Make sure you keep a copy of the `metabolic_pathways.csv` file to yourself, so that you can use it in the next module.
For example, send it to you by email or upload it to Dropbox.

7. Submit your code and the answers to the quiz below to moodle.

### Quiz:
1. How would you change the Python code to print the class of each pathway instead of its name?

2. Explain why, in the CSV file, some fields are delimited by quotes (`"`) and other are not.



# Module 2 -- Simple selection and saving data on disk

## Objectives:
- Transform selection criteria into actual Python code
- Implementar o processo de seleção em Python
- Guardar informação em ficheiro

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
            path_id = path[???]  # select the column for the ID
            
            if path_id == '???': # replace with the ID we are searching for
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
    # PLACE HERE THE FUNCTION DEFINED ABOVE #
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
            field = path[???]  # select the column for the list of enzymes
            
            # break that information into a list
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

## Quiz:
1. Create a new filter function `filter3` that selects the pathways that are part of the class "Human Diseases; Cancers".

2. Using the built-in function `len`, which returns the number of elements in a list, create a function `filter4` that selects pathways containing at most 10 enzymes.
The documentation for this function can be found in <https://docs.python.org/2/library/functions.html#len>

**Note**: to read and write CSV files in Python, we have beein using the `csv` module.
This module allows us to specify the format of the file to read/write, _e.g._ which character to use to separate the fields and to delimit the fields.
You should familiarize yourself with this module by reading its documentation at <https://docs.python.org/2/library/csv.html>.






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

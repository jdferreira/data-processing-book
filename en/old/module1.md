## Processing

Despite the data being provided to the students as an Excel file, the data processing operations will mostly be executed with a programming language.
In this class, we will use [Python](http://www.python.org).
Processing our data with Python instead of Excel offers several benefits:

- We can define a set of operations to be executed automatically, which in Excel would take a large amount of time, since it is mostly driven by user interaction rather than direct commands;
- Programming languages can handle complex data types, while Excel is mostly oriented towards numeric computations.

No deep knowledge of programming will be required for the class exercises, as we will provide most of the code.
In fact, the students will not directly learn the details of Python as a programming language, but will instead be given "recipes" that contain most of the necessary logic, with small snippets of missing code that the students need to fill.
However, we expect that the students familiarize themselves with Python syntax by following some online courses.
For example, [Codecademy](https://www.codecademy.com/en/tracks/python) contains six modules that will help the students in this task:

- [Python Syntax](https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1?curriculum_id=4f89dab3d788890003000096)
- [Strings & Console Output](https://www.codecademy.com/courses/python-beginner-sRXwR/0/1?curriculum_id=4f89dab3d788890003000096)
- [Conditionals & Control Flow](https://www.codecademy.com/courses/python-beginner-BxUFN/0/1?curriculum_id=4f89dab3d788890003000096)
- [Python Lists and Dictionaries](https://www.codecademy.com/courses/python-beginner-en-pwmb1/0/1?curriculum_id=4f89dab3d788890003000096)
- [File Input/Output](https://www.codecademy.com/courses/python-intermediate-en-OGNHh/0/1?curriculum_id=4f89dab3d788890003000096)

# Module 1 -- Metabolic pathways data {#module1}

## Part I: Notepad++ and Python

### Objectives:

- Open Notepad++, write some Python code and save the file
- Execute the file with Python

### Steps:

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

5. Observe the output produced by Python and ensure that the screen shows the following:
```text
    Hello World!
```

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
```text
    Glycolysis / Gluconeogenesis
    Citrate cycle (TCA cycle)
    Pentose phosphate pathway
    Pentose and glucuronate interconversions
    ...
```

### Steps:

1. Open the Excel file.
Take special attention to the contents of this file and get familiar with the data it contains.
This step is one of the most important to data processing, as it allows us to gain intuition about the information that we're dealing with.

2. Remove the first row, which contains the headers of the columns.
(This first row is called "metadata" since it explains the data contained in the file but is not itself actual data.)

3. Using Excel's functionalities, save the data in the CSV format using the name `metabolic_pathways.csv`.

4. Open the CSV file in a text editor (`Notepad++`) and study the file that you saved.
For example, determine what character is used to separate the various fields of the data, whether the fields are delimited and how, _etc_.

5. Let's create a Python script to read the CSV file and print the name of each pathway.

    a. Create an empty file and save it as `module1.py` on the same folder where the `metabolic_pathways.csv` file is.
    Do not forget the `.py` ending, as this instructs the computer that the file is a Python script.
    
    b. Copy and paste the following code to your file:
    ```python
        import csv
        
        f = open('metabolic_pathways.csv') # Open the file
        
        paths = csv.reader(f, delimiter=???) # Create a CSV reader object
        
        for path in paths: # For each pathway ...
            print ???      # ... print its name
        
        # Close the file
        f.close()
    ```
    
    c. Replace all the green question mark place-holders (`???`) with appropriate Python code.

6. Run `module1.py` in the command line and observe the output.
Does it correspond to what you were expecting to see?

7. Make sure you keep a copy of the `metabolic_pathways.csv` file to yourself, and the so `module1.py` script, that you can use them in the next modules.
For example, send it to you by email or upload it to Dropbox.

## After the class:

1. Change the Python code to print the class of each pathway instead of its name.

2. Vertify that some fields in the CSV file are delimited by quotes <nobr>(`"`)</nobr> and other are not. Explain why.

# Module 1 -- Metabolic pathways data {#module1}

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

6. Run `module1.py` in the command line and observe the output.
Does it correspond to what you were expecting to see?

7. Make sure you keep a copy of the `metabolic_pathways.csv` file to yourself, so that you can use it in the next modules.
For example, send it to you by email or upload it to Dropbox.


## After the class:
1. Change the Python code to print the class of each pathway instead of its name.

2. Vertify that some fields in the CSV file are delimited by quotes (`"`) and other are not.

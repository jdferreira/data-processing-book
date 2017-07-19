# Module 4 -- Read and print data {#module4}

## Objectives:
- Read CSV files and print data with Python
- Understand the meaning of metadata

## Input:

- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - created in the previous module

### Output:
- Console:
```text
    Glycolysis / Gluconeogenesis
    Citrate cycle (TCA cycle)
    Pentose phosphate pathway
    Pentose and glucuronate interconversions
    ...
```
    
## Steps:

1. Open your Personal Area on your computer and create a folder named module4.

2. Save the file `metabolic_pathways.csv` given as input in the previous folder.

3. Open the application `IDLE (Python 3...)`
**Note**: do not open version 2 of Python 

4. Click on `File`, then on `New File`, and write

    ```python
    print('Hello World!')
    ```

5. Save the file as `module4.py` in the previous folder.

6. Click on `Run` and then `Run Module` and observe the output produced by Python and ensure that the screen shows the following:

    ```text
    Hello World!
    ```

7. Create a Python script to read the CSV file and print the name of each pathway. 
Replace the previous command: 

    ```python
    print('Hello World!')
    ```

by the following code:    

    ```python
    import csv
     
    f = open('metabolic_pathways.csv') # Open the file
  
    paths = csv.reader(f, delimiter='???') # Create a CSV reader object
    
    next(paths) # ignore the first row, which contains the headers of the columns called "metadata" 
        
    for path in paths: # For each pathway ...
        print(path[???])      # ... print its name
        
    # Close the file
    f.close()
    ```
    
**Note**: Replace all the green question mark place-holders (`???`) with appropriate Python code.

8. Click on `Run` and then `Run Module` and observe the output. 
Does it correspond to what you were expecting to see?

9. Change the previous Python code to print the class of each pathway instead of its name.

**Note**: to read and write CSV files in Python, we have been using the `csv` module.
This module allows us to specify the format of the file to read/write, _e.g._ which character to use to separate the fields and to delimit the fields.
You should familiarize yourself with this module by reading its documentation at <https://docs.python.org/2/library/csv.html>.



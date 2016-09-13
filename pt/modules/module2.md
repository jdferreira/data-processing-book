# Module 2 -- Simple selection and saving data on disk {#module2}

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


## After the class:
1. Create a new filter function `filter3` that selects the pathways that are part of the class "Human Diseases; Cancers".

2. Using the built-in function `len`, which returns the number of elements in a list, create a function `filter4` that selects pathways containing at most 10 enzymes.
The documentation for this function can be found in <https://docs.python.org/2/library/functions.html#len>

**Note**: to read and write CSV files in Python, we have been using the `csv` module.
This module allows us to specify the format of the file to read/write, _e.g._ which character to use to separate the fields and to delimit the fields.
You should familiarize yourself with this module by reading its documentation at <https://docs.python.org/2/library/csv.html>.



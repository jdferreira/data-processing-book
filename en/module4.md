# Module 4 -- Read and print data {#module4}

## Objectives:
- Read CSV files and print data with Python
- Understand the meaning of metadata

## Input:

- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - created in the previous module

### Output:
- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - without the headers
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

3. Open the CSV file in a text editor (Notepad) and remove the first row, which contains the headers of the columns, and save the file.
(This first row is called "metadata" since it explains the data contained in the file but is not itself actual data.)

4. Open the application `IDLE (Python 3...)`
NOTE: do not open version 2 of Python 

5. Click on `File`, then on `New File`, and write
```python
    print('Hello World!')
```

6. Save the file as `module4.py` in the previous folder.

7. Click on `Run` and then `Run Module` and observe the output produced by Python and ensure that the screen shows the following:
```text
    Hello World!
```

8. Let's create a Python script to read the CSV file and print the name of each pathway. 
Replace the previous command: 
	```python
		print('Hello World!')
	```
by the following code:    
    ```python
        import csv
        
        f = open('metabolic_pathways.csv') # Open the file
        
        paths = csv.reader(f, delimiter='???') # Create a CSV reader object
        
        for path in paths: # For each pathway ...
            print(paths[???])      # ... print its name
        
        # Close the file
        f.close()
    ```
    
NOTE: Replace all the green question mark place-holders (`???`) with appropriate Python code.

9. Click on `Run` and then `Run Module` and observe the output. 
Does it correspond to what you were expecting to see?

10. Change the previous Python code to print the class of each pathway instead of its name.



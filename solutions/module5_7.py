import csv
 
# Open the original file to read all pathways
file_to_read = open('metabolic_pathways.csv')
paths = csv.reader(file_to_read, delimiter=',')
next(paths) 

# Open the file to save the selection
# The 'w' instructs Python that we want to write on this file
# The newline='' avoids blank lines between each row
file_to_write = open('selected3.csv', 'w', newline='')
w = csv.writer(file_to_write, delimiter=',')
    
for path in paths: # For each pathway ...
    path_id = path[0] 
    enzymes = path[3] # Select the column for the list of enzymes
        
    # Break that information into a list
    enzyme_list = str.split(enzymes, '|')
    
    # `enzyme_list` is now a list of strings, such as follows:
    # ['H9EC08', 'P03905', 'G9LG04', 'P03901']
    
    if len(enzyme_list)>500: # Check if our selected enzyme is in that list
       print("the pathway " + path_id + " was written to the file")      
       w.writerow(path)      # write the pathway to the file
 
# Close the files
file_to_read.close()
file_to_write.close()

import csv
 
# Open the original file to read all pathways
file_to_read = open('metabolic_pathways.csv')
paths = csv.reader(file_to_read, delimiter=',')
next(paths) 

# Open the file to save the selection
# The 'w' instructs Python that we want to write on this file
# The newline='' avoids blank lines between each row
file_to_write = open('selected1.csv', 'w', newline='')
w = csv.writer(file_to_write, delimiter=',')
    
for path in paths: # For each pathway ...
    path_id = path[0]  
    
    if path_id == 'hsa03030':
       print("the pathway " + path_id + " was written to the file")      
       w.writerow(path)      # write the pathway to the file
 
# Close the files
file_to_read.close()
file_to_write.close()

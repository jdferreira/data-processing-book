# Module 6 -- Create a database {#module6}

## Objectives:
- Design a simple database schema to store information on the pathways
- Use foreign keys

## Input:
- None

## Output:
- Database file: `pathways.db`

## Steps:

1. Open your Personal Area on your computer and create a folder named module9.

2. Like in module 3 open the application [DB Browser for SQLite](http://sqlitebrowser.org/),
and create a new database named `pathways.db` and save it in the previous folder. 
Click Cancel when asked for `Edit table definition`.

3. To create the table click on `Execute SQL` and write:

```sql
	-- Erase the tables in case they already exist in the database
    DROP TABLE IF EXISTS path;
    DROP TABLE IF EXISTS enzyme;
    DROP TABLE IF EXISTS path_enzyme;
    
	-- This table will contain data about the pathways
	CREATE TABLE path (
		id VARCHAR(255) PRIMARY KEY,
		name VARCHAR(255) NOT NULL,
		class VARCHAR(255) NOT NULL
	);

	-- This table will contain data about the enzymes
   	CREATE TABLE enzyme (
		id VARCHAR(255) PRIMARY KEY,
		sequence TEXT NOT NULL
	);

	-- This table will associate each pathway with its enzymes
	CREATE TABLE path_enzyme (
		path_id VARCHAR(255),
		enzyme_id VARCHAR(255),
		PRIMARY KEY (path_id, enzyme_id),
		FOREIGN KEY (path_id) REFERENCES ??? (id),
		FOREIGN KEY (enzyme_id) REFERENCES ??? (id)
	);
```
and then click on Execute SQL (play icon).

**Note**: Replace all the green question mark place-holders (`???`) with appropriate SQL code.

3. Now, insert some data in these three tables.
We will only insert two pathways and three enzymes of the pathway based on the contents of the files 
`sequences.csv` and `selected2.csv` created in the previous modules.
Click on `Execute SQL` and write:
```sql
	-- Delete any rows in case they already exist
    DELETE FROM path;
    DELETE FROM enzyme;
    DELETE FROM path_enzyme;

	-- Insert the pathways
	INSERT INTO path (id, name, class) VALUES ('hsa00232', 'Caffeine metabolism', 'Metabolism; Biosynthesis of other secondary metabolites');
	INSERT INTO path (id, name, class) VALUES ('hsa00983', 'Drug metabolism - other enzymes', 'Metabolism; Xenobiotics biodegradation and metabolism');

	
	-- Insert the enzymes
	INSERT INTO enzyme (id, sequence) VALUES ('P05177','MALSQSVPFSATELLLASAIFCLVFWVLKGLRPRVPKGLKSPPEPWGWPLLGHVLTLGKNPHLALSRMSQRYGDVLQIRIGSTPVLVLSRLDTIRQALVRQGDDFKGRPDLYTSTLITDGQSLTFSTDSGPVWAARRRLAQNALNTFSIASDPASSSSCYLEEHVSKEAKALISRLQELMAGPGHFDPYNQVVVSVANVIGAMCF');
	INSERT INTO enzyme (id, sequence) VALUES ('P18440','MDIEAYLERIGYKKSRNKLDLETLTDILQHQIRAVPFENLNIHCGDAMDLGLEAIFDQVVRRNRGGWCLQVNHLLYWALTTIGFETTMLGGYVYSTPAKKYSTGMIHLLLQVTIDGRNYIVDAGFGRSYQMWQPLELISGKDQPQVPCVFRLTEENGFWYLDQIRREQYIPNEEFLHSDLLEDSKYRKIYSFTLKPRTIEDFESMNT');
	INSERT INTO enzyme (id, sequence) VALUES ('P00492','MATRSPGVVISDDEPGYDLDLFCIPNHYAEDLERVFIPHGLIMDRTERLARDVMKEMGGHHIVALCVLKGGYKFFADLLDYIKALNRNSDRSIPMTVDFIRLKSYCNDQSTGDIKVIGGDDLSTLTGKNVLIVEDIIDTGKTMQTLLSLVRQYNPKMVKVASLLVKRTPRSVGYKPDFVGFEIPDKFVVGYALDYNEYFRDLNHVC');

	-- Associate the enzymes with the pathways
	INSERT INTO path_enzyme (path_id, enzyme_id) VALUES ('hsa00232','P05177');
	INSERT INTO path_enzyme (path_id, enzyme_id) VALUES ('hsa00232','P18440');
	INSERT INTO path_enzyme (path_id, enzyme_id) VALUES ('hsa00983','P00492');
	INSERT INTO path_enzyme (path_id, enzyme_id) VALUES ('hsa00983','P18440');
```
and then click on Execute SQL (play icon).	
Click on write changes...
	

4. Finally, let's just make sure that the tables contain some data.
To do that, you can use [DB Browser for SQLite](http://sqlitebrowser.org/), which has a [portable version](https://github.com/sqlitebrowser/sqlitebrowser/releases/download/v3.9.1/SQLiteDatabaseBrowserPortable_3.9.1_English.paf.exe) that can be used without installation.
o check with Python, we can select, for example, the sequences of each pathway.
```python
	rows = connection.execute('SELECT id, sequence FROM enzyme')
	for row in rows:
		enzyme_id = row[0]
		enzyme_sequence = row[1]
		
		print enzyme_id + ' starts with ' + enzyme_sequence[:5]
```

5. Ensure that the output on the screen is:
```text
	Q53FP3 starts with MLLRA
	Q9Y697 starts with MLLRA
```

6. Make sure you keep a copy of the `pathways.db` file to yourself, so that you can use it in the next module.
For example, send it to you by email or upload it to Dropbox.

## After the class:

1. Explain why the primary key of the table `path_enzyme` has two atributes.

2. Modify the database schema so that the database can store the name of the enzymes and also their position within the pathway (a whole number).

3. Change the code of step 4 so that you can also verify the contents of the  tables `paths` and `path_enzyme`.


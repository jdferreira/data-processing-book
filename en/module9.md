# Module 6 -- Create a database {#module6}

## Objectives:
- Design a simple database schema to store information of the pathways
- Use SQL statements to define and change the database structure or schema
- Use SQL statements to insert, update and delete data

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
		PRIMARY KEY (path_id, ???)
	);
```
and then click on Execute SQL (play icon).
Explain why the primary key of the table `path_enzyme` has two atributes.

**Note**: Replace all the green question mark place-holders (`???`) with appropriate SQL code.

4. Insert some data in these three tables.
We will only insert two pathways and three enzymes of the pathway based on the contents of the files 
`sequences.csv` and `selected2.csv` created in the previous modules.
Click on `Execute SQL` and run the following SQL commands:
```sql
	-- Delete any rows in case they already exist
    DELETE FROM path;
    DELETE FROM enzyme;
    DELETE FROM path_enzyme;

	-- Insert the pathways
	INSERT INTO path (id, name, ???) VALUES ('hsa00232', 'Caffeine metabolism', 'Metabolism; Biosynthesis of other secondary metabolites');
	INSERT INTO path (id, name, ???) VALUES ('hsa00983', 'Drug metabolism - other enzymes', 'Metabolism; Xenobiotics biodegradation and metabolism');

	
	-- Insert the enzymes
	INSERT INTO enzyme (id, ???) VALUES ('P05177','MALSQSVPFSATELLLASAIFCLVFWVLKGLRPRVPKGLKSPPEPWGWPLLGHVLTLGKNPHLALSRMSQRYGDVLQIRIGSTPVLVLSRLDTIRQALVRQGDDFKGRPDLYTSTLITDGQSLTFSTDSGPVWAARRRLAQNALNTFSIASDPASSSSCYLEEHVSKEAKALISRLQELMAGPGHFDPYNQVVVSVANVIGAMCF');
	INSERT INTO enzyme (id, ???) VALUES ('P18440','MDIEAYLERIGYKKSRNKLDLETLTDILQHQIRAVPFENLNIHCGDAMDLGLEAIFDQVVRRNRGGWCLQVNHLLYWALTTIGFETTMLGGYVYSTPAKKYSTGMIHLLLQVTIDGRNYIVDAGFGRSYQMWQPLELISGKDQPQVPCVFRLTEENGFWYLDQIRREQYIPNEEFLHSDLLEDSKYRKIYSFTLKPRTIEDFESMNT');
	INSERT INTO enzyme (id, ???) VALUES ('P00492','MATRSPGVVISDDEPGYDLDLFCIPNHYAEDLERVFIPHGLIMDRTERLARDVMKEMGGHHIVALCVLKGGYKFFADLLDYIKALNRNSDRSIPMTVDFIRLKSYCNDQSTGDIKVIGGDDLSTLTGKNVLIVEDIIDTGKTMQTLLSLVRQYNPKMVKVASLLVKRTPRSVGYKPDFVGFEIPDKFVVGYALDYNEYFRDLNHVC');

	-- Associate the enzymes with the pathways
	INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00232','P05177');
	INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00232','P18440');
	INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00983','P00492');
	INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00983','P18440');
```
and then click on Execute SQL (play icon).	
Click on Write Changes to save the modifications to the database.

**Note**: Save your SQL statements in a file for future study. 
	
5. Try to associate a second sequence to enzyme `P18440` by running the SQL statement:
```sql
INSERT INTO enzyme (id, ???) VALUES ('P18440', 'AAAAAAA');
```
Why the SQL statement failed?

6. DELETE the sequence of enzyme `P18440` by running the SQL statement:
```sql
DELETE FROM enzyme WHERE ??? = 'P18440';
```

7. Insert the original sequence of enzyme `P18440` by running the SQL statement in step 4:

8. Modify the database schema so that the database can store the name of the enzymes and also their position within the pathway (a whole number):
```sql
ALTER TABLE enzyme ADD COLUMN name VARCHAR(255);
ALTER TABLE path_enzyme ADD COLUMN position INTEGER;
```

9. Update the values of the new columns created in the previous step:
```sql
UPDATE enzyme SET name = 'Cytochrome P450 1A2' WHERE ??? = 'P05177';
UPDATE enzyme SET name = 'Arylamine N-acetyltransferase 1' WHERE ??? = 'P18440';
UPDATE enzyme SET name = 'Hypoxanthine-guanine phosphoribosyltransferase' WHERE ??? = 'P00492';

UPDATE path_enzyme SET position = 1 WHERE enzyme_id = 'P05177' and ??? = 'hsa00232';
UPDATE path_enzyme SET position = 2 WHERE enzyme_id = 'P18440' and ??? = 'hsa00232';
UPDATE path_enzyme SET position = 1 WHERE enzyme_id = 'P18440' and ??? = 'hsa00983';
UPDATE path_enzyme SET position = 2 WHERE enzyme_id = 'P00492' and ??? = 'hsa00983';
```
Click on Browse Data to check the changes.
Click on `Write Changes` to save the database.



# Module 9 -- Create and query a database {#module9}

## Objectives:

- Design a simple database schema to store information of the pathways
- Use SQL statements to define and change the database structure or schema
- Use SQL statements to insert, update and delete data
- Use SQL statements to query data

## Input:

- None

## Output:

- Database file: `pathways.db`

## Steps:

1. Open your Personal Area on your computer and create a folder named `module9`.

2. Like in module 3, open the application [DB Browser for SQLite](http://sqlitebrowser.org/), and create a new database named `pathways.db` and save it in the previous folder.
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
Then click on `Execute SQL` (the play icon).
Explain why the primary key of the table `path_enzyme` has two atributes.
**Note**: Replace all the green question mark place-holders <span class="nobr">(`???`)</span> with appropriate SQL code.

4. Let's insert some data in these three tables.
We will only insert two pathways and three enzymes based on the contents of the files `sequences.csv` and `selected2.csv` created in previous modules.
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
    INSERT INTO enzyme (id, ???) VALUES ('P18440','MDIEAYLERIGYK');
    INSERT INTO enzyme (id, ???) VALUES ('P00492','MATRSPGVVISDDEPGYDLDLFCIPNHYAEDLERVFIPHGLIMDRTERLARDVMKEMGGHHIVALCVLKGGYKFFADLLDYIKALNRNSDRSIPMTVDFIRLKSYCNDQSTGDIKVIGGDDLSTLTGKNVLIVEDIIDTGKTMQTLLSLVRQYNPKMVKVASLLVKRTPRSVGYKPDFVGFEIPDKFVVGYALDYNEYFRDLNHVC');
    
    -- Associate the enzymes with the pathways
    INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00232','P05177');
    INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00232','P18440');
    INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00983','P00492');
    INSERT INTO path_enzyme (path_id, ???) VALUES ('hsa00983','P18440');
    ```
Then click on `Execute SQL` (play icon).
Click on `Write Changes` to save the modifications to the database.
**Note**: Save your SQL statements in a file for future study.

5. Imagine you detect an error in the data that has been added to the database.
In fact, the sequence of P18440 seems suspiciously short.
If you compare it with the one in the `sequences.csv` file, you will find that it is not correct.
Let's correct it

    a. Try to associate the correct sequence to enzyme `P18440` by running the SQL statement:
        ```sql
        INSERT INTO enzyme (id, ???) VALUES ('P18440', 'MDIEAYLERIGYKKSRNKLDLETLTDILQHQIRAVPFENLNIHCGDAMDLGLEAIFDQVVRRNRGGWCLQVNHLLYWALTTIGFETTMLGGYVYSTPAKKYSTGMIHLLLQVTIDGRNYIVDAGFGRSYQMWQPLELISGKDQPQVPCVFRLTEENGFWYLDQIRREQYIPNEEFLHSDLLEDSKYRKIYSFTLKPRTIEDFESMNT');
        ```
    Why has the SQL statement failed?

    b. Delete the sequence of enzyme `P18440` by running the SQL statement:
        ```sql
        DELETE FROM enzyme WHERE ??? = 'P18440';
        ```

    c. Insert the original sequence of enzyme `P18440` by running again the SQL statement in step 5a.

6. Now suppose you decide that you need to store more information about the pathways: namely, we want the names of the enzymes and their position in the pathways they participate.

    a. Modify the database schema so that the database can store the name of the enzymes and also their position within the pathway (a whole number):
        ```sql
        ALTER TABLE enzyme ADD COLUMN name VARCHAR(255);
        ALTER TABLE path_enzyme ADD COLUMN position INTEGER;
        ```

    b. Update the values of the new columns created in the previous step:
        ```sql
        UPDATE enzyme SET name = 'Cytochrome P450 1A2' WHERE ??? = 'P05177';
        UPDATE enzyme SET name = 'Arylamine N-acetyltransferase 1' WHERE ??? = 'P18440';
        UPDATE enzyme SET name = 'Hypoxanthine-guanine phosphoribosyltransferase' WHERE ??? = 'P00492';
        
        UPDATE path_enzyme SET position = 1 WHERE enzyme_id = 'P05177' and ??? = 'hsa00232';
        UPDATE path_enzyme SET position = 2 WHERE enzyme_id = 'P18440' and ??? = 'hsa00232';
        UPDATE path_enzyme SET position = 1 WHERE enzyme_id = 'P18440' and ??? = 'hsa00983';
        UPDATE path_enzyme SET position = 2 WHERE enzyme_id = 'P00492' and ??? = 'hsa00983';
        ```
    
    c. Click on `Browse Data` to check the changes.

7. Write a SQL query that selects the name of the enzymes whose id starts with `P0`.
Click on `Execute SQL` and write:
    ```sql
    SELECT ??? FROM enzyme WHERE ??? LIKE "P0%";
    ```
and then click on `Execute SQL` (play icon).

8. Write an SQL query that associates the enzyme sequences with the name of each pathway:
    ```sql
    SELECT path.???, enzyme.???
    FROM path, enzyme, path_enzyme
    WHERE path.id = path_enzyme.path_id AND
          enzyme.id = path_enzyme.enzyme_id;
    ```
Observe the output that should be composed of 4 rows.
**Note**: You can save the results in CSV by using the button next to the output window.

9. Remove from the previous SQL query the WHERE clause, and run it:
    ```sql
    SELECT path.???, enzyme.???
    FROM path, enzyme, path_enzyme
    ```
Why does the output have now 24 rows?

10. Write a SQL query that selects the id and name of the pathways associated with at least 2 enzymes whose sequence contains a glutamic acid `E` followed by a alanine `A`:
    ```sql
    SELECT path.id, path.name
    FROM path, enzyme, path_enzyme
    WHERE path.id = path_enzyme.path_id AND
          enzyme.id = path_enzyme.enzyme_id AND
          enzyme.sequence LIKE "%EA%"
    GROUP BY path.id
    HAVING COUNT(enzyme.id) >= ???
    ```
Observe the output and try to understand why only the pathway `hsa00232` is shown.

11. Click on `Write Changes` to save the database.

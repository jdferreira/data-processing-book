# Module 3 -- Relational databases {#module3}

## Objectives:

-  Store data in an SQLite database.

## Input:

- File: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - created in the module 2

## Output:
- File: `database_metabolic_pathways.db`
- File: `database_metabolic_pathways.db.sql`

## Steps:

1. Open your Personal Area on your computer and create a folder named `module3`.

2. Save the file `metabolic_pathways.csv` given as input in the previous folder.

3. Open the application [DB Browser for SQLite](http://sqlitebrowser.org/).
**Note**: There is a portable version available for download that can be used without installation.

4. Create a new database named `database_metabolic_pathways.db` and save it in the previous folder.
Click Cancel when asked for `Edit table definition`.

5. Click on `File`, then on `Import`, and finally on `Table from CSV file...`.
Select the `metabolic_pathways.csv` and click Open.
Make sure that the checkbox "Column names in first line" is selected and that the "Field separator" and "Quote separator" characters are correct (a comma `,` and a double quote `"` respectively). See the picture below if necessary.

    ![Table metabolic_pathways](images/table_metabolic_pathways.png "Table metabolic_pathways")

6. Click OK twice to import the table.

7. Click on `Browse Data` and check how many rows the table `metabolic_pathways`.

8. Click on `Execute SQL` and write:
    ```sql
    CREATE TABLE my_pathways (
        id TEXT,
        name TEXT
    )
    ```
and then click on Execute SQL (play icon).

9. Insert one metabolic pathway in the table:

    a. Click on `Browse Data`, select the table `metabolic_pathways` and find the identifier (the id) and name of your favorite pathway.
    b. Next, select the table `my_pathways` and click on `New Record` and replace `NULL` by the id and name of your favorite pathway.
    c. Click on `Write Changes` to save the database.

10. Click on `File`, then on `Export`, and finally on `Database to SQL file...`.
Make sure that you select all the tables in your database (click the `Select All` button) and click `OK`.
Save the file as `database_metabolic_pathways.db.sql` in the previous folder.

11. Open the file `database_metabolic_pathways.db.sql` in a text editor (Notepad) and check how each pathway is now being stored.

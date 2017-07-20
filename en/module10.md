# Module 10 -- Query a database {#module10}

## Objectives:
- Use SQL statements to query data

## Input:
- File: [pathways.db](files/pathways.db)
    - created in module 9

## Output:
- None

## Steps:

1. Open your Personal Area on your computer and create a folder named module10,
and save the file `pathways.db` in that folder. 

2. Like in module 9 open the application [DB Browser for SQLite](http://sqlitebrowser.org/),
and open the database `pathways.db`. 

3. Write a SQL query that selects the name of the enzymes whose id starts with `P0`.
Click on `Execute SQL` and write:
```sql
    SELECT ??? FROM enzyme WHERE ??? LIKE "P0%";
```
and then click on Execute SQL (play icon).

**Note**: Replace all the green question mark place-holders (`???`) with appropriate SQL code.

4. Write a SQL query that associates the enzyme sequences with the name of each pathway:
```sql
    SELECT path.???, enzyme.???
    FROM path, enzyme, path_enzyme
    WHERE path.id = path_enzyme.path_id
      AND enzyme.id = path_enzyme.enzyme_id;
```
Observe the output that should be composed of 4 rows.

**Note**: You can save the results in CSV by using the button next to the output window.

5. Remove from the previous SQL query the WHERE clause, and run it:
```sql
    SELECT path.???, enzyme.???
    FROM path, enzyme, path_enzyme
```
Why the output has now 24 rows?

6. Write a SQL query that selects the id and name of the pathways associated with at least 2 enzymes whose sequence contains a glutamic acid `E` followed by a alanine `A`:
```sql
    SELECT path.id, path.name
    FROM path, enzyme, path_enzyme
    WHERE path.id = path_enzyme.path_id
    AND enzyme.id = path_enzyme.enzyme_id
	AND enzyme.sequence LIKE "%EA%"
    GROUP BY path_id
	HAVING COUNT(enzyme_id) >= ???
```
Observe the output and try to understand why only the pathway `hsa00232` is shown. 
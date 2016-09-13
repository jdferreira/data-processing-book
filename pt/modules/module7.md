# Módulo 7 -- Inserção de dados CSV {#module7}

## Objetivos:
- Copiar dados de CSV para a base de dados
- Consultar os dados com critérios de seleção complexos

## Input:
- Ficheiro: [selected2.csv](files/selected2.csv)
    - criado no módulo 3
- Ficheiro: [sequences.csv](files/sequences.csv)
    - criado no módulo 3
- Ficheiro: [pathways.db](files/pathways.db)
    - criado no módulo 6

## Output:
- Ficheiro: `results_1.csv`
- Ficheiro: `results_2.csv`
- Ficheiro: `results_3.csv`
- Ficheiro: `results_4.csv`

## Passos:

1. Crie um novo _script_ Python `module7.py` que abre a base de dados criada no módulo anterior e remove as linhas das tabelas.
```python
    import sqlite3
    
    connection = sqlite3.connect('pathways.db')
    
    # Erase all data from the three tables
    connection.execute('DELETE FROM path_enzyme')
    connection.execute('DELETE FROM paths')
    connection.execute('DELETE FROM enzymes')
    
    # Save the deletions
    connection.commit()
```

2. Adicione o código seguinte ao _script_, o qual lê os dados de cada via  metabólica e adicionam-nos à base de dados.
```python
    import csv
    
    # Read the pathways from the file from module 3
    f = open('selected2.csv')
    paths = csv.reader(f, delimiter=???)
    
    # For each pathway, insert its information into the database
    for path in paths:
        # Extract the pathway information from the `path` variable
        path_id = path[0]
        path_name = ???
        path_class = ???
        
        # Insert into the database using the `?` notation
        connection.execute('''
            INSERT INTO paths (id, name, class)
            VALUES (?, ?, ?)
        ''', (path_id, path_name, path_class))
        
    # Save the changes
    connection.commit()
```

3. Vamos fazer o mesmo com as enzimas:
```python
    # Now do the same for the enzymes
    f = open('sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    enzymes_inserted = [] # Keep a list of the enzymes already inserted
    
    for enzyme in enzymes:
        enzyme_id = ???
        enzyme_sequence = ???
        
        # Check to see if the enzyme has been added before
        if enzyme_id not in enzymes_inserted:
            connection.execute('''
                INSERT INTO enzymes (id, sequence)
                VALUES (?, ?)
            ''', (enzyme_id, enzyme_sequence))
            
            # Add this enzyme to the list of enzymes already inserted
            enzymes_inserted.append(enzyme_id)
    
    # Save the changes
    connection.commit()
```

4. E agora vamos inserir na base de dados a informação que associa cada via às suas enzimas:
```python
    # Which file do we need to read in order to relate pathways with enzymes?
    f = open(???)
    
    paths =  csv.reader(f, delimiter=???)
    
    for path in paths:
        path_id = path[0]
        enzyme_list = path[3].split('|')
        
        # For each enzyme, we need to add one line to the `path_enzyme` table
        for enzyme_id in enzyme_list:
            connection.execute('''
                INSERT INTO path_enzyme (path_id, enzyme_id)
                VALUES (?, ?)
            ''', (path_id, enzyme_id))
    
    connection.commit()
```

5. Com um comando SQL, consulte os dados das vias metabólicas e imprima o identificar e o nome no terminal:
```python
    rows = connection.execute('SELECT ??? FROM ???')
    
    # For each selected pathway, print the id and the name of the pathway
    for row in rows:
        path_id = row[???]
        path_name = row[???]
        
        print 'Path ' + path_id + ' is named "' + path_name + '"'
```

6. Verifique que o output é
```text
    Path hsa00730 is named "Thiamine metabolism"
    Path hsa04122 is named "Sulfur relay system"
```

7. O código anterior imprime a informação no terminal.
Agora queremos gravar essa mesma informação no ficheiro CSV `results_1.csv`.
Substitua o código do passo 5 por isto:
```python
    # Let's open file 'results_1.csv' in write mode
    f = open(???, ???)
    w = csv.writer(f, delimiter=???)
    
    rows = connection.execute('SELECT ??? FROM ???')
    
    # For each selected pathway, save it to the file
    for row in rows:
        w.writerow(row)
```

8. Selecione agora as enzimas cujo identificar começa com Q e grave-as no ficheiro `results_2.csv`.
A receita é a mesma, apenas mudando o nome do ficheiro e o comando de consulta.
Pode usar a seguinte consulta, substituindo onde for apropriado:
```sql
    SELECT ??? FROM enzymes WHERE ??? LIKE "Q%"
```

9. Agora vamos cruzar informação de várias tabelas.
Duplique e adapte o código do passo anterior, usando o seguinte comando SQL para selecionar as sequências das enzimas de cada via metabólica, e grave o resultado no ficheiro `results_3.csv`:
```sql
    SELECT paths.name, enzymes.???
    FROM paths, enzymes, path_enzyme
    WHERE paths.id = path_enzyme.path_id
      AND enzymes.id = path_enzyme.enzyme_id
```

10. SQL permite consultas mais complexas.
Use a consulta seguinte para gravar o identificador e o nome das vias metabólicas associadas a pelo menos 15 enzimas.
Grave o resultado no ficheiro `results_4.csv`.
```sql
    SELECT paths.id, paths.name
    FROM paths, path_enzymes
    GROUP BY path_id HAVING COUNT(*) >= 15
```

## Após a aula:

1. Determine a razão para usar uma lista `enzymes_inserted` no passo 3.<br>
**Dica**: tente remover o uso da lista, execute o _script_ e observe que o código falha com uma exceção `constraint failed`.

2. Muitos dos passos deste módulo consistem em código repetido.
    
    a. Crie uma função `run_sql` que aceita dois argumentos: um comando SQL e o nome de um ficheiro.
    
    b. A implementação desta função deve executar o comando SQL fornecido e gravar o resultado obtido num ficheiro CSV.
    
    c. Altere o código deste módulo de forma a que use a função `run_sql` em vez de repetir código.
    **Dica**: Os passos 7 a 10 serão simplesmente a chamada à função.

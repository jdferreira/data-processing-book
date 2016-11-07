# Módulo 7 -- Inserção de dados CSV {#module7}

## Objetivos:
- Copiar dados de CSV para a base de dados
- Consultar os dados com critérios de seleção complexos

## Input:
- Ficheiro: [metabolic_pathways.csv](files/metabolic_pathways.csv)
    - criado no módulo 1
- Ficheiro: [all_sequences.csv](files/all_sequences.csv)
    - semelhante ao ficheiro `sequences.csv` do módulo 3, mas com a sequências de todas as enzimas.
    Veja a questão 2 da secção **Após a aula** do módulo 3.
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
    
    # Remove todos os dados inseridos nas tabelas
    connection.execute('DELETE FROM path_enzyme')
    connection.execute('DELETE FROM path')
    connection.execute('DELETE FROM enzyme')
    
    # Grava a base de dados
    connection.commit()
```

2. Adicione o código seguinte ao _script_, o qual lê os dados de cada via  metabólica e adicionam-nos à base de dados.
```python
    import csv
    
    # Le as vias selecionadas no modulo 3
    f = open('metabolic_pathways.csv')
    paths = csv.reader(f, delimiter=???)
    
    # Para cada via, insere a sua informacao na base de dados
    for path in paths:
        # Extrai a informacao da via presente na variavel `path`
        path_id = path[0]
        path_name = ???
        path_class = ???
        
        # Insere a informacao na base de dados
        # Note que usamos um comando generico usando a notacao `?`
        # e fornecemos os parametros atraves de um tuplo
        connection.execute('''
            INSERT INTO path (id, name, class)
            VALUES (?, ?, ?)
        ''', (path_id, path_name, path_class))
    
    # Grava
    connection.commit()
```

3. Vamos fazer o mesmo com as enzimas:
```python
    # Agora fazemos o mesmo para as enzimas
    f = open('all_sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    enzymes_inserted = [] # Lista com as enzimas ja inseridas
    
    for enzyme in enzymes:
        enzyme_id = ???
        enzyme_sequence = ???
        
        # Determina se a enzima ja foi inserida anteriormente
        if enzyme_id not in enzymes_inserted:
            connection.execute('''
                INSERT INTO enzyme (id, sequence)
                VALUES (?, ?)
            ''', (enzyme_id, enzyme_sequence))
            
            # Adiciona esta enzima a lista de enzimas ja inseridas
            enzymes_inserted.append(enzyme_id)
    
    # Grava
    connection.commit()
```

4. E agora vamos inserir na base de dados a informação que associa cada via às suas enzimas:
```python
    # Que ficheiro precisamos de ler para relacionar vias e enzimas?
    f = open(???)
    
    paths =  csv.reader(f, delimiter=???)
    
    for path in paths:
        path_id = path[0]
        enzyme_list = path[3].split('|')
        
        # Para cada enzima, precisamos de inserir uma linha
        # na tabela `path_enzyme`
        for enzyme_id in enzyme_list:
            connection.execute('''
                INSERT INTO path_enzyme (path_id, enzyme_id)
                VALUES (?, ?)
            ''', (path_id, enzyme_id))
    
    connection.commit()
```

5. Com um comando SQL, consulte os dados das vias metabólicas e imprima o identificador e o nome no terminal:
```python
    rows = connection.execute('SELECT ??? FROM ???')
    
    # Para cada via, imprime o identificador e o nome
    for row in rows:
        path_id = row[???]
        path_name = row[???]
        
        print 'Path ' + path_id + ' is named "' + path_name + '"'
```

6. Verifique que o output é
```text
    Path hsa00010 is named "Glycolysis / Gluconeogenesis"
    Path hsa00020 is named "Citrate cycle (TCA cycle)"
    Path hsa00030 is named "Pentose phosphate pathway"
    Path hsa00040 is named "Pentose and glucuronate interconversions"
    Path hsa00051 is named "Fructose and mannose metabolism"
    ...
```

7. O código anterior imprime a informação no terminal.
Agora queremos gravar essa mesma informação no ficheiro CSV `results_1.csv`.
Substitua o código do passo 5 por isto:
```python
    # Abre o ficheiro `results_1.csv` em modo de escrita (write mode)
    f = open(???, ???)
    w = csv.writer(f, delimiter=???)
    
    rows = connection.execute('SELECT ??? FROM ???')
    
    # Escreve a informacao de cada via no ficheiro CSV
    for row in rows:
        w.writerow(row)
    
    f.close()
```

8. Selecione agora as enzimas cujo identificador começa com Q e grave-as no ficheiro `results_2.csv`.
A receita é a mesma, apenas mudando o nome do ficheiro e o comando de consulta.
Pode usar a seguinte consulta, substituindo onde for apropriado:
```sql
    SELECT ??? FROM enzyme WHERE ??? LIKE "Q%"
```

9. Agora vamos cruzar informação de várias tabelas.
Duplique e adapte o código do passo anterior, usando o seguinte comando SQL para selecionar as sequências das enzimas de cada via metabólica, e grave o resultado no ficheiro `results_3.csv`:
```sql
    SELECT path.name, enzyme.???
    FROM path, enzyme, path_enzyme
    WHERE path.id = path_enzyme.path_id
      AND enzyme.id = path_enzyme.enzyme_id
```

10. SQL permite consultas mais complexas.
Use a consulta seguinte para gravar o identificador e o nome das vias metabólicas associadas a pelo menos 300 enzimas.
Grave o resultado no ficheiro `results_4.csv`.
```sql
    SELECT path.id, path.name
    FROM path, path_enzyme
    WHERE path.id = path_enzyme.path_id
    GROUP BY path_id HAVING COUNT(*) >= 300
```

## Após a aula:

1. Determine a razão para usar uma lista `enzymes_inserted` no passo 3.<br>
**Dica**: tente remover o uso da lista, execute o _script_ e observe que o código falha com uma exceção `constraint failed`.

2. Muitos dos passos deste módulo consistem em código repetido.
    
    a. Crie uma função `run_sql` que aceita dois argumentos: um comando SQL e o nome de um ficheiro.
    
    b. A implementação desta função deve executar o comando SQL fornecido e gravar o resultado obtido num ficheiro CSV.
    
    c. Altere o código deste módulo de forma a que use a função `run_sql` em vez de repetir código.<br>
    **Dica**: Os passos 7 a 10 serão simplesmente a chamada à função.

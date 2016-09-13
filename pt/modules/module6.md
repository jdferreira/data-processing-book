# Módulo 6 -- Criar uma base de dados SQL {#module6}

## Parte I: Um pequeno exemplo para começar

### Objetivos:
- Criar uma base de dados SQLite usando Python
- Inserir e consultar dados na base de dados

### Input:
- Nenhum

### Output:
- Ficheiro da base de dados: `example.db`

### Passos:

1. Primeiro crie uma base de dados vazia usando Python.
Dê a este _script_ o nome de <nobr>`example.py`.</nobr>
```python
    # `sqlite3` is a package that can be used to create a file containing
    # a relational database. We use this package to create the database,
    # insert data in it and query the data.
    
    import sqlite3
    
    # To access a database, we need to connect to it. If the file does not
    # exist, one will be created
    connection = sqlite3.connect('example.db')
```

2. Agora que temos uma base de dados vazia, vamos adicionar tabelas e algumas linhas.
Adicione o seguinte código ao seu _script_:
```python
    # We can now emit SQL commands to the opened database
    
    # First create a table to store student information
    connection.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    
    # Then add information to that table
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (1, 'Alice', 20)
    ''')
    
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (2, 'Brock', 21)
    ''')
    
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (3, 'Chuck', 19)
    ''')
    
    # You can also insert data that is stored in variables
    student_id = 4
    student_name = 'Doris'
    student_age = 19
    connection.execute('''
        INSERT INTO students (id, name, age)
        VALUES (?, ?, ?)
    ''', (student_id, student_name, student_age))
    
    # Ensure that the data is saved
    connection.commit()
```

3. Finalmente, vamos certificar-nos que a base de dados contém a informação inserida:
```python
    # We can also emit SELECT commands which will return data back to Python
    
    rows = connection.execute('SELECT id, name, age FROM students')
    
    for row in rows:
        student_id = row[0]
        student_name = row[1]
        student_age = row[2]
        
        msg = student_name + ' is ' + str(student_age) + ' years old'
        msg = msg + ' and has id #' + str(student_id)
        
        print msg
```

4. Verifique que este é o output produzido.
```text
    Alice is 20 years old and has id #1
    Brock is 21 years old and has id #2
    Chuck is 19 years old and has id #3
    Doris is 19 years old and has id #4
```

## Part II: Agora com dados reais

## Objetivos:
- Desenhar um esquema de base de dados simples para guardar informação de vias metabólicas
- Usar chaves estrangeiras

## Input:
- Nenhum

## Output:
- Ficheiro de base de dados: `pathways.db`

## Passos:

1. AGora que já sabe criar uma base de dados e criar as suas tabelas, vamos começar uma nova base de dados no ficheiro `pathways.db` com três tabelas.
Primeiro, crie um _script_ `module6.py` com o seguinte código:
```python
    import sqlite3
    
    connection = sqlite3.connect('pathways.db')
    
    # Let's create the three tables.
    
    # This contains information about the pathway
    connection.execute('''
        CREATE TABLE path (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            class VARCHAR(255) NOT NULL
        )
    ''')
    
    # This contains information about the enzymes
    connection.execute('''
        CREATE TABLE enzyme (
            id VARCHAR(255) PRIMARY KEY,
            sequence TEXT NOT NULL
        )
    ''')
    
    # This associates each pathway with its enzymes
    connection.execute('''
        CREATE TABLE path_enzyme (
            path_id VARCHAR(255),
            enzyme_id VARCHAR(255),
            PRIMARY KEY (path_id, enzyme_id),
            FOREIGN KEY (path_id) REFERENCES path (id),
            FOREIGN KEY (enzyme_id) REFERENCES enzyme (id)
        )
    ''')
```

2. Agora vamos inserir os dados nestas três tabelas.
Como exemplo, vamos inserir apenas uma via e duas enzimas dessa via.
Se necessário, consulte os ficheiros criados nos módulos anteriores para encontrar o nome da via `hsa00730` e as enzimas que fazem parte dela.
```python
    connection.execute('''
        INSERT INTO path (id, name, class)
        VALUES ('hsa00730', '???', '???');
    ''')
    
    connection.execute('''
        INSERT INTO enzyme (id, sequence)
        VALUES ('Q53FP3','???');
    ''')
    
    connection.execute('''
        INSERT INTO enzyme (id, sequence)
        VALUES ('???','???');
    ''')
    
    connection.execute('''
        INSERT INTO path_enzyme (path_id, enzyme_id)
        VALUES ('hsa00730','???');
    ''')
    
    connection.execute('''
        INSERT INTO path_enzyme (path_id, enzyme_id)
        VALUES ('???','???');
    ''')
    
    # Ensure that the data is saved
    connection.commit()
```

3. Por fim, vamos assegurar-nos que as tabelas contêm os dados que lá colocámos.
Para tal, como exemplo, vamos selecionar as enzimas de cada via.
```python
    rows = connection.execute('SELECT id, sequence FROM enzymes')
    for row in rows:
        enzyme_id = row[0]
        enzyme_sequence = row[1]
        
        print enzyme_id + ' starts with ' + enzyme_sequence[:5]
```

4. Verifique que o output corresponde ao seguinte:
```text
    Q53FP3 starts with MLLRA
    Q9Y697 starts with MLLRA
```

5. Certifique-se de que mantém uma cópia do ficheiro `pathways.db` para si, assim como do _script_ `module6.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Verifique que a chave primária da tabela `path_enzyme` tem dois atributos e explique porquê.

2. Modifique o esquema da base de dados para que possa guardar também o nome de cada enzima e a sua posição na via metabólica (um número inteiro).

3. Altere o código do passo 3 para que verifique também o conteúdo das tabelas `paths` e `path_enzyme`.


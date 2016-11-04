# Módulo 4 -- Cruzamento de dados de várias fontes {#module4}

## Objetivos:
- Usar dicionários para associar informação
- Cruzar dados de diversas fontes

## Input:
- Ficheiro: [selected2.csv](files/selected2.csv)
    - criado no módulo 2
- Ficheiro: [sequences.csv](files/sequences.csv)
    - criado no módulo 3

## Output:
- Ficheiro: `paths_enzymes.csv`

## Passos:

1. Comece por criar um novo _script_ `module4.py` vazio.

2. Vamos primeiro ler o ficheiro `sequences.csv` para construir um dicionário onde cada enzima é associada à sua própria sequência.
Para tal, adicione ao _script_ o seguinte código, substituindo os pontos de interrogação:
```python
    import csv
    
    # Le o ficheiro CSV
    f = open('sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    # Cria um dicionario vazio onde vamos introduzir a informacao
    # proveniente do ficheiro CSV
    dict_sequences = {}
    
    # Para cada enzima no ficheiro, associa-a com a sua sequencia
    for enzyme in enzymes:
        enzyme_id = enzyme[???] # O identificador desta enzima
        seq = enzyme[???]       # A sequencia de aminoacidos da enzima
        dict_sequences[enzyme_id] = seq
```

3. Em seguida, vamos ler o ficheiro `selected2.csv` e associar a cada via uma lista das suas enzimas
Também aqui vamos usar um dicionário.
```python
    # Le o ficheiro CSV
    f = open('selected2.csv')
    paths = csv.reader(f, delimiter=???)
    
    # Cria um dicionario vazio onde vamos introduzir a informacao
    # proveniente do ficheiro CSV
    dict_paths = {}
    
    # Para cada via nesse ficheiro:
    # - extrai a lista de enzimas da via,
    # - associa a via com esta lista de enzimas
    for path in paths:
        path_id = path[???] # O identificador da via
        enzymes = path[???] # O campo com a lista de enzimas
        
        # Divide a string de enzimas numa lista
        enzyme_list = str.split(enzymes, ???)
        
        # Associa o identificador da via com a lista de enzimas
        dict_paths[???] = ???
```

4. Agora que temos os dois dicionários, podemos percorrer cada via e cada enzima de cada via de forma a criar um ficheiro CSV que cruza a informação, associando a cada via as sequências de aminoácidos das suas enzimas.
Para tal, adicione o seguinte ao seu _script_:
```python
    # Abre um ficheiro para gravar o output
    f = open('paths_enzymes.csv', 'wb')
    w = csv.writer(f, delimiter=???)
    
    # Para cada via e cada enzima que ela contem
    for path_id in dict_paths :
        # Vamos imprimir alguma informacao no ecra para
        # sabermos o que esta a acontecer
        print 'Processing pathway with ID ' + path_id
        
        # Seleciona a lista de enzimas associadas a esta via
        enzyme_list = dict_paths[???]
        
        # Agora que temos a lista de enzimas, associa a via com a cada uma
        # das sequencias de aminoacidos das suas enzimas
        for enzyme_id in enzyme_list:
            # Mais informacao de depuracao
            print '  enzyme = ' + enzyme_id
            
            # Seleciona a sequencia associada a esta enzima
            seq = dict_sequences[???]
            
            # Escreve esta informacao no ficheiro CSV
            w.writerow([path_id, seq])
    
    f.close()
```

5. Corra o código e estude o conteúdo do ficheiro que foi criado (`paths_enzymes.csv`).
Corresponde ao que estava à espera?

6. Certifique-se de que mantém uma cópia do ficheiro `paths_enzymes.csv` para si, assim como do _script_ `module4.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Altere o critério de seleção usado para criar o ficheiro `selected2.csv` (por exemplo selecionando as vias com um máximo de 10 enzimas, como proposto no módulo 2).
Em seguida altere o código de hoje para acomodar esta alteração.


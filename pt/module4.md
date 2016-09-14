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
    
    # Read the CSV file
    f = open('sequences.csv')
    enzymes = csv.reader(f, delimiter=???)
    
    # Create an empty dictionary that we will populate as we read the CSV
    # file
    dict_sequences = {}
    
    # For each of the enzymes in the file, associate the enzyme with its
    # sequence
    for enzyme in enzymes:
        enzyme_id = enzyme[???] # The ID of this enzyme
        seq = enzyme[???]       # The aminoacid sequence of this enzyme
        dict_sequences[enzyme_id] = seq
```

3. Em seguida, vamos ler o ficheiro `selected2.csv` e associar a cada via uma lista das suas enzimas
Também aqui vamos usar um dicionário.
```python
    # Read the CSV file
    f = open('selected2.csv')
    paths = csv.reader(f, delimiter=???)
    
    # Create an empty dictionary that we will populate as we read the CSV
    # file
    dict_paths = {}
    
    # For each pathway in that file:
    # - extract the list of enzymes in the pathway
    # - associate the pathway with this list of enzymes
    for path in paths:
        path_id = path[???] # The ID of the pathways
        enzymes = path[???] # The field of the enzymes
        
        # Break that information into a list
        enzyme_list = str.split(enzymes, ???)
        
        # Associate the pathway ID with the corresponding list of enzymes
        dict_paths[???] = ???
```

4. Agora que temos os dois dicionários, podemos percorrer cada via e cada enzima de cada via de forma a criar um ficheiro CSV que cruza a informação, associando a cada via as sequências de aminoácidos das suas enzimas.
Para tal, adicione o seguinte ao seu _script_:
```python
    # Open a file to save the output
    f = open('paths_enzymes.csv', 'w')
    w = csv.writer(f, delimiter=???)
    
    # For each pathway and each enzyme that it contains
    for path_id in dict_paths :
        # Let's print some debugging information
        print 'Processing pathway with ID ' + path_id
        
        # Retrieve the list of enzymes associated with this pathway
        enzyme_list = dict_paths[???]
        
        # Now that we have the list of enzymes, associate the pathway with each
        # aminoacid sequence
        for enzyme_id in enzyme_list:
            # Some more debugging information
            print '  enzyme = ' + enzyme_id
            
            # Retrieve the sequence associated with this enzyme
            seq = dict_sequences[???]
            
            # Write this row to the CSV file
            w.writerow([path_id, seq])
```

5. Corra o código e estude o conteúdo do ficheiro que foi criado (`paths_enzymes.csv`).
Corresponde ao que estava à espera?

6. Certifique-se de que mantém uma cópia do ficheiro `paths_enzymes.csv` para si, assim como do _script_ `module4.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Altere o critério de seleção usado para criar o ficheiro `selected2.csv` (por exemplo selecionando as vias com um máximo de 10 enzimas, como proposto no módulo 2).
Em seguida altere o código de hoje para acomodar esta alteração.


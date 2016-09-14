# Módulo 3 -- UniProt como serviço web {#module3}

## Objetivos:
- Reconhecer a importância das fontes de dados externas
- Usar um serviço web através de código Python
- Processar a informação proveniente de um serviço web

## Input:
- Ficheiro: [selected2.csv](files/selected2.csv)
    - criado no módulo anterior

## Output:
- Ficheiro: `sequences.csv`
    - contendo as sequências de aminoácidos de cada enzima

## Passos:

1. Abra o URL <http://www.uniprot.org/uniprot/P12345.fasta> no _browser_ e estude o formato FASTA.
Altere o identificador do link de `P12345` para outro à sua escolha e estude o seu conteúdo e quais as diferenças entre os dois.

2. Num _script_ Python chamado `module3.py`, crie uma função chamada `get_sequence` que recebe o identificador de uma proteína e devolve a sua sequência de aminoácidos.
Esta função:

    a. abre o URL mencionado acima,
    
    b. lê o conteúdo acessível por esse URL,
    
    c. extrai a sequência de aminoácidos, e
    
    d. junta todas as linhas numa só, de forma a devolver apenas uma _string_.
    ```python
        import urllib # Este módulo contém funções para ler URLs

        def get_sequence(identifier):
            # Estabelece o URL a abrir
            url = 'http://www.uniprot.org/uniprot/' + ??? + '.fasta'
            
            # Abre o URL
            f = urllib.urlopen(url)
            
            # Lê todas as linhas do URL  numa lista
            lines = f.readlines()
            
            # Ignora a primeira linha, que contém apenas metadados
            del lines[0]
            
            # Junta as linhas todas numa string única
            sequence = str.join("", lines)
            
            # Remove a terminação das linhas (o "enter" usado para começar
            # a linha seguinte)
            # Esta terminação é representada por `\n`
            sequence = str.replace(sequence, '\n', '')
            
            # Devolve a sequência
            return ???
    ```

3. Vamos experimentar executar a função com um pequeno número de proteínas.
Para tal, adicione as seguintes linhas ao _script_ Python, substituindo `???` pelos identificadores que quiser:
```python
    sequence1 = get_sequence('P12345')
    sequence2 = get_sequence('???')
    sequence3 = get_sequence('???')
    
    print "SEQUENCE 1:\n" + sequence1 + "\n"
    print "SEQUENCE 2:\n" + sequence2 + "\n"
    print "SEQUENCE 3:\n" + sequence3 + "\n"
```

4. Agora que já vimos como utilizar a função, vamos ler as enzimas do ficheiro `selected2.csv` e determinar as suas sequências de aminoácidos.
    
    a. Remova ou comente as linhas do passo 3.
    
    b. Substitua-as por:
    ```python
        import csv
        
        # Abre o output do módulo anterior
        f = open('selected2.csv')
        paths = csv.reader(f, delimiter=???)
        
        # Começa uma lista de enzimas vazia
        enzymes = []
        
        # Depois:
        # - lê a informação de cada via,
        # - extrai a lista de enzimas de cada via, e
        # - adiciona cada enzima à lista de enzimas
        for path in paths:
            enzymes_field = path[???] # O campo das enzimas
            
            # Divide as enzimas numa lista, tal como no módulo 2
            enzymes_in_this_path = str.split(enzymes_field, ???)
            
            # Adiciona acad uma à lista mestre de enzimas
            for e in enzymes_in_this_path:
                enzymes.append(e)
    ```

5. Agora que temos uma lista de enzimas, podemos usá-la juntamente com a função que criamos anteriormente para obter as suas sequências de aminoácidos.
Vamos gravar esta informação num novo ficheiro `sequences.csv`.
Para tal, continue a adicionar códugo ao _script_ `module3.py`:
```python
    f = open('sequences.csv', 'w')
    w = csv.writer(f, delimiter=???)
    
    for e in enzymes:
        seq = get_sequence(e)
        w.writerow([e, seq])
    
    f.close()
```

6. Execute o código e estude o conteúdo do novo ficheiro (`sequences.csv`).
Corresponde ao que esperava ver?

7. Certifique-se de que mantém uma cópia do ficheiro `sequences.csv` para si, assim como do _script_ `module3.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Verifique que no ficheiro `sequences.csv` algumas enzimas aparecem repetidas. Tente explicar porquê.

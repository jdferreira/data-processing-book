# Módulo 2 -- Seleção simples e guardar informação em disco {#module2}

## Objetivos:
- Transformar um critério de seleção em código Python
- Implementar o processo de seleção em Python
- Gravar os dados selecionados num novo ficheiro

## Input:
- Ficheiro: [metabolic_pathways.csv](files/metabolic_pathways.csv)

## Output:
- Ficheiro: `selected1.csv`
    * contendo os dados da via `hsa04210`.
- Ficheiro: `selected2.csv`
    * contendo os dados das vias `hsa00730` e `hsa04122`.

## Passos:

1. Vamos criar uma função Python que determine se o ID de uma via é `hsa04210`:

    a. Crie um ficheiro vazio e grave-o como `module2.py` na mesma pasta onde o ficheiro `metabolic_pathways.csv` está.
    Não se esqueça da terminação `.py`, pois esta indica ao computador que o ficheiro é um _script_ Python.
    
    b. Copie e cole o código seguinte para o ficheiro:
    ```python
        def filter1(path):
            path_id = path[???]  # Seleciona a coluna do identificar
            
            # Substitua '???' pelo identificador que estamos a procura
            if path_id == '???':
                return True
            else:
                return False
    ```
    
    c. Substitua os pontos de interrogração (`???`) por código Python apropriado.

2. O código do passo anterior define uma função que vai ser executada quando for chamada, mas por si só não faz nada.
Vamos adicionar mais código ao ficheiro para efetivamente usarmos a função em cada uma das vias metabólicas.
```python
    import csv
    
    # Abre o ficheiro original para ler todas as vias
    file_to_read = open('metabolic_pathways.csv')
    paths = csv.reader(file_to_read, delimiter=???)
    
    # Abre o ficheiro para gravar as vias selecionadas
    # O 'w' indica ao Python que queremos gravar neste ficheiro
    file_to_write = open('selected1.csv', 'w')
    w = csv.writer(file_to_write, delimiter=???)
    
    for path in paths:
        if filter1(path):
            w.writerow(path)
    
    # Fecha o ficheiro
    file_to_write.close()
```

3. Corra o _script_ `module2.py` e estude o novo ficheiro que foi criado.
Verifique que o seu conteúdo corresponde ao que esperava.

4. Edite o ficheiro `module2.py` criando agora uma nova função `filter2` que seleciona as vias onde a enzima Q9Y697 participa.
Se necessário, consulte a documentação para a função `str.split` em <https://docs.python.org/2/library/stdtypes.html#str.split>.
Vamos implementar esta funcionalidade em dois passos:

    a. Crie a nova função `filter2`:
    ```python
        def filter2(path):
            field = path[???] # Seleciona a coluna com a lista de enzymas
            
            # Divide as enzimas numa lista
            enzyme_list = str.split(field, ???)
            
            # `enzyme_list` e agora uma lista de strings, como por exemplo:
            # ['H9EC08', 'P03905', 'G9LG04', 'P03901']
            
            # Devolve `True` se a enzima escolhida estiver nessa lista
            if '???' in enzyme_list:
                return True
            else:
                return False
    ```
    
    b. Altere `'selected1.csv'` para `'selected2.csv'`.
    Esta modifação é essencial para que o novo ficheiro produzido não substitua o que já existe.

5. Corra o `module2.py` outra vez e estude o ficheiro que foi produzido.
Verifique que o seu conteúdo corresponde ao que esperava: em particular, assegure-se que a enzima Q9Y697 pertence a todas as vias selecionadas.

6. Certifique-se de que mantém uma cópia dos ficheiros `selected1.csv` e `selected2.csv` para si, assim como do _script_ `module2.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Crie uma terceira função `filter3` que seleciona as vias que fazem parte da classe "Human Diseases; Cancers".

2. Usando a função pré-existente `len`, que devolve o número de elementos numa lista, crie a função `filter4` que seleciona as vias que contêm no máximo 10 enzimas.
A documentação para esta função pode ser encontrada em <https://docs.python.org/2/library/functions.html#len>

**Nota**: para ler e escrever ficheiros CSV em Python, usámos (e vamos usar mais vezes) o módulo `csv`.
Este módulo permite especificar o formato do ficheiro a ler e escrever, _e.g._ qual o caracter a usar para separar os campos e para os delimitar.
Deve familiarizar-se com este módulo por si mesmo lendo a documentação em <https://docs.python.org/2/library/csv.html>.



# Módulo 5 -- Seleção de informação com expressões regulares {#module5}

## Objetivos:
- Desenhar expressões regular para representar vários critérios de seleção
- Usar o módulo `re` para criar e utilizar expressões regular
- Procurar por motivos de aminoácidos nas sequências das enzimas

## Input:
- Ficheiro: [sequences.csv](files/sequences.csv)
    - criado no módulo 3

## Output:
- Ficheiro: `relevant_sequences_1.csv`
- Ficheiro: `relevant_sequences_2.csv`
- Ficheiro: `relevant_sequences_3.csv`

## Passos:

1. Neste módulo, vamos usar expressões regulares para procurar enzimas cujas sequências de aminoácidos satisfazem certos padrões.
    
    a. Consulte a [folha de mnemónicas de expressões regulares](http://www.cheat-sheets.org/saved-copy/regular_expressions_cheat_sheet.png).
    
    b. Pode ainda encontrar a correspondência entre cada aminoácido e a seu código de 1 letra [neste quadro](http://bio100.class.uic.edu/lectures/aminoacids01.jpg).
    
    c. Familiarize-se com estes dois quadros.

2. Começamos por ler o conteúdo do ficheiro `sequences.csv` e por criar um dicionário que associa as enzimas às suas sequências de aminoácidos, tal como fizemos no módulo anterior.
Crie o _script_ `module5.py`:
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

3. Agora que temos o dicionário, vamos procurar as enzimas cujas sequências contêm três alaninas consecutivas:
```python
    # We import the re module to handle regular expressions
    import re
    
    # Define here your regular expression
    reg_expr = r'???'
    
    # For each enzyme, retrieve their sequence and determine whether
    # the sequence matches three consecutive alanines
    for enzyme in dict_sequences:
        # Retrieve the aminoacid sequence
        seq = ???
        
        # Determine whether the sequence matches the pattern
        if re.search(reg_expr, seq):
            print 'The enzyme ' + ??? + ' matches the expression ' + reg_expr
```

4. Modifique o código acima para gravar os identificadores e sequências de aminoácidos num ficheiro `relevant_sequences_1.csv`, em vez de escrever no ecrã.
Refira-se ao módulo 3, passo 5 se necessitar de se relembrar de como escrever um ficheiro CSV.

5. Altere a expressão regular no _script_ para encontrar outros padrões.
Para cada um destes padrões, grave os identificadores e sequências no ficheiro `relevant_sequences_2.csv` e `relevant_sequences_3.csv` respetivamente.
    
    a. Sequências onde os primeiros 5 aminoácidos são não-polares.
    
    b. Sequências que contêm uma metionina, seguida de qualquer aminoácido, seguida de uma serina ou uma prolina.

6. Execute o código e estude os ficheiros criados.
Correspondem ao que esperava ver?

7. Certifique-se de que mantém uma cópia dos ficheiros `relevant_sequences_1.csv`, `relevant_sequences_2.csv` e `relevant_sequences_3.csv` para si, assim como do _script_ `module5.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Escreva uma expressão regular alternativa à definida no passo 1, mantendo o significado mas usando elementos de expressões regulares diferentes.

2. Imagine que quer aplicar a primeira expressão regular usada neste módulo (3 alaninas consecutivas) ao ficheiro `relevant_sequences_2.csv` em vez de `sequences.csv`.
Altere o _script_ Python para acomodar estas alterações.
Verifique se o resultado é igual ao que tinha obtido no ficheiro `relevant_sequences_1.csv`.

**Nota**: Para os alunos que queiram explorar expressões regulares em mais detalhe, propomos o seguinte exercício:<br>
Qual a expressão regular que descreve um grupo de ligação ao GTP?
Este é um grupo complexo que consiste em três sub-sequências:

- a primeira é `GXXXXGK`,
- a segunda é `DXXG`, e
- a terceira é `NKXD` ou `NKXW`.

Entre o primeiro e o segundo grupos existem 40 a 80 aminoácidos ou 130 a 170 aminoácidos; entre o segundo e o terceiro grupo existem entre 40 a 80 aminoácidos.
<small>[Fonte: Dever TE, Glynias MJ, Merrick WC (1987). PNAS 84(7), 1814-1818.]</small>

# Módulo 1 -- Dados de vias metabólicas {#module1}

## Parte I: Notepad++ e Python

### Objetivos:

- Abrir o Notepad++, escrever algum código Python e gravar o ficheiro
- Executar o código com o interpretador Python

### Passos:

1. No menu iniciar do Windows, abra o `Notepad++`.

![Abrir o Notepad++](images/open-notepad.png "Abrir o Notepad++")

2. Escreva um pequeno programa "Hello World" e grave o ficheiro no Ambiente de Trabalho (ou em qualquer outra pasta que quiser) com o nome `test.py`.

![O programa \"Hello World\"](images/hello-world.png "O programa \"Hello World\"")

3. No menu iniciar, abra a linha de comandos (`cmd`).

![Abrindo a linha de comandos](images/open-cmd.png "Abrindo a linha de comandos")

4. No terminal (a janela com a linha de comandos), precisamos de navegar para o Ambiente de Trabalho e depois instruir o interpretador Python a executar o ficheiro `test.py`.
Para tal, escreva e execute os seguintes comandos no terminal:
```bash
    cd Desktop
    python test.py
```
![O output do programa \"Hello World\"](images/hello-world-run.png "O output do programa \"Hello World\"")

5. Observe o output produzido pelo Python e confirme que o terminal mostra o seguinte:
```text
    Hello World!
```

## Part II: Iniciando o processamento de dados

### Objetivos:
- Compreender o formato CSV
- Converter um ficheiro Excel no formato CSV
- Compreender o significado de metadados
- Ler ficheiros CSV com Python

### Input:
- Ficheiro: [metabolic_pathways.xls](files/metabolic_pathways.xls)

### Output:
- Ficheiro: `metabolic_pathways.csv`
- Terminal:
```text
    Glycolysis / Gluconeogenesis
    Citrate cycle (TCA cycle)
    Pentose phosphate pathway
    Pentose and glucuronate interconversions
    ...
```

### Passos:

1. Abra o ficheiro Excel.
Tome especial atenção ao conteúdo deste ficheiro e familiarize-se com os dados que contém.
Este passo é de grande importância em processamento de dados, pois permite-nos ganhar intuição sobre a informação com que estamos a lidar.

2. Remova a primeira linha, que contém os cabeçalhos das colunas.
(Esta primeira linha é classificada como "metadados" uma vez que fornece informação acerca dos dados no ficheiro mas não contém, por si mesma, dados.)

3. Usando as funcionalidades do Excel, grave os dados no formato CSV usando o nome `metabolic_pathways.csv`.

4. Abra o ficheiro CSV num editor de texto (`Notepad++`) e estude o conteúdo do novo ficheiro.
Por exemplo, determine qual caracter é usado para separar os vários campos, se os campos estão delimitados e como, _etc_.

5. Vamos criar um _script_ Python para ler o ficheiro CSV e imprimir o nome de cada via.
    
    a. Crie um ficheiro vazio e grave-o como `module1.py` na mesma pasta onde está o ficheiro `metabolic_pathways.csv`.
    Não esqueça a terminação `.py`, pois esta indica ao computador que o ficheiro é um _script_ Python.
    
    b. Copie e cole o código seguinte para o seu ficheiro:
    ```python
        import csv
        
        f = open('metabolic_pathways.csv')   # Open the file
        
        paths = csv.reader(f, delimiter=???) # Create a CSV reader object
        
        for path in paths: # For each pathway ...
            print ???      # ... print its name
    ```
    
    c. Substitua todos os pontos de interrogação (`???`) por código Python apropriado.

6. Corra o `module1.py` no terminal e observe o output.
O output corresponde ao que estava à espera de ver?

7. Certifique-se de que mantém uma cópia do ficheiro `metabolic_pathways.csv` para si, assim como do _script_ `module1.py`, de forma a que os possa usar nos próximos módulos.
Por exemplo, envie-os para si por email ou faça o upload para a Dropbox.

## Após a aula:

1. Altere o código Python para imprimir não o nome das vias mas a sua classe.

2. Explique a razão pela qual alguns campos no ficheiro CSV estão delimitados por aspas <nobr>(`"`)</nobr> e outros não.

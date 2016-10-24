% Processamento de dados de vias metabólicas usando ficheiros, serviços web e bases de dados
% João D. Ferreira; Francisco M. Couto
% Faculdade de Ciências da Universidade de Lisboa<br>Versão de 2016

<div id="license">
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
![](images/cc-88x31.png "Creative Commons License")
</a>
Este documento está protegido pela licença<br>
[Creative Commons - Atribuição 4.0 Internacional](http://creativecommons.org/licenses/by/4.0/)
</div>

# Índice

- [Introdução](#introduction)
- [Módulo 1 -- Dados de vias metabólicas](#module1)
- [Módulo 2 -- Seleção simples e guardar informação em disco](#module2)
- [Módulo 3 -- UniProt como serviço web](#module3)
- [Módulo 4 -- Cruzamento de dados de várias fontes](#module4)
- [Módulo 5 -- Seleção de informação com expressões regulares](#module5)
- [Módulo 6 -- Criar uma base de dados SQL](#module6)
- [Módulo 7 -- Inserção de dados CSV](#module7)


# Introdução {#introduction}

O objetivo destes exercícios é munir os alunos com a capacidade e a competência para processar dados de forma automática.
O tema principal destes exercícios será o processamento de dados de vias metabólicas, com foco sobre as proteínas que catalisam as reações químicas das vias, também conhecido como _enzimas_.
Apesar de trabalharmos com vias metabólicas durante as aulas, os métodos de processamento de dados que os alunos vão aprender nesta disciplina podem ser aplicado a muitos outros tipos de dados.

## Dados

A figura que se segue representa os primeiros passos na glicólise, uma via metabólica que decompõe a glicose em compostos químicos mais pequenos.
Esta figura inclui uma representação de cinco etapas desta via, cada uma catalisada por uma enzima diferente.

![Uma via metabólica](images/pathway.png "Exemplo de uma via metabólica")

Para estas aulas, iremos fornecer [um ficheiro Excel](files/metabolic_pathways.xls) com informação sobre 297 vias metabólicas.
Cada linha neste arquivo contém:

- O identificador da via metabólica;
- O nome da via;
- A classe a que pertence;
- Uma lista das enzimas que participam na via.

Assim, o arquivo Excel tem 297 linhas de informação, mais uma para os cabeçalhos das colunas.

A imagem seguinte mostra uma imagem do ficheiro Excel e seus dados.

![Screenshot do ficheiro Excel](images/excel.png "Parte dos dados do ficheiro Excel")

Esta informação foi extraída de um banco de dados online chamado [Kyoto Encyclopedia of Genes and Genome](http://www.genome.jp/kegg/kegg2.html).
As enzimas são referidos pelo seu código UniProt.
A [UniProt](http://www.uniprot.org/) é um banco de dados de proteínas que contêm, entre uma vasta quantidade de informação, as sequências de aminoácidos das proteínas.

## Processamento

Apesar de os dados serem fornecidos aos alunos na forma de ficheiro Excel, as operações de processamento de dados vão ser maioritariamente executadas com uma linguagem de programação.
Nesta disciplina vamos usar [Python](http://www.python.org).
O processamento dos dados com Python em vez de Excel oferece vários benefícios:

- Podemos definir um conjunto de operações a serem executadas automaticamente, as quais levariam muito tempo no Excel, uma vez que nesse programa o processamento de dados é feito maioritariamente através da interação do utilizador com a interface gráfica, e não com o uso direto de comandos;
- Uma linguagens de programação pode lidar com tipos de dados complexos, enquanto que o Excel é principalmente orientada para cálculos numéricos.

Não será necessário nenhum conhecimento profundo da programação para os exercícios das aulas, pois iremos fornecer a maior parte do código.
Na verdade, os alunos não aprenderão diretamente os detalhes do Python como uma linguagem de programação, mas em vez disso, serão dadas "receitas" que contêm a maior parte da lógica necessária, com pequenos trechos de código em falta que os estudantes precisarão de preencher.
No entanto, esperamos que os alunos se familiarizarem com a sintaxe de Python, seguindo alguns cursos online.
Por exemplo, o [Codecademy](https://www.codecademy.com/en/tracks/python) contém seis módulos que irão ajudar os alunos nesta tarefa (note-se que existem versões em português nesse site):

- [Python Syntax](https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1?curriculum_id=4f89dab3d788890003000096)
- [Strings & Console Output](https://www.codecademy.com/courses/python-beginner-sRXwR/0/1?curriculum_id=4f89dab3d788890003000096)
- [Conditionals & Control Flow](https://www.codecademy.com/courses/python-beginner-BxUFN/0/1?curriculum_id=4f89dab3d788890003000096)
- [Python Lists and Dictionaries](https://www.codecademy.com/courses/python-beginner-en-pwmb1/0/1?curriculum_id=4f89dab3d788890003000096)
- [File Input/Output](https://www.codecademy.com/courses/python-intermediate-en-OGNHh/0/1?curriculum_id=4f89dab3d788890003000096)

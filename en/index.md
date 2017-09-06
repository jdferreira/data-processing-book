% Biological Data Processing with Python and SQL
% João D. Ferreira; Francisco M. Couto
% Faculdade de Ciências da Universidade de Lisboa<br>Version of 2017

<div id="license">
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
![](images/cc-88x31.png "Creative Commons License")
</a>
This work is licensed under a<br>
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)
</div>

# Table of contents

- [Introduction](#introduction)
- [Module 1 -- Metabolic pathway data](#module1)
- [Module 2 -- CSV files](#module2)
- [Module 3 -- Relational databases](#module3)
- [Module 4 -- Read and print data](#module4)
- [Module 5 -- Filter data](#module5)
- [Module 6 -- Web services](#module6)
- [Module 7 -- Merging data](#module7)
- [Module 8 -- Regular expressions](#module8)
- [Module 9 -- Create a database](#module9)
- [Module 10 -- Query a database](#module10)
- [Module 11 -- Access a database](#module11)


# Introduction

The aim of these exercises is to provide students the ability and competence to process data in an automatic fashion.
The main topic surrounding these exercises will be metabolic pathway data processing, with a closer focus on the proteins that catalyse the chemical reactions of those pathways, also known as _enzymes_.
Despite working with metabolic pathways during the classes, the data processing methods that the students will learn in this class can be applied to many other types of data.

Despite the data being provided to the students as an Excel file, the data processing operations will mostly be executed with a programming language and a relational database.
In this class, we will use [Python](http://www.python.org) and [SQLite](https://www.sqlite.org/).
Processing our data with Python and SQLite instead of just using Excel offers several benefits:

- We can define a set of operations to be executed automatically, which in Excel would take a large amount of time, since it is mostly driven by user interaction rather than direct commands;
- Programming languages can handle complex data types and large datasets, while Excel is mostly oriented towards numeric computations.

No deep knowledge of programming will be required for the class exercises, as we will provide most of the code.
In fact, the students will not directly learn the details of Python and SQL as programming languages, but will instead be given "recipes" that contain most of the necessary logic, with small snippets of missing code that the students need to fill.
However, we expect that the students familiarize themselves with Python and SQL syntax by following some online courses.
For example, [Codecademy](https://www.codecademy.com/) contains multiple modules that will help the students in this task:

- [Python](https://www.codecademy.com/learn/learn-python)
- [SQL](https://www.codecademy.com/learn/learn-sql)


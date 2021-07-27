# OCR - Chess Tournament Manager

## The project :
It's the 4th project to the Python Developer course.
The goal of the project is to build a full application with the MVC pattern.
For this we have to develop a chess tournament manager.

## Requirement :
Python 3.x

## Used external libraries

### Inquirer : 
Inquirer should ease the process of asking end user questions, parsing, validating answers, managing hierarchical prompts and providing error feedback.

https://github.com/magmax/python-inquirer

### Pandas :
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. 

https://pandas.pydata.org/

### Colorama :
Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.

https://pypi.org/project/colorama/

### TinyDB :
TinyDB is a lightweight document oriented database optimized for your happiness :) It’s written in pure Python and has no external dependencies. The target are small apps that would be blown away by a SQL-DB or an external database server.

https://tinydb.readthedocs.io/en/latest/

### Flake8 + Flake8-Html
Flake8 is a wrapper around these tools:

- PyFlakes
- pycodestyle
- Ned Batchelder’s McCabe script

Flake8 runs all the tools by launching the single flake8 command. It displays the warnings in a per-file, merged output.

https://flake8.pycqa.org/en/latest/

Flak8-Html : A flake8 plugin to generate HTML reports of flake8 violations.

https://pypi.org/project/flake8-html/

## Installation

- Download the files or clone the repo where you want :
```bash
cd {your-desired-path}
git clone git@github.com:FrancoisQUI/P4-00-Projet.git
cd P4-00-Projet
```
- Create and activate your virtual environnement :
```bash
python -m venv {your-desired-env-path}
source {your-desired-env-path}/activate
```
- Install necessary packages
```bash
pip install -r requirements.txt
```

## Start the app
```bash
python main.py
```

## Generate a Flake8 report
```bash
flake8 --format=html --htmldir=flake-report --exclude=./env
```
The report will be created in the flaker-report directory.
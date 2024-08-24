<div align="center" id="top"> 
  <img src="./img/dataops-icon.png" alt="img-logo" style="width:750px; height:250px;" />

  &#xa0;

</div>

<h1 align="center">DataOps</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/Pedrinhonitz/dataopsa?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/Pedrinhonitz/dataops?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Pedrinhonitz/dataops?color=56BEB8">

</p>

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#rocket-tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-como-usar">Como Usar</a> &#xa0; | &#xa0;
  <a href="https://github.com/Pedrinhonitz" target="_blank">Autor</a>
</p>

<br>

## :dart: Sobre ##

Este projeto é uma implementação de uma esteira de dados (DataOps) que automatiza o fluxo de dados desde a extração de dados brutos até o tratamento e armazenamento em um banco de dados PostgreSQL.

## :rocket: Tecnologias ##

As seguintes ferramentas foram utilizadas neste projeto:

- [Airflow](https://airflow.apache.org/)
- [DBT](https://www.getdbt.com/)
- [Python](https://www.python.org/)
- [SQL](https://www.postgresql.org/docs/current/sql.html)
- [Docker](https://www.docker.com/)
- [Make](https://www.gnu.org/software/make/manual/make.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)


## :white_check_mark: Como Usar ##
```bash
# Clone
$ git clone https://github.com/Pedrinhonitz/dataops.git

# Entrando na Pasta
$ cd dataops

# Abrindo no VScode
$ code .

# Inicializando o Ariflow
$ make build

# Parando a execução do Airflow
$ make stop

# Parando a execução do Airflow e fazendo prune
$ make kill
```

<br>
Feito por <a href="https://github.com/Pedrinhonitz" target="_blank">Pedrinhonitz</a>

&#xa0;

<a href="#top">Voltar ao topo</a>
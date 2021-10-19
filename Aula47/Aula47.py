import sqlite3
from sqlite3 import Error

print "Aula 47"

def conexDB(): # Criando a conexão sqlite3
    conex = None
    try:
        conex = sqlite3.connect("C:\\Users\\Estudio3\\Documents\\GitHub\\PythonDev\\CFB Aulas\\Aula47\\banco.db")
    except Error as ex:
        print ex
    return conex

# Código SQL
sqlcode = """ 
    CREATE TABLE tb_contatos_teste0 (
        N_IDCONTATO        INTEGER      PRIMARY KEY AUTOINCREMENT,
        VC_NOMECONTATO     VARCHAR (30),
        VC_TELEFONECONTATO VARCHAR (14),
        VC_EMAILCONTATO    VARCHAR (30) 
    );
"""

def newTabela(conex, sql):
    try:
        new = conex.cursor() # Indicando o ponteiro do arquivo
        new.execute(sql)
        print "Tabela criada"
    except Error as ex:
        print ex

############## Programa
newTabela(conexDB(), sqlcode)
conexDB().close()
import sqlite3
from sqlite3 import Error

print "Aula 52"

def conexDB(): # Criando a conexão sqlite3
    conex = None
    try:
        conex = sqlite3.connect("C:\\Users\\Estudio3\\Documents\\GitHub\\PythonDev\\CFB Aulas\\Aula47\\banco.db")
    except Error as ex:
        print ex
    return conex

# Código SQL
sqlcode = "SELECT * FROM tb_contatos_teste0 WHERE VC_NOMECONTATO='{$nome}'"

def selectTb(conex, sql):
    new = conex.cursor() # Indicando o ponteiro do arquivo
    new.execute(sql) #query
    print "Registro resgatado..." 
    return new.fetchall()

print selectTb(conexDB(), sqlcode)
conexDB().close()
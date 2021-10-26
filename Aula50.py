import sqlite3
from sqlite3 import Error

print "Aula 50"

def conexDB(): # Criando a conexão sqlite3
    conex = None
    try:
        conex = sqlite3.connect("C:\\Users\\Estudio3\\Documents\\GitHub\\PythonDev\\CFB Aulas\\Aula47\\banco.db")
    except Error as ex:
        print ex
    return conex

id = raw_input("Deletar tabela de que id? ").replace("\r", "")

# Código SQL
sqlcode = "DELETE FROM tb_contatos_teste0 WHERE N_IDCONTATO={0};".format(id)

def deleteTb(conex, sql):
    try:
        new = conex.cursor() # Indicando o ponteiro do arquivo
        new.execute(sql) #query
        conex.commit() ############# COMMIT
        print "Registro deletado..."
    except Error as ex:
        print ex
    return conex

deleteTb(conexDB(), sqlcode)
conexDB().close()
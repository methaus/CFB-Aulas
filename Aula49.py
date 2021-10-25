import sqlite3
from sqlite3 import Error

print "Aula 49"

nome = raw_input("Nome: ").replace("\r", "")
telefone = raw_input("Tel: ").replace("\r", "")
email = raw_input("Email: ").replace("\r", "")

def conexDB(): # Criando a conexão sqlite3
    conex = None
    try:
        conex = sqlite3.connect("C:\\Users\\Estudio3\\Documents\\GitHub\\PythonDev\\CFB Aulas\\Aula47\\banco.db")
    except Error as ex:
        print ex
    return conex

# Código SQL
sqlcode = """ 
    INSERT INTO tb_contatos_teste0 (
        VC_NOMECONTATO, VC_TELEFONECONTATO, VC_EMAILCONTATO 
    )VALUES(
        '{0}','{1}','{2}'
    );
""".format(nome, telefone, email)

def insertTb(conex, sql):
    try:
        new = conex.cursor() # Indicando o ponteiro do arquivo
        new.execute(sql) #query
        conex.commit() ############# COMMIT
        print "Registro inserido..."
    except Error as ex:
        print ex
    return conex

insertTb(conexDB(), sqlcode)
conexDB().close()
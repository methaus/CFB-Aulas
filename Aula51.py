import sqlite3
from sqlite3 import Error

print "Aula 51"

def conexDB(): # Criando a conexão sqlite3
    conex = None
    try:
        conex = sqlite3.connect("C:\\Users\\Estudio3\\Documents\\GitHub\\PythonDev\\CFB Aulas\\Aula47\\banco.db")
    except Error as ex:
        print ex
    return conex

Id = raw_input("ID do registo a ser atualizado: ").replace("\r", "")
nome = raw_input("Novo nome: ").replace("\r", "")
telefone = raw_input("Novo telefone: ").replace("\r", "")
email = raw_input("Novo email: ").replace("\r", "")

# Código SQL
sqlcode = """
    UPDATE tb_contatos_teste0 SET 
    VC_NOMECONTATO='{0}', VC_TELEFONECONTATO='{1}', VC_EMAILCONTATO='{2}'
    WHERE N_IDCONTATO={3}
""".format(nome, telefone, email, Id)

def updateTb(conex, sql):
    try:
        new = conex.cursor() # Indicando o ponteiro do arquivo
        new.execute(sql) #query
        conex.commit() ############# COMMIT
        print "Registro atualizado..."
    except Error as ex:
        print ex
    return conex

updateTb(conexDB(), sqlcode)
conexDB().close()

############### Não dá erro se atualizar um registro inexistente
import os
import json
import sqlite3
from sqlite3 import Error

print "Aula 53 - Agenda"

path  = "C:/agendas/agenda.db"

if not os.path.exists(path):
    null = open(path, "w")
    null.close()

def connDB():
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as ex:
        print ex
    return conn

#PROGRAM
conn = connDB()

try:
    conn.cursor().execute("""
    CREATE TABLE contatos (
        id_contato INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_contato VARCHAR(100) NOT NULL,
        telefone_contato VARCHAR(30),
        email_contato VARCHAR(100)
    )""")
    conn.commit()
    print "Tabela criada com sucesso!"
except Error as ex:
    createTableError = ex

while 1:
    os.system('cls')
    print """============================
-----------Agenda-----------
============================
    [1] Adicionar contato
    [2] Editar contato
    [3] Deletar contato
    [4] Mostrar agenda

    [0] Sair
"""

    option = raw_input("     >> ")

    if option == "1\r":
        print "\nAdicionar contato..."
        try:
            conn.cursor().execute("INSERT INTO contatos (nome_contato, telefone_contato, email_contato) VALUES ('{0}', '{1}', '{2}')".format(raw_input("Nome: ").replace("\r", ""),raw_input("Telefone: ").replace("\r", ""),raw_input("Email: ").replace("\r", "")))
            conn.commit()
            print "Contato adicionado!"
        except Error as ex:
            print ex
    elif option == "2\r":
        id_contato = raw_input("\nEditar contato de id: ").replace("\r", "")
        try:
            conn.cursor().execute("UPDATE contatos SET nome_contato = '{0}', telefone_contato = '{1}', email_contato = '{2}' WHERE id_contato = {3}".format(raw_input("Nome: ").replace("\r", ""),raw_input("Telefone: ").replace("\r", ""),raw_input("Email: ").replace("\r", ""),int(id_contato)))
            conn.commit()
            print "Contato alterado!"
        except Error as ex:
            print ex
    elif option == "3\r":
        try:
            conn.cursor().execute("DELETE FROM contatos WHERE id_contato = {0}".format(int(raw_input("ID do contato a deletar: ").replace("\r", ""))))
            conn.commit()
            print "Contato deletado!"
        except Error as ex:
            print ex
    elif option == "4\r":
        contador = 1
        for i in conn.cursor().execute("SELECT * FROM contatos").fetchall():
            print "Contato {0}: {1}".format(contador, json.dumps(i))
            contador+=1
    elif option == "0\r":
        break
    else:
        print "Opcao invalida!"
    raw_input()

os.system('cls')
print "Fim do programa..."

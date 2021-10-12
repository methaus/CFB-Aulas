import re

print "Aula 44"

oper = raw_input("Operacao 'r' 'a' 'w': ").replace("\r", "")
arqui = open("C:/Users/Estudio3/Documents/GitHub/PythonDev/CFB Aulas/Aula44/{0}".format(raw_input("Nome do arquivo: ").replace("\r", "")), oper)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for rewriting, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file

if (oper == 'r'):
    search = raw_input("Procurar no arquivo: ").replace("\r", "")
    ocor = re.findall(search, arqui.read())
    print "Ocorrencia: {0}, Qtde: {1}.".format(ocor, len(ocor))
if (oper == 'a'):
    print "Caracteres escritos: {0}".format(arqui.write(raw_input("Adicionar ao arquivo: ")))
if (oper == 'w'):
    print "Caracteres escritos: {0}".format(arqui.write(raw_input("Adicionar ao arquivo: ")))
arqui.close()
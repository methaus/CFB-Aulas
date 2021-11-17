import re
import os

print "Aula 44/45"
caminho = "C:/Users/Estudio3/Documents/GitHub/PythonDev/CFB Aulas/Aula44/"

oper = raw_input("Operacao 'r' 'a' 'w': ").replace("\r", "")
arqui = open("{0}{1}".format(caminho, raw_input("Nome do arquivo: ").replace("\r", "")), oper)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for rewriting, creates the file if it does not exist
# (python 3) "x" - Create - Creates the specified file, returns an error if the file exist

if (oper == 'r'):
    search = raw_input("Procurar no arquivo: ").replace("\r", "")
    ocor = re.findall(search, arqui.read())
    arqui.seek(0) #tornar o ponteiro do arquivo de volta ao início para a proxima leitura
    """
    Por isso que o readline() lê as linhas consecutivamente
    readline().1 lê a primeira linha
    readline().2 lê a segunda linha
    readline().3 lê a terceira linha
    Pois está levando o ponteiro
    readlines() retorna todas as linhas numa list de strings
    """
    print "Ocorrencia: {0}, Qtde: {1}.".format(ocor, len(ocor))
    print "{0} {1}".format(arqui, type(arqui))
    print "{0} {1}".format(arqui.read(), type(arqui.read()))

if (oper == 'a'):
    print "Caracteres escritos: {0}".format(arqui.write(raw_input("Adicionar ao arquivo: ")))

if (oper == 'w'):
    print "Caracteres escritos: {0}".format(arqui.write(raw_input("Adicionar ao arquivo: ")))

arqui.close()

remove = raw_input("Remover arquivo: ")
try:
    os.remove(caminho+remove.replace("\r", ""))
except:
    print "Nenhum arquivos removido."
finally:
    print "Fim do programa..."
print "Aula 07"

mot = "Curso de Python - Aula 07"
testador = "Python" in mot #not = negação
formato = "{0} nao contem a palavra *Python* = {1}"

print mot + " contem a palavra *Python* = " + str(testador) #Forma com casting
# <value> in var / in = testador de existência, saída boolean

print formato.format(mot,not testador) #Forma sem casting
print "\'aspas\"\nponto"

#Criar caracteres de escape = contra-barra (\)
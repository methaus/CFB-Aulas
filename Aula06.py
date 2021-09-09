print "Aula 06"

mot = "Aulas de Python"
print mot[9:15] #posição 9 a 15
print "{0} tem tamanho: {1}".format(mot[0:5],len(mot[0:5]))
print "{0} tem tamanho: {1}".format(mot,len(mot))
mot = mot.replace("Python","C#")
print "{0} tem tamanho: {1}".format(mot,len(mot))
array = mot.split(" ") #Retorna list o corte sendo o index indicado
print array

# string.strip() = remove espaços anteriores e posteriores, ex: " curso de python   " = "curso de python"
# string.lower() = tudo minúsculo
# string.upper() = tudo maiúsculo
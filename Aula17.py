print "Aula 17"

keylist = { #Não é uma lista ordenada
    "A": "Valor 1",
    "B": "Valor 2",
    0: "Valor 3"
}

print keylist
print "{0} {1} {2}\n".format(keylist["A"], keylist["B"], keylist[0]) #Dict não recebe índice de ordem

lista = keylist.items() #Retorna uma list com cada item do dict como uma tupla
print lista[0][0]
for i,j in lista:
    print "chave: {0} = valor: {1}".format(i,j)

valores = keylist.values() #Retorna uma list com somente os valores do dict
print valores

valor = bool("A" in keylist)
valor1 = bool("C" in keylist)
if 0 in keylist:
    print "0 is in keylist"
print valor
print str(valor1) + "\n"

keylist["Nova chave"] = "Novo Valor" #Adiciona uma chave sem método
print keylist

keylist.pop("Nova chave") #Remove o item pelo índice
print str(keylist) + "\n"

keylist.popitem() #Remove o último adicionado
print keylist

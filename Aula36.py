import json

print "Aula 36"

# JSON(string) para Dict
listaJSON = '{"chave1":"item1","chave2":"item2","chave3":"item3","chave4":"item4"}'

lista = json.loads(listaJSON) # .load string

print "{0} {1}".format(lista, type(lista)) # u' = unicode
print "{0} {1}".format(lista.items(), type(lista.items()))
print "{0} {1}".format(lista["chave1"], type(lista["chave1"]))
print "-----------------"

# Dict para JSON(string)
dictJSON = {
    "chave1":"item1",
    "chave2":"item2",
    "chave3":"item3",
    "chave4":"item4"
}

dicio = json.dumps(dictJSON) # .dump string

print "{0} {1}".format(dicio, type(dicio))
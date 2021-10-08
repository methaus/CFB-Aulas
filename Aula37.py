import json
import os

print "Aula 37"

listJSON = ["item1","item2","item3","item4"] # List se torna um array JSON
tupleJSON = ("item1","item2","item3","item4") # Tuple se torna um array JSON
dictJSON = { # Dict se torna um obj JSON
    "chave2":"item1",
    "chave0":listJSON,
    "chave3":"item3",
    "chave1":tupleJSON
} # só converte em ordem auto se tiver valores ordenados 

dicio = json.dumps(dictJSON, indent=4, separators=(";","= "), sort_keys=True)
# indent=(valor do tab)
# separators=(" , "," : ")
print "{0} {1}".format(dicio, type(dicio))
print "---------------"

with open('C:\\Users\\Estudio3\\Documents\\GitHub\\PythonDev\\CFB Aulas\\Aula37.json', 'r') as file:
    jason = json.load(file)

print jason

saida = json.dumps(jason, indent=4)

print saida

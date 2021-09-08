print "Aula 04"

x = 1; y = 1.5; z = "um ponto cinco"; f = False #False com F maiúsculo
i = complex(x, y)
array = [1,2,3,"pedro",False] #Python chama o array de list [] aceita varios tipos // list()
tupla = (1,2,3,2,1) #Um array estático e imutável () // tuple()
tipoSet = {1,2,2,3,1,"Carlos"} #Lista não ordenada e suporta operações de conjunto {} //set()
frozen = frozenset(tipoSet) #Lista 'set' estática e imutável //frozenset
dicio = {
    0: "Valor1",
    "nome": "Valor2",
    True: "Valor3"
} #Lista dictionary com índice chave-valor //dict()

print str(x) + " tem tipo: " + str(type(x))
print str(y) + " tem tipo: " + str(type(y))
print z + " tem tipo: " + str(type(z))
print str(f) + " tem tipo: " + str(type(f))
print str(i) + " tem tipo: " + str(type(i))
print str(array) + " tem tipo: " + str(type(array))
print str(tupla) + " tem tipo: " + str(type(tupla))
print str(tipoSet) + " tem tipo: " + str(type(tipoSet))
print str(frozen) + " tem tipo: " + str(type(frozen))
print str(dicio) + " tem tipo: " + str(type(dicio))

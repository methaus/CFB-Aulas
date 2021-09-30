print "Aula 29"

lista = [1,2,3,4,5,6,7,8,9,10]
rotina = iter(lista)

while True:
    try:
        print next(rotina)
    except StopIteration:
        #Fim da rotina
        break

print "Fim do programa..."


"""
lista = ["Valor 1","Valor 2","Valor 3","Valor 4","Valor 5"]

leitura = iter(lista) #iter() = rotina a ser operada

print type(leitura) #type: <type 'listiterator'>

print next(leitura)
print next(leitura)
print next(leitura)

lista = ["Valor 5","Valor 4","Valor 3","Valor 2","Valor 1"]
leitura = iter(lista)

print next(leitura)
print next(leitura)

"""

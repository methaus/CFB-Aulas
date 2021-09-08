import random

print "Aula 05"

inteiro = 10
aleatorio = random.randrange(0, 10) #Intervalo de número aleatórios

print "{0} tem tipo: {1} e id: {2}".format(str(inteiro),str(type(inteiro)),id(inteiro))
inteiro = float(inteiro)
print "{0} tem tipo: {1} e id: {2}".format(str(inteiro),str(type(inteiro)),id(inteiro))

print "{0} tem tipo: {1} e id: {2}".format(str(aleatorio),str(type(aleatorio)),id(aleatorio))
print "{0} tem tipo: {1} e id: {2}".format(str(aleatorio),str(type(aleatorio)),id(aleatorio))

print "Cinco elementos aleatorios:"

i = 0
array = []
while i < 5:
    array.append(random.randrange(0,9))
    print array[i]
    i+=1

print array


# int()
# float()
# complex(real, imag)
# cast é o mesmo que atribuição
# Ramdom é uma biblioteca

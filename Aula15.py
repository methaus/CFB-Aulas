print "Aula 15"

tupla = (0, 0) #List estática
array = []

print "Insira dois valores xy para comparar com x=0 e y=0"
array.append(input("1 valor: "))
array.append(input("1 valor: "))
if array == list(tupla):
    print "verdadeiro"
else:
    print "falso"
print "Aula 09"

array = ["indice 0",0,1,2.2,True,False]

print array
print "Ultima posicao {0}".format(array[-1])
print "Penultima posicao {0}".format(array[-2])

array.append("Novo item")

print array
print "tamanho do array e {0}".format(len(array))
print "tamanho do indice 0 e {0}".format(len(array[0]))

#len() declara tamanho tanto de elementos quanto de conjuntos

array.remove(True) #int = 1 tem a mesma interpretação de True
array.remove(False) #int = 0 tem a mesma interpretação de True
print array

array.pop() #remove o último elemento da lista
print array

del array[1] #del = deleta por endereço
array1 = ["indice primeiro","indice segundo"] + list(array)
print array1
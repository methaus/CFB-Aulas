print "Aula 16"

lista = [ #Matriz é um array de array, ou seja, em Python, uma list de lists
    ["0 0","0 1","0 2"],
    ["1 0","1 1","1 2"],
    ["2 0","2 1","2 2"],
    ["3 0","3 1","3 2"]
]

print lista

for i in lista:
    for j in i:
        print j
    print "------"

for i,j,z in lista: #Recebe índice que leêm as colunas
    print "{0} {1} {2}".format(i,j,z)

print lista[1][1] #Leitura do array[index] que returna uma list[index] == (array[index])[index]


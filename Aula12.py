import random

print "Aula 12"

array = ["Vit","For","Sta","Dex","Wis","Luc"]

for i in range(5): #Loop index *i* percorre o objeto *range(5)* recebendo o índice
    print 1+i

for i in array:
    rng = random.randrange(0,10)
    if rng == 0:
        print "valor 0\nfim"
        break
    elif rng <= 3:
        score = "bad"
    elif rng <= 7:
        score = "good"
    else:
        score = "great"
    print "Status {0}: {1} {2}".format(i,rng,score)

for i in "vertical": #string logo convertida em objeto indexado
    print i

print "---------------"

matriz = [["0 0","0 1"],["1 0","1 1"]]

for coluna1,coluna2 in matriz: #Recebe dois índices que leêm a quatidade de colunas
    print "{0} {1}".format(coluna1,coluna2)

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

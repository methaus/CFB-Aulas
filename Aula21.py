import random

print "Aula 21"

def embaralhar(*params):
    array = list(params)
    p0 = ""
    for i in array:
        p0+=i
    random.shuffle(array)
    p1 = ""
    for i in array:
        p1+=i
    return (p0, p1)

print "Palavra: {0}, embaralhado: {1}".format(embaralhar("M","A","T","H","E","U","S")[0], embaralhar("M","A","T","H","E","U","S")[1])

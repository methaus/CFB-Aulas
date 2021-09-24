print "Aula 20"

def somar(*params):
    res = 0
    for i in params:
        res+=i
        print str(params.index(i))
        print i
    print "A soma dos calores e: " + str(res)

def printar(var0 = "Nao tem o valor[0]", var1 = "Nao tem o valor[1]"):
    txt = var0 + var1
    print txt

def testn(*params):
    print "{0} {1}".format(params, type(params))

somar(1,2)
printar("A ")
testn()


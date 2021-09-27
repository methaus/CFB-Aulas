print "Aula 22"

var0 = float(raw_input("INSIRA UM VALOR PARA TESTAR SE E POSITIVO OU NEGATIVO: "))

res = (lambda var0: False if var0 < 0 else True)(var0) #Testando se é positivo ou negativo, 0 == POSITIVO
var = (lambda var0: int(var0) if var0 == int(var0) else var0)(var0) #Para caso saída int, impressao int

def switch(res, var):
    case = {
        0: "{0} E NEGATIVO".format(var),
        1: "{0} E POSITIVO".format(var)
    }
    return case.get(res)

print switch(res, var)

#lambda recebe operações
print "Aula 26"

print "======= Calculadora =======\n"

try:
    num0 = float(raw_input("OPERANDO 1: "))
except ValueError:
    print "\n*VALOR NAO NUMERICO*\n"

#finally: (finaliza o programa sem ler o resto)

try:
    num1 = float(raw_input("OPERANDO 2: "))
except ValueError:
    print "\n*VALOR NAO NUMERICO*\n"

oper = raw_input("OPERACAO: ")

operacoes = ("+\r","-\r","*\r","/\r")

if oper not in operacoes:
    raise Exception("OPERACAO INVALIDA")

def operar(num0, num1, oper):
    switch = {
        0: num0 + num1,
        1: num0 - num1,
        2: num0 * num1,
        3: num0 / num1
    }
    return switch.get(operacoes.index(oper))

def testeInt(var):
    if var == int(var):
        return int(var)
    else:
        return var

print "{0} {1} {2} = {3}".format(testeInt(num0), oper[0], testeInt(num1), testeInt(operar(num0,num1,oper)))

print "\n===== fim do programa ====="

"""
erro = Exception("Qualquer valor dividido por 1 e o mesmo")

print "Entre com dois numeros para a divisao: "
num0 = float(raw_input("Primeiro numero: "))
num1 = float(raw_input("Segundo numero: "))

if num1 == 1:
    raise erro

try:
    res = num0 / num1
except ZeroDivisionError:
    print "\n*Nao e possivel dividir por 0*\n"
else:
    print "{0} / {1} = {2}".format(num0, num1, res)
finally:
    print "Fim do programa..."

"""
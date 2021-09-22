print "Aula 19"

num0 = float(raw_input("Digite dois numeros e escolha a operacao.\nPrimeiro numero: "))
num1 = float(raw_input("Segundo numero: "))
operacao = raw_input("Operacao (+) (-) (*) (/): ")

def switch(case):
    test = {
        "+\r": [num0 + num1, "+"],
        "-\r": [num0 - num1, "-"],
        "*\r": [num0 * num1, "*"],
        "/\r": [num0 / num1, "/"] 
    }
    return test.get(case, "Operacao invalida...")

print "{0} {1} {2} = {3}".format(num0, switch(operacao)[1], num1, switch(operacao)[0])


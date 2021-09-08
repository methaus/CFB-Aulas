print "Aula 03" 
#python não funciona em UTF-8

def funcao():
    global var #para ter acesso fora da variável = global <nome>, que não pode ser inicializada na mesma linha
    var = "variavel"

funcao() #função que está criando a variável global

print var



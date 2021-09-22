import random
import os

print "Aula 18"

entrada = -1; numero = random.randrange(0,100); tentativas = 0
while True:
    entrada = int(raw_input("Tente adivinhar o numero (0 a 100): "))
    os.system("cls")
    if (entrada < 0 or entrada > 100):
        print "Voce nao digitou um numero no intervalo de 0 a 100!"
    else:
        if entrada < numero:
            print "Tente adivinhar um numero maior que {0}.".format(entrada)
        elif entrada > numero:
            print "Tente adinhar um numero menor que {0}.".format(entrada)
        else:
            print "Voce acertou, o numero e {0}. Voce usou {1} tentativas.".format(numero,tentativas)
            break
        tentativas+=1
    print "Tentativas feitas: {0}.".format(tentativas)
print "Fim de Jogo"
    
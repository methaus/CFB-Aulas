import re

print "Aula 40/41/42/43"

txt = "Henri, homo ad mortus et fructo det homo, vus focu, Cicianon, vus focu det locus quod via locus, praq scienza saperego permicita voliego. Cicianon, un dexota demono, ire det circulego."

#findall(oque, onde) = retorna um array com todas as ocorrências da palavra
entrada = raw_input("Ocorrencia: ").replace("\r", "")
array = re.findall(entrada, txt)
print array
saida = len(array)
print "Vezes: " + str(saida)

#search(oque, onde) = retorna por método a posição inicial e final + 1 da primeira ocorrência
string = re.search(entrada, txt)
print "Primeira ocorrencia comeca em p({0}) e termina em p({1})".format(string.start(), string.end())

#split(divisor, onde) = retorna uma coleção com as strings da variavel
split = re.split(" ", txt)
print split

#sub(peloque, oque, onde) = substitui caracter por outro
replace = re.sub(raw_input("O que? ").replace("\r", ""), raw_input("No lugar do que? ").replace("\r", ""), txt)
print replace
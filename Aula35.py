import datetime

print "Aula 35"

data = datetime.datetime.now() #retorna a data local (do pc) AAAA/MM/DD HH:MM:SS.ML

print "Data de hoje: {0} e tem tipo {1}".format(data, type(data))
print "Dia: {0}\nMes: {1}\nAno: {2}".format(data.day,data.month,data.year)

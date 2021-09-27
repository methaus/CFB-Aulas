print "Aula 23"

class Char:
    name = ""
    classe = ""
    nv = 1
    def info(self):
        return "name: {0}\nclass: {1}\nlv: {2}".format(self.name, self.classe, self.nv)


personagem = Char()
personagem.name = "Player"
personagem.classe = "Guerreiro"
personagem.nv = 1

print personagem.info()

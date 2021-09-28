print "Aula 25"

class Char(object):
    def __init__(self, name, nv):
        self.name = name
        self.nv = nv
    def info(self):
        print "Nome: {0}\nNv: {1}".format(self.name, self.nv)
    
class Player(Char):
    def __init__(self, name, nv, classe, element):
        super(Player, self).__init__(name, nv)
        self.classe = classe
        self.element = element
    def info(self):
        super(Player, self).info()
        print "Classe: {0}\nElemento: {1}\n------------".format(self.classe, self.element)
        

personagem0 = Player("Jogador0", 1, "Guerreiro", "Luz")
personagem0.info()

personagem1 = Player("Jogador1", 3, "Arqueiro", "Vento")
personagem1.info()

personagem2 = Player("Jogador2", 2, "Mago", "Fogo")
personagem2.info()
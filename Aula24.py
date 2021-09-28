print "Aula 24"

class Char:
    name = ""
    classe = ""
    lv = 0
    def __init__(self, name, classe, lv):
        self.name = name
        self.classe = classe
        self.lv = lv
        print "Personagem {0} criado...\n".format(self.name)
    def Info(self):
        print "name: {0}\nclass: {1}\nlv: {2}\n--------------".format(self.name, self.classe, self.lv)
    def AddLv(self,lv):
        self.lv+=lv
        print "{0} lv + {1}\ncurrent lv: {2}".format(self.name, lv, self.lv)

personagem0 = Char("Player1","Guerreiro",1)
personagem1 = Char("Player2","Arqueiro",3)
personagem2 = Char("Player3","Cavaleiro",2)

personagem0.Info()

personagem1.AddLv(2)
personagem1.Info()

personagem2.Info()


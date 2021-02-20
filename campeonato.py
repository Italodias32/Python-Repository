def vencedor(lista):
    maior = -1
    for i in lista:
        if i.get_pontos() >= maior:
            maior = i.get_pontos()
            campeao = i.get_nome()
    
    return campeao
    
class Participante():
    def __init__(self, nome, index):
        self.__nome = nome
        self.__pontos = 0
        self.__index = index
    
    def get_nome(self):
        return self.__nome
    
    def get_pontos(self):
        return self.__pontos
        
    def get_index(self):
        return self.__index
        
    def set_pontos(self, aux):
        self.__pontos += aux
        
    def duelo(self, other):
        print('Duelo de ' + self.get_nome() + ' contra ' + other.get_nome())
        p1 = int(input('Quantos duelos ' + self.get_nome() + ' venceu ? '))
        p2 = int(input('Quantos duelos ' + other.get_nome() + ' venceu ? '))
        
        if p1 == 2 and p2 == 0:
            self.set_pontos(4)
        elif p1 == 2 and p2 == 1:
            self.set_pontos(3)
            other.set_pontos(1)
        elif p1 == 0 and p2 == 2:
            other.set_pontos(4)
        elif p1 == 1 and p2 == 2:
            other.set_pontos(3)
            self.set_pontos(1)
                  
    def pontucao_final(self):
        print('A pontução final de ' + self.get_nome() + ' foi de: ' + str(self.get_pontos()) + ' pontos')
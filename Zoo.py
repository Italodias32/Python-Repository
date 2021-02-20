from Animal import * 

class Zoo():
    def __init__(self):
        self.__catalogo = list()
        
    def __add__(self, other):
        return self.__catalogo + other.__catalogo
    
    def __str__(self):
        a = 'Metodo str sobreposto:\nLista de Animais do Zoo:\n\n'
        for i in self.__catalogo:
            a += i.__str__() 
        return a + '\n'
    
    def adicionar_animal(self, aux_animal):
        if isinstance(aux_animal, list):
            self.__catalogo.extend(aux_animal)
        else:
            self.__catalogo.append(aux_animal)
   
    
from Animal import * 

class Mamifero(Animal):
    def __init__(self, aux_nome, aux_peso):
        super().__init__(aux_nome, aux_peso)
        self.__classe = 'Mammalia'
    
    def __str__(self):
        return super().__str__().rstrip('\n') + ', Classe: ' + self.__classe + '\n'


class Ave(Animal):
    def __init__(self, aux_nome, aux_peso):
        super().__init__(aux_nome, aux_peso)
        self.__classe = 'Aves'
    
    def __str__(self):
        return super().__str__().rstrip('\n') + ', Classe: ' + self.__classe + '\n'


class Reptil(Animal):
    def __init__(self, aux_nome, aux_peso):
        super().__init__(aux_nome, aux_peso)
        self.__classe = 'Reptilia'
    
    def __str__(self):
        return super().__str__().rstrip('\n') + ', Classe: ' + self.__classe + '\n'


class Peixe(Animal):
    def __init__(self, aux_nome, aux_peso):
        super().__init__(aux_nome, aux_peso)
        self.__classe = 'Peixes'
    
    def __str__(self):
        return super().__str__().rstrip('\n') + ', Classe: ' + self.__classe + '\n'


class Anfibio(Animal):
    def __init__(self, aux_nome, aux_peso):
        super().__init__(aux_nome, aux_peso)
        self.__classe = 'Amphibia'
    
    def __str__(self):
        return super().__str__().rstrip('\n') + ', Classe: ' + self.__classe + '\n'
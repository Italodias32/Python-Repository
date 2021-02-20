#Classe Animal, principal classe do codigo, ela sera usada para herança
#Tem os gettes e setters e duas funções apenas
class Animal():
    def __init__(self, aux_nome, aux_peso):
        self.__nome = aux_nome
        self.__peso = aux_peso
    
    #Getter e Setters do Nome
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, aux_nome):
        if isinstance(aux_nome, str):
            self.__nome = aux_nome
        else:
            self.__nome = None
    
    #Property do Nome
    @property
    def __nome(self):
        return self._nome
    
    @__nome.setter
    def __nome(self, aux_nome):
        if isinstance(aux_nome, str):
            self._nome = aux_nome
        else:
            self._nome = str(aux_nome)      
    
    #Getter e Setter do Peso
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, aux_peso):
        if isinstance(aux_peso, float):
            self.__peso = aux_peso
        else:
            self.__peso = float(aux_peso)
    
    #Property do Peso
    @property
    def __peso(self):
        return self._peso
        
    @__peso.setter
    def __peso(self, aux_peso):
        if isinstance(aux_peso, float):
            self._peso = aux_peso
        else:
            self._peso = float(aux_peso)
    
    def __str__(self):
        return "Nome: " + self.__nome + ", Peso: " + str(self.__peso) + '\n'
    
    #Metodos da Classe   
    def imprime_animal(self):
        print("Nome: " + self.__nome + ", Peso: " + str(self.__peso))

    def alimentacao(self, peso_comida):
        self.__peso += peso_comida





#Aqui tem inicio as classes de herança, as classes mamimifero, aves e etc
#o rstrip() retira da string o que passa de parametro dentro dele, retira o \n que vem da superclasse
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





#Aqui é a classe zoologico que agrupa todas as outras classes
#isinstance testar se o objeto é instancia de outro
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





#Metodo principal
def main():
    zoo1 = Zoo()
    zoo1.adicionar_animal(Reptil('Cobra', 15))
    zoo1.adicionar_animal(Mamifero('Leao', 190))
    zoo1.adicionar_animal(Anfibio('Sapo', 0.50))

    zoo2 = Zoo()
    zoo2.adicionar_animal(Animal('Gorila', 160))
    zoo2.adicionar_animal(Peixe('Tubarao', 300))
    zoo2.adicionar_animal(Ave('Arara', 1))

    zoo3 = Zoo()
    zoo3.adicionar_animal(zoo1 + zoo2)

    print(zoo3)
    
main()
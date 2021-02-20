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

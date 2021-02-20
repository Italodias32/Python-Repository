from Classes_Animais import * 
from Zoo import * 

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

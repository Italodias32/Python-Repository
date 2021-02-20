from campeonato import *

numero_participantes = int(input('Digite o numero de participantes: '))
lista = list()
print('\nCerto! Agora vamos colocar os nomes dos participantes ok?\n')

count = 1
while True:
    aux = Participante(input('Digite o nome do participante ' + str(count) + ' : '), count)
    print('Obrigado\n')
    lista.append(aux)
    
    
    if count == numero_participantes:
       break
       
    count += 1
    print('vamos para o proximo')

partidas = numero_participantes*(numero_participantes - 1)
print('Como de participantes é ' + str(numero_participantes) + ' o numero de partidas do campeonato será ' + str(partidas) + '\n')

print('\nIniciando as partidas de ida:\n')
for i in lista: 
    for j in lista:
        if i.get_index() > j.get_index():
            i.duelo(j)
            print()

print('\nIniciando as partidas de volta:\n')
for i in lista: 
    for j in lista:
        if i.get_index() > j.get_index():
            i.duelo(j)
            print()

for i in lista:
    i.pontucao_final()
    
print('\nO grande vencedor é :' + vencedor(lista))
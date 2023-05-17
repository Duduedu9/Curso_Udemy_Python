# 0 1 2 3 4 5
# O tá vio See More
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' no nome)
# print('zero' no nome)
# print(10 * '-')
# print('vio' não está no nome)
# print('zero' não está no nome)

nome = input (' Digite seu nome: ')
encontrar = input(' Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar}  não está em {nome}')

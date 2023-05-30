"""
Iteração strings com while
"""
#       0123456   
nome = 'Eduardo Bizerra '
#       6543210

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome [indice]
    novo_nome += f'*{letra}'
    indice+=1

print(novo_nome)

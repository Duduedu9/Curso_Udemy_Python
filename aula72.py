# Exercicios com funções

# Cria uma função que multiplica todos os argumentos 
# não nomeados recebidos
# Retorne o total para uma variavel de mostre o valor
# da variavel.



def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero    
    return total

  
multiplicação = multiplicar(1, 2, 3, 4, 5)
print(multiplicação)



# Crie uma função fala se oum numero é par ou impar.
# Retorne se o numero é par ou impar.

def par_impar(numero):
   multiplo_2 =  numero % 2 == 0

   if multiplo_2:
        return f'{numero} é par' 
  
   return f'{numero} é impar' 

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

    
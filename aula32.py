"""""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = (int(input('Digite um numero inteiro: ')))
if numero_inteiro % 2 == 0:
    print (f'{numero_inteiro} é par')
elif numero_inteiro % 2 == 1:
   print(f'{numero_inteiro} é impar')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = (float(input('Qual o horario? ')))
if horario >= 0.0 and horario  <= 11.9 :
   print (f' Bom dia, são exatamente {horario}')
elif horario >= 12.0 and horario <= 17.59 :
    print (f'Boa tarde, são exatamente {horario}')
#elif horario >= 18.0 and horario  <= 23.59:
#   print (f'Boa noite, são exatamente {horario}')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

Nome = (str(input(' Digite seu primeiro nome: ')))
Conta_letra = len(Nome)
if Conta_letra >= 0 and Conta_letra  <= 4 :
    print(f' Seu nome nome é curto ')
elif Conta_letra >= 5 and Conta_letra <= 6 :
    print (f'Seu nome é normal ')
elif Conta_letra > 6 :
    print (f' Seu nome é muito grande ')

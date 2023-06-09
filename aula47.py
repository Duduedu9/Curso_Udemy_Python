"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
# loop infinito com while pois não sabemos em quantas tentativas vamos acertar.
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

# usando o if e len para digitar apenas uma letra, e o continue, para se der esse erro, continuar o programa.
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

# lógica para saber se é uma letra que o usuario acertou ou uma errada/ se estiver errado aparece *
# Usando o for dentro do while pois aqui sabemos o tamanho da palavra e o for é mais indicado quando
# sabemos até onde vamos.
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)
#usando o import os, para limpar o terminal depois que acertamos a palavra.
#e no final limpando as variaveis para não dá problema no programa
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0

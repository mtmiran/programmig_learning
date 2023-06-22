#!/usr/bin/python3

import forca, adivinhacao

print('##################')
print('Escolha o seu Jogo')
print('##################')


jogo = int(input('Qual o seu jogo? \n(1) Forca (2) Adinhação \nResposta: '))


if jogo == 1:
    forca.jogar()
    print('Jogando Forca')
elif jogo == 2:
    adivinhacao.jogar()
    print('Jogando Adivinhação')

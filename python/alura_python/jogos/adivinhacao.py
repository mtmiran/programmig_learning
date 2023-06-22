#!/usr/bin/python3

#### Bibliotecas ####

from random import randint

def jogar():
    #### Variáveis ####

    numero_secreto = randint(1, 101)
    pontos = 100


    #### Nível do  jogo ####

    while True:
        total_de_tentativas = input('Qual nível de dificuldade? \n(1) Fácil (2) Médio (3) Difícil \nResposta: ')

        if total_de_tentativas == "1":
            total_de_tentativas = 20
            pontos_rodada = 5
            break
        elif total_de_tentativas == "2":
            total_de_tentativas = 10
            pontos_rodada = 10
            break
        elif total_de_tentativas == "3":
            total_de_tentativas = 5
            pontos_rodada = 20
            break
        else:
            print('Você digitou errado!')


    #### Inicio do  jogo ####

    print("*********************************")
    print('Bem vindo ao jogo de adivinhação!')
    print("*********************************")


    for rodada in range(1, total_de_tentativas + 1):
        print(f'\n#### Tentativa {rodada} de {total_de_tentativas} ####\n')

        chute = int(input('Digite seu número entre 1 e 100: '))

        print('\n#### Incio do jogo ####\n')

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue
        else:
            if numero_secreto == chute:
                print('Você acertou!')
                break

            elif chute > numero_secreto:
                print('Você errou, seu chute foi maior do que o número secreto')
            else:
                print('Você errou, seu chute foi menor do que o número secreto')
            pontos = pontos - pontos_rodada
            rodada += 1

    print('\n#### Fim do jogo ####\n')
    print(f'Você digitou: {chute} \nE o número secreto é: {numero_secreto}')
    print(f'Você fez: {pontos} pontos')


#### Chamando Função ####

if __name__ == "__main__":
    jogar()

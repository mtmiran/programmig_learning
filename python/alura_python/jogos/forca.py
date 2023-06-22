#!/usr/bin/python3

import random

### Criando funções ### 

def imprimir_mensagem(mensagem):
    print('#' * len(mensagem))
    print(mensagem)
    print('#' * len(mensagem))


def carregar_palavra_secreta():
    # selecionando a palavra do arquivo palavras.txt
    arquivo = open('palavras.txt', 'r')
    palavras = [linha.strip() for linha in arquivo]
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    
    return palavra_secreta
    

def letra_chute():
    chute = input('Qual letra? ').lower()
    return chute.strip()   # tira espaços em branco


### Inicio do Jogo ###

def jogar():
    
    ### impirimir mensagem de inicio
    imprimir_mensagem('Bem vindo ao Jogo da Forca')

    ### criando a palavra secreta
    palavra_secreta = carregar_palavra_secreta()
    
    letras_acertadas = ['_' for letra in palavra_secreta]
    letras_erradas = len(palavra_secreta)

    print(letras_acertadas)

    while letras_erradas > 0:
        #### chamando função de chute
        chute = letra_chute()
        
        ### executando o jogo
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra 
                index += 1                      
 
        elif chute not in palavra_secreta:
                letras_erradas -= 1
                print(f'chutou errado heimm...você tem mais {letras_erradas} chances de acertar')

        print(letras_acertadas)

        # critério de pausa do comando while
        if letras_acertadas == list(palavra_secreta):
            print('\nParabéns! Você acertou!!\n')
            break
        elif letras_erradas == 0:
            print('\nVocê perdeu!\n')
        else:
            continue        


    ### impirimir mensagem de fim
    imprimir_mensagem('Fim do jogo')



#### Chamando Função do Jogo #### 

if __name__ == "__main__":
    jogar()

# Escrever uma função que recebe uma lista de Strings contendo nomes de pessoas como parâmetro e devolve o nome mais curto. A função deve ignorar espaços antes e depois do nome e deve devolver o nome 'capitalizado', i.e., apenas com a primeira letra maiúscula.

# Lista vazia

lista = []

# Inserindo nomes na lista

nome = 0

while nome != 'n':
    nome = str(input('Digite um nome(n para parar): '))
    if nome != 'n':
        lista.append(nome)
    else:
        break




# Função

def mais_curto(lista):
    count = 0
    len_lista = len(lista)
    menor = lista[count]
    while count < len_lista:        
        if len(lista[count]) <= len(lista[count + 1]):
            menor = lista[count]            
        else:
            menor = lista[count + 1]
        count += 1
    print(menor)


mais_curto(lista)

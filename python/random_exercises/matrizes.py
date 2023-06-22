# Matrizes - listas de listas
'''
Estrutura de dados bidimensional com linhas e colunas
A
1 2 3
4 5 6
7 8 9

A [0] [0] -> 1
A [1] [2] -> 8

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''

def cria_matriz(linha, coluna):
    # lista vazia
    matriz = []
    # cria a linha i como lista vazia linha
    for i in range(linha):
        linha = []
        for j in range(coluna):
            valor = int(input(str(f'Digiteo elemento da linha {[i]} coluna {[j]} ')))
            linha.append(valor)
        # adiciona linha à matriz    
        matriz.append(linha)
    return matriz
    

def ler_matriz():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(lin,col)

m = ler_matriz()
print(m)
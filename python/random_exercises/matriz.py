# Cria matriz

def cria_matriz(linha, coluna):
    matriz = []

    for i in range(linha):
        linha = []
        for c in range(coluna):
            n = int(input(f'Digite o valor da linha {[i]} coluna{[c]}'))
            linha.append(n)
        matriz.append(linha)
    return matriz


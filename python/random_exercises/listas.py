# Faça um programa em que o usuário digite uma sequência de números inteiros terminado por zero. No final, quando o usuário terminar ele digita 0 e vai mostrar a lista ordenado inverso.

# Input

lista = []
n = int(input('Digite um número terminado em zero: '))
lista.append(n)
while n > 0:
    n = int(input('Digite outro número terminado em zero. Digite zero(0) para terminar o programa: '))
    if n > 0:
        lista.append(n)

print(sorted(lista, reverse = True))
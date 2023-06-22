#!/usr/bin/python3

# Função Fatorial

def fatorial(n):    
    fat = 1
    while (n > 1):
        fat *= n
        n -= 1
    return fat
# Teste da função fatorial
'''
def testa_fatorial():
    if fatorial(1) == 1:
        print('Funciona para 1')
    else:
        print('Não funciona para 1')
    if fatorial(2) == 2:
        print('Funciona para 2')
    else:
        print('Não funciona para 2')
    if fatorial(0) == 1:
        print('Funciona para 0')
    else:
        print('Não funciona para 0')
    if fatorial(5) == 120:
        print('Funciona para 5')
    else:
        print('Não funciona para 5')

testa_fatorial()
'''

# Função Binominal
def numero_binominal(n, k):
    if k <= n:
        return fatorial(n) / (fatorial(k) * fatorial(n-k))
    else:
        print('Erro, k tem que ser menor ou igual a n')

print(numero_binominal(1,3))
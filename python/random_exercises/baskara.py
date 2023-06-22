#!/usr/bin/python3

# Formula de Baskara

import math

# Coeficientes

a = int(input('Digite o valor de "a": '))
b = int(input('Digite o valor de "b": '))
c = int(input('Digite o calor de "c": '))

# Função delta 
def delta(x, y, z):
    delta = (y**2) - (4 * x * z)
    return delta

# Função Raízes

def raiz1(x,y,z):
    x1 = (-y + math.sqrt(z)) / (2 * x)
    return x1

def raiz2(x,y,z):
    x2 = (-y - math.sqrt(z)) / (2 * x)
    return x2

# Executando o código
delta = delta(a,b,c)


if delta > 0:
    r1 = raiz1(a,b,delta)
    r2 = raiz2(a,b,delta)
    print(f'Seu delta é {delta}, maoir que zero, logo suas raízes são {r1} e {r2}.')
elif delta == 0:
    r1 = raiz1(a,b,delta)
    print(f'Seu delta é {delta}, igual a zero, logo sua única raíz é {r1}.')
else:
    print('Seu delta é menor que zero, não possui raízes.')
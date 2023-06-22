# dado um número inteiro positivo n, imprimir sua decomposição em fatores primos, indicando também a mutiplicidade de cada fator

def fatoracao(x):
    count = 0
    fator = 2
    while x > 1:
        while (x % fator) == 0:        
            x = x / fator
            count += 1
        print(f'{x} é dividido por {fator} ^ {count}')
        fator += 1


fatoracao(150)
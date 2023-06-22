# Funcoes: bloco de codigo que pode ser executado quando chamado, pode ser usado com parametro de entrada ou nao, saida ou nao. Reaproveitamento de código, ajuda na manutenção do codigo.
'''
n1 = 15
n2 = 7
'''

# Funções
def somar(n1,n2):
    r = n1 + n2
    print(f'Soma de {n1} e {n2} é igual {r}')

def subtrair(n1,n2):
        r = n1 + n2
        print(f'Subtração de {n1} e {n2} é igual {r}')

def multiplicar(n1,n2):
        r = n1 * n2
        print(f'Multiplicação de {n1} e {n2} é igual {r}')

def dividir(n1,n2):
        r = n1 / n2
        print(f'Divisão de {n1} e {n2} é igual {r}')

def calculos():
    somar(2,4)
    subtrair(1,2)
    multiplicar(4,5)
    dividir(8,7)

# Função com multiplas variaveis
def somar2(*num):
    r = 0 
    for n in num:
        r += n
    print(f'A soma do valores é {r}')

#Retorno de Funções
def somar3(*num):
        r = 0
        for n in num:
            r += n
        return r

# Retorno de função com multiplos valores
valores = [1,2,3,4,5,6,7,8,9]
def somar4(num):
        r = 0 
        for n in num:
            r += n
        return r


# Chamando Funções
calculos()
somar2(2,3,4,5,6,7,1,2,3,4)
print(somar3(2,2,1,4,5))
soma_valores = somar4(valores)
print(soma_valores)

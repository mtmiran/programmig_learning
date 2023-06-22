# Classes: conjunto de regras de um determinado objeto, objeto é uma instancia de classe
'''
class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()

c1.velMax = 200
c1.cor = "preto"
c1.ligado = False
estado = 'sim' if c1.ligado else 'não'
print(f'Velocidade máxima:{c1.velMax}')
print(f'Cor: {c1.cor}') 
print(f'Ligado: {estado}')
'''

# construtor __init__, metodo que vai instanciar um objeto da classe, self é uma referencia para propria class

class Carro:
    def __init__(self, vm, lig, cor):
        self.velMax = vm
        self.ligado = lig
        self.cor = cor
    
    def mostrar(self):
        estado = 'sim' if self.ligado else 'não'
        print(f'Velocidade máxima:{self.velMax}')
        print(f'Cor: {self.cor}') 
        print(f'Ligado: {estado}')
        print(10*'-=')
    def ligar(self):
        self.ligado = True
    def desligado(self):
        self.ligado= False
    def andando(self):
        if (self.ligado):
            print('Carro andando')
        else:
            print('Carro parado')



c1 = Carro(200, False, 'Preto')
c2 = Carro(120, False, 'Branco')
c3 = Carro(350, False, 'Vermelho')

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andando()
c2.andando()


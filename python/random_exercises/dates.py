#import datetime

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes 
        self.ano = ano
    
    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')


if "__main__" == __name__:
    data = Data(21, 11, 2007)
    data.formatada()
# Organizando finanças
''' Descobrir como armazenar um arquivo com os gastos e puxar esse arquivo nesse comando sempre que for executado
'''

tipoInput = int(input('Entrada(1) ou Gasto(2) de dinheiro: '))



# Gastos
mercantil = 0
nubank = 0
farmacia = 0

if tipoInput == 2:
    pergunta = 1
    while pergunta == 1:
        
        gasto = int(input('O gasto foi com Mercantil(1), Nubank(2), Farmacia(3): '))
        quanto = float(input('Quando? '))
        
        if gasto == 1:
            mercantil = mercantil + quanto
        elif gasto == 2:
            nubank = nubank + quanto
        else:
            farmacia = farmacia + quanto

        pergunta = int(input('Outro gasto? Sim(1) Não(2)'))



print(f'Gasto total = {mercantil + nubank + farmacia}')
# Video do Felipe Dechamps: https://www.youtube.com/watch?v=F608hzn_ygo&t=150s
# Introdução a Ciência de Dados (Primeira aula prática programando em Python)
# pip3 install pandas

import pandas as pd # (pd nome para o pandas...tem q dar um nome antes)

# importar o arquivo csv do endereço(uri) como string
uri_notas = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.3/ratings.csv'
uri_filmes = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.3/movies.csv'

# ler o arquivo csv e colocar em uma variável
notas = pd.read_csv(uri_notas)
filmes = pd.read_csv(uri_filmes)

# colocar as colunas em portugeus, alterar o dado
notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
filmes.columns = ['filmeId', 'título', 'generos']

# Saída de Dados
'''
print(filmes.head())     # head lê as 5 primeiras linhas (quase um cabeçario)
print('-=' * 50)
print(notas.head())'''

# Saber os valores únicos, quais as notas que tem, sem levar em quanta a quantidade de notas
#print(notas['nota'].unique())

# Média das notas
#print(notas['nota'].mean())

# Minimo
#print(notas['nota'].min())

# Estatisticas tradicionais do data.frame
print(notas.describe())
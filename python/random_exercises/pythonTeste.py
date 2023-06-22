#!/usr/bin/python3

# Teste automatizado de python
# pip3 install -U pytest
# executar: py.test nome_do_arquivo.py
def func(x):
	return x + 1

def test_amswer():
	assert func(3) == 5


#!/usr/bin/python3

'''Converte temperaturas de Celsius para Fahrenheit, Kelvin para Celsius e Kelvin para Fahrenheit
Uso:
	Carregue no python console usando
		import temp_convert as tc
	Autor:
		Mateus Miranda - 24/04/2020
'''

def celsius_para_fahrenheit(temp_celsius):
	return (temp_celsius * 1.8) + 32

def kelvins_para_celsius(temp_kelvin):
	return temp_kelvi - 273.15

def kelvins_para_fahr(temp_kelvins):
	temp_celsius = kelvins_para_celsius(temp_kelvins)
	temp_fahr = celsius_para_fahr(temp_celsius)
	return temp_fahr

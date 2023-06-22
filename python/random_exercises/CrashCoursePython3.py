#!/usr/bin/python3

# link: https://www.youtube.com/watch?v=DcEfZeR71qg
# instalar sudo apt install figlet -> chamar no ipython !figlet 'Mateus'


#print('hello world')

# Python Shell: digite python3 no terminal
# Matemática básica
# Variaveis: pedaços de memoria alocada
# Indentation
# ipython:sudo pip3 install ipython; python shell com highlight (interativo)
# Tipos de dados: strings, dictionaries,  lists, tuplas, int, float, bol....
'''
sets-> não repete valores {}
tuplas -> imutavel ()

name = "mateus"
print(type(name))
'''
# Indexing: tirar algo em particular de ums lista/sequencia de valores
# Comments->deixar notas no codigo
# String formating -> (f'blablabla{}')
# Files-> w: write; r: read; a: append
'''
In [2]: with open('try_me.py', 'w') as file_handler:
   ...:     file_handler.write('print("hello world")')
   ...:     file_handler.close()
   ...: 

In [3]: wiht open("try_me.py", "r") as fh:
   ...:     content = fh.read()
  File "<ipython-input-3-810778039bab>", line 1
    wiht open("try_me.py", "r") as fh:
            ^
SyntaxError: invalid syntax


In [4]: with open("try_me.py", "r") as fh:
   ...:     content = fh.read()
   ...:     fh.close()
   ...: 

In [5]: print(content)
print("hello world")

In [6]: with open('try_me.py', 'a') as fh:
   ...:     fh.write('\nTesting line 2')
   ...:     fh.close()
   ...:
'''

# Comparison Operator ( ==; >=, <=, != )
# For Loops
# While Loops
'''
[200~In [4]: n = 1

In [5]: while n < 10:
       ...:     print(n)
          ...:     n += 1
             ...: 
             1
             2
             3
             4
             5
             6
             7
             8
             9
'''
# List Compreention
'''
In [6]: nums = [1,2,3,4,5,6,7,8,9,10]

In [7]: nums
Out[7]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [8]: times_ten = [num*10 for num in nums]

In [9]: times_ten
Out[9]: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

In [10]: times_ten = [num*10 for num in nums if num % 2 == 0]

In [11]: times_ten
Out[11]: [20, 40, 60, 80, 100]
'''
# Functions
'''
In [12]: def greeting(name):
    ...:     print(f'{name}, hello to you good sir!')
    ...:

In [13]: greeting('mateus')
mateus, hello to you good sir!

KeyWord Argument -> *args
Regular Argument -> **kwargs

def blabla(name, greetings='Hello') -> name=args, greetings=kwargs
'''

# Scope - Global...
# OPP - Classes (em python tudo é objeto mas podemos criar nossos proprio objetos, variaveis sao atributos e funções sao metodos)
'''
In [14]: class Person:
    ...:     pass
    ...:

In [15]: mateus = Person()

In [16]: mateus
Out[16]: <__main__.Person at 0x7f713e2a3b38>

In [17]: type(mateus)
Out[17]: __main__.Person

In [18]: class Person:
    ...:     name = 'Mateus'
    ...:

In [19]: pessoa = Person()

In [20]: pessoa.name
Out[20]: 'Mateus'

In [21]: class Person:
    ...:     name = 'Mateus'
    ...:     def speak(self):
    ...:         print('I need tacos')
    ...:

In [22]: hungry_person = Person()
In [24]: hungry_person.speak()
I need tacos

In [30]: class Person:
    ...:     def __init__(self, name, age, food):
    ...:         self.name = name
    ...:         self.age = age
    ...:         self.food = food
    ...:     def speak(self):
    ...:         print(f'Feed me more {self.food}')
    ...:     def get_name(self):
    ...:         print('The name of this person is', self.name)
             def __str__(self):
    ...:         return self.name

    ...:

In [31]: mateus = Person('Mateus', 31, 'Pizza')

In [32]: mateus.name
Out[32]: 'Mateus'

In [33]: mateus.age
Out[33]: 31

In [34]: mateus.food
Out[34]: 'Pizza'

In [36]: mateus.speak()
Feed me more Pizza

In [37]: mateus.get_name()
The name of this person is Mateus

In [42]: mateus
Out[42]: <__main__.Person at 0x7f713d7596d8>

In [43]: print(mateus)
Mateus
'''

# Packages -> pip
'''
mateus@debian:~/Documentos/Python$ pip3 -V
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)

mateus@debian:~/Documentos/Python$ pip3 freeze -> mostra todos os pacotes instalados
'''

# Try and Except

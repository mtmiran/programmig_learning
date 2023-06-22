# Funções anonimas = lambda, função simples e declaração simples 
'''
palavra chave = lambda
arg = argumentos de entrada
expressaão = o que a função vai fazer
não precisa de nome ou retorno

lambda arg:expr
'''

# Atribuindo a vairavel
soma = lambda a,b:a+b
multiplos_valores = lambda a,b,c:(a+b)*c

# Sem atribuir a variavel
print((lambda a,b:a+b)(2,3))

# Função dentro de função
r = lambda x,func:x+func(x)    # aqui estou somando x com func e atribuindo na variavel r
res = r(2,lambda x:x*x)      # agora estou atribuindo a variavel r para a var res, onde func = lambda.....
print(res)                  # agora vou printar r onde x = 2 e func = x*x = 4

# Chamando funções
print(soma(2,3))
print(multiplos_valores(2,3,4))

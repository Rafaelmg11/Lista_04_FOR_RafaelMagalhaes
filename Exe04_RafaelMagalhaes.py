#Escreva um programa para pedir um número e em seguida o nome. Exiba o nome(uma letra de cada vez em cada linha) e repita isso para o número de vezes que o usuario digitou

num = int (input('Digite um número: '))
nome = (input('Digite seu nome: '))


for i in range(num):
    for i in nome:
        print(i)
        print('==')
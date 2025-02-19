#Faça um programa que pergunte em qual direção o usuario deseja contar se se ele quiser ir para cima ('c' ou "C" ),se para baixo ('B','b')
#---Se ele selecionar para cima pessa um número superior e conte de 1 até esse número
#---Se ele selecionar para baixo peça-lhe para inserir um número abaixo de 20, e em seguida faça contagem regressiva de 20 até esse número
#---Se ele digitar uma direção diferente  de cima ou de baixo digite a mensagem(Direção Invalida)


direcao = input("Digite em qual direção você deseja contar ('C' ou 'c' para cima ou 'B' ou 'b' para baixo): ")

direcao = direcao.lower()

if direcao == 'c':
    num = int (input("Insira um número: "))
    for i in range(1,num +1,+1):
        print(i)

elif direcao == 'b':
    num = int (input("Insira um número abaixo de 20: "))

    if num < 20:
        for i in range(20,num -1,-1):
            print(i)
    else:
        print("Número Invalido.")

else:
    print("Direção Inavalida.")

print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")

#CODIGO OK

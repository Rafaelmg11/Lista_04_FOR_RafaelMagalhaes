#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".

convidados = int (input("Digite quantos pessoas você deseja convidar para a festa: "))

if convidados <= 10:

    for i in range(convidados):
        nome = input("Digite o nome do convidado: ")
        print(nome,"está convidado pra festa")

else:
    print("Muitas Pessoas!")


print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")

#CODIGO OK

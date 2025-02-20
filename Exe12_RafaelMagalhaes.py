#LISTAS:
horario = []

#Declarando horaios:
qntdehorario = int (input("Digite quantos horarios você deseja disponibilizar hoje: "))

for i in range(qntdehorario):
    horario.append (input("Digite um horario que você deseja disponibilizar: "))

#Cliente:
print("Os horarios disponiveis são:")
print(horario)

#Descobrindo indice
escolha_horario = input("Digite o horario que você deseja agendar: ")

try:  
    indice_horario = horario.index(escolha_horario)

    #Removendo horario:
    horario.pop(indice_horario)

    print("Horario Marcado: {}".format(escolha_horario))

except:
    print("Horario Invalido")

print("")

print("Horarios disponiveis:")
print(horario)


indice = len(horario)

for i in range(indice):

    for i in enumerate(horario):
        if horario != []:
            resposta = input ("Você deseja agendar mais algum horario? ")
            resposta.lower()

            
            if resposta == 's' or resposta == 'sim':
                print("Os horarios disposniveis são:")
                print(horario)

                escolha_horario = input("Digite o horario que você deseja agendar: ")
                indice_horario = horario.index(escolha_horario)

                #Removendo horario:
                horario.pop(indice_horario)

                print("Horario Marcado: {}".format(escolha_horario))

                if horario == []:
                    print("Não existem mais horarios Disponiveis")

            if resposta == 'n' or resposta == 'nao':
                print("Encerrando o Sistema...")
                exit()

        if resposta == 'n' or resposta == 'nao':
                print("Encerrando o Sistema...")
                exit()
#Você é um desenvolvedor de sistemas trabalhando em um projeto para um salão de beleza. O salão precisa de um sistema para gerenciar os horários de atendimento dos clientes. 
# Primeiro, a dona do salão monta a grade horária da agenda. Depois, uma cliente deseja agendar um horário, e o sistema exibe os horários disponíveis. 
# A dona do salão então agenda o horário escolhido pela cliente, e o horário escolhido não estará mais disponível. 
# O sistema deve continuar permitindo agendamentos até que todos os horários disponíveis sejam preenchidos ou até que a dona do salão decida parar.
#Desenvolva um programa em Python que:
#1.	Solicite à dona do salão para inserir os horários disponíveis na agenda.
#2.	Exiba os horários disponíveis para a cliente.
#3.	Permita que a cliente escolha um horário para agendamento.
#4.	Atualize a agenda marcando o horário escolhido como ocupado.
#5.	Pergunte se deseja agendar mais um horário e continue até que todos os horários estejam preenchidos ou a dona do salão decida parar.

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
escolha_horario = input("Digite o horario que você deseja: ")
indice_horario = horario.index(escolha_horario)

#Removendo horario:



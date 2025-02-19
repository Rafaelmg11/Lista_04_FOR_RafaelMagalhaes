#defina uma variavel chamada total como 0. 
# Peça ao ususario para inserir 5 números e, apos cada entrada pergunte se ele deseja se esse numero seja incluido('S' ou 's', 'N' ou 'n')
#Se ele desejar adicone o número ao total. Se ele nao quiser inclui-lo nao o adicone ao total. Depos de inserir 5 n´´úmeros exiba o total

total = 0

for i in range(5):
    num = int (input("Digite um número: "))
    resposta =  str (input("Digite se você deseja que esse número seja incluido no total('S' para sim, 'N' para não): "))
    resposta = resposta.lower()
    if resposta == 's':
        total = total + num

print("Total: {} ".format(total))

print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")

#CODIGO OK
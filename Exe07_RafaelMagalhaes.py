#Peça ao usuario para inserir seu nome e um número. Se o número for menor que 10 exiba o nome dele esse numero de vezes, 
# caso ao contrario exiba a mensagem "número muito alto"(TRES VEZES) 

nome = (input("Digite seu nome: "))
num = int (input("Digite um número menor que 10: "))

if num < 10:
    for i in range(num):
        print(nome)
else:
    for i in range(3):
        print("Número muito alto!")

print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")

#CODIGO OK

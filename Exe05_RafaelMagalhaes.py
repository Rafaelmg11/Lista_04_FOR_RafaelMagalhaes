#Peça ao usuario para inserir um número que deseja a tabuada e em seguida exiba a tabuada para esse número

num = int (input("Digite o número que você deseja saber a tabuada: "))

for i in range(11):
    tabuada = num * i
    x = num * i
    print(num,"X",i,"=",tabuada)


#Peça um número a baixo de 50 e em seguida faça uma contagem regressiva até esse número, certificando-se , 
# de demonstrar o número que ele inseriu a saida 

num = int (input("Digite um número a baixo de 50: "))

if num < 50:
     for i in range(50,num - 1, -1):
          print(i)
else:
     print("Número Invalido")

print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")

#CODIGO OK
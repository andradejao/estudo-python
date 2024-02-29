# Um número é pedido e verifica se é par ou impar
numero = input("Digite um número inteiro: ")
# Necessário converção de texto(str) para número(int). A função input sempre retorna o valor em formato de texto 
numero = int(numero)


if(numero % 2 == 0):
    print("O número é par")
else:
    print("O número digitado é impar")
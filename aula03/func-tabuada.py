def tabuada(num = 0):
    arq = open("tabuada.txt", "a")
    for i in range(1,11):
        arq.write(str(num) + "x" + str(i) + "=" + str(num * i)+ "\n")
    arq.close()

n = input("Digite um número para a criação da tabuada: ")
tabuada(int(n))

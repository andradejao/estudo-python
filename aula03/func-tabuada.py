def tabuada(n = 0):
    arq = open("tabuada.txt", "a")
    for i in range(1,11):
        arq.write(str(n) + "x" + str(i) + "=" + str(n * i)+ "\n")
    arq.close()

n = input("Digite um número para a criação da tabuada: ")
tabuada(int(n))

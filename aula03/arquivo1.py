arq = open("dados.txt", "a",)       # A função "open" permite abrir um arquivo, ler ou escrever no arquivo
arq.write("Olá\n")                  # A função "write" permite escrever em um arquivo
arq.close()                         # A função "close" fecha o arquivo e o retira da memória

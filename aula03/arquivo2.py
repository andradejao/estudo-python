nome_arquivo = input("Digite o nome do arquivo: ")
extensao_arquivo = input("Digite a extensão do arquivo: ")
conteudo = input("Digite o conteúdo do arquivo: ")

arq = open(nome_arquivo+"."+extensao_arquivo, "a")
arq.write(conteudo)
arq.close
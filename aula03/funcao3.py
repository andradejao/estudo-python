def criaArquivo(nome = "", ext = "", cont = "")->str:
    """A função criaArquivo recebe o nome
    do arquivo, a extensão e um conteúdo para o arquivo,
    e cria este arquivo no diretório local"""
    f = open(nome + "." +ext, "a")
    f.write(cont)
    f.close()
    return "Arquivo criado com sucesso"

print(criaArquivo("teste","txt","Olá, este é um texto tá?"))

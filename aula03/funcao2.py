def desconto(preco = 0.0, taxa = 0.0):
    """A função desconto realiza o cálculo
    de desconto recebendo o valor do preço de um produto
    e multiplica pelo valor da taxa e exibe o resultado 
    em tela no final"""
    desc = preco * (taxa / 100)
    total = preco - desc
    print(f"O valor de desconto é {desc} e o valor final é {total}")


desconto(800, 7)

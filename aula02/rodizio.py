print("\nEste programa serve para analisar se um veículo poderá rodar em um determinado dia da semana \n")
digito = input("Digite o último dígito da placa do veículo: ")

match digito:
    case '1' | '2':  
        print("\nSeu carro não poderá rodar na segunda-feira \n")
    case '3' | '4':
        print("\nSeu carro não poderá rodar na terça-feira \n")
    case '5' | '6':
        print("\nSeu carro não poderá rodar na quarta-feira \n")
    case '7' | '8':
        print("\nSeu carro não poderá rodar na quinta-feira \n")
    case '9' | '0':
        print("\nSeu carro não poderá rodar na sexta-feira \n")


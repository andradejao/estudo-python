print("Este programa analisa os valores digitados de 0 a 6 e diz o dia da semana \n")
digito = input("Digite um número de 0 a 6: ")

match digito:
    case '0':       # Utilize o símbolo "|" para usar duas variáveis para o mesmo case
        print("Domingo")
    case '1':
        print("Segunda-Feira")
    case '2':
        print("Terça-Feira")
    case '3':
        print("Quarta-Feira")
    case '4':
        print("Quinta-Feira")
    case '5':
        print("Sexta-Feira")
    case '6':
        print("Sábado")
    case '_':
        print("Valor incorreto. Tente um número de 0 a 6")

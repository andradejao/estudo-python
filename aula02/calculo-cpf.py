print("\nPrograma para verificar se o CPF digitado é válido\n")

cpf_usu = input("Digite o seu CPF: ")   # Variável que guarda o CPF do usuário
peso10 = 10                             # Variável que serve para calcular o peso de 10 até 2
rs = 0                                  # Variável que guarda a soma das multiplicações entre os dígitos de CPF e os pesos 

for i in range(0,9):                    # Para obter os 9 primeiros dígitos do CPF foi usado "for" com uma contagem de 0 até 9
    print(cpf_usu[i])                   # Exibe um dígito do CPF por vez
    print(int(cpf_usu[i])*peso10)
    rs+=(int(cpf_usu[i])*peso10)        # Para calcular um dígito por vez com o peso, se converteu cada dígito em "int", depois, os resultados
                                        #foram somados e armazenados na variável "rs"
    peso10-=1                           # Sempre que o loop "for" rodar, será subtraído o valor 1 da variável "peso10"

print(rs)                               # Exibição do resultado encontrado
resto = rs % 11                         # Variável que guarda o resto da divisão

if(resto < 2):                          # Se o resto da divisão for menor que 2, o primeiro dígito será 0. Se não for, deverá subtrair 11 pelo valor 
                                        #encontrado em "rs"
    print("Primeiro dígito é 0")
else:
    print("Primeiro dígito é "+str(11-resto))

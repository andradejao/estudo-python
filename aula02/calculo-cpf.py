print("\nPrograma para verificar se o CPF digitado é válido\n")

cpf_usu = input("Digite o seu CPF: ")   # Variável que guarda o CPF do usuário
cpf_calc = ""                           # Variável que guarda o CPF que está calculando
peso10 = 10                             # Variável que serve para calcular o peso de 10 até 2
peso11 = 11                             # Variável que serve para calcular o peso de 11 até 2
rs = 0                                  # Variável que guarda a soma das multiplicações entre os dígitos de CPF e os pesos 

for i in range(0,9):                    # Para obter os 9 primeiros dígitos do CPF foi usado "for" com uma contagem de 0 até 9
    print(cpf_usu[i])                   # Exibe um dígito do CPF por vez
                                        # Adiciona a variável "cpf_calc" os nove primeiros dígitos do CPF e adiciona o primeiro dígito verificador adiante
    print(int(cpf_usu[i])*peso10)
    rs+=(int(cpf_usu[i])*peso10)        # Para calcular um dígito por vez com o peso, se converteu cada dígito em "int", depois, os resultados
    cpf_calc += cpf_usu[i]                                    #foram somados e armazenados na variável "rs"
    peso10-=1                           # Sempre que o loop "for" rodar, será subtraído o valor 1 da variável "peso10"

print(rs)                               # Exibição do resultado encontrado
resto = rs % 11                         # Variável que guarda o resto da divisão

if(resto < 2):                          # Se o resto da divisão for menor que 2, o primeiro dígito será 0. Se não for, deverá subtrair 11 pelo valor 
                                        #encontrado em "rs"
    print("Primeiro dígito é 0")
    cpf_calc += "0"
else:
    print("Primeiro dígito é "+str(11-resto))
    cpf_calc += str(11-resto)

rs = 0
for i in range(0,10):
    rs += int(cpf_calc[i]*peso11)

resto = rs % 11
if(resto < 2):
    cpf_calc += "0"
else:
    cpf_calc += str(11-resto)


# Valida se o CPF digitado é igual ao CPF calculado

if(cpf_usu == cpf_calc):
    print("CPF válido")
else:
    print("CPF inválido")

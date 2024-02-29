n1 = input("Digite a primeira nota do aluno: ")
n2 = input("Digite a segunda nota do aluno: ")
n3= input("Digite a terceira nota do aluno: ")
n4 = input("Digite a quarta nota do aluno: ")
rs = ( int(n1) + int(n2) + int(n3) + int(n4) ) / 4
# Se o aluno tiver uma média acima ou igual a 7, estará aprovado.
# Se o aluno tiver uma média abaixo ou igual a 4, estará reprovado.
# Se a média não se aplicar a essas duas regras, o aluno estará em recuperação.



if(rs >= 7):
    print("O aluno está aprovado com média "+str(rs)+" \n")
elif(rs <= 4):
    print("O aluno está reprovado com média "+str(rs)+" \n")
else:
    print("O aluno está em recuperação com média "+str(rs)+" \n")

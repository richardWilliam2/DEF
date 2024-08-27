# Criar um programa que calcule a média de um aluno
# Solicite as notas ao usuario. O programa deve:


# Ultilizar uma função para calcular a média.
# Validadr os dados de entrada, garantindo que sejam números. 
# tratar o caso em que o usuario digite um numero negativo
# Exibir a media calculada 

try:
    def media(n1,n2,n3):
        soma = n1+n2+n3
        divi = soma/2
        print("A sua media é:" + str(divi))
    
    n1 = int(input("Digite a sua primeira nota: "))
    n2 = int(input("Digite a sua segundo nota: "))
    n3 = int(input("Digite a sua terceiro nota: "))

    cal = media(n1,n2,n3)
    print(f"{cal}")

except:
    print("Digite apenas numeros !!!!")

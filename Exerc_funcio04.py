# Faça um programa com uma função
# que, necessite de três argumentos
# e que retorne a soma desses três argumentos

def mult (n1,n2,n3):
     multiplicação = n1*n2*n3
     return (multiplicação)

n1 = float(input(f"Digite o primeiro numero: "))
n2 = float(input(f"Digite o segundo numero: "))
n3 = float(input(f"Digite o terceiro numero: "))

resultado = mult (n1,n2,n3)
print(f" O Resultado é: {resultado}")


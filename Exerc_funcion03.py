# Função com pareamento e retorno 
def numero(num):
    if num % 2 == 0 : 
        return "PAR"
    else:
        return "IMPAR"

resultado = numero(int(input("Digite um numero")))
print(resultado)
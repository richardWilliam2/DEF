try:
    dividendos = int (input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    resultado = dividendos/divisor

except ValueError:
    print("Numero digitado invalido")

except ZeroDivisionError:
    print("Divisão por zero não permitida")
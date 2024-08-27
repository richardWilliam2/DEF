def area(altura,base):
    ab = int(altura*base)
    area = (ab*0.02)
    print("A area do seu tringulo e de: " + str(area))

altura = int(input("Digite a altura do tringulo: "))
base = int(input("Digite a base do triangulo: "))

Resultado = area(altura,base)
print(f"{Resultado}")
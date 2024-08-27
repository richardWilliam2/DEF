def rea(salario):
    if salario >= 5000:
        print(f"Seu salario tera um reajuste de ate 10%")
        reajuste = float(salario*0.10)
        print(f"o reajustre e de: "+ str(reajuste))
        print(f"O seu reajuste salario e de ate: " + str(salario+reajuste))
    elif salario <= 5000:
        print(f"Seu salaria tera um Reajuste de ate 15%")
        reajust = float(salario*0.15)
        print(f"O o reajuste sera de: " + str(reajust))
        print(f"O seu reajuste salarial e de ate: " + str(salario + reajust))


salario = int(input(f"Qual e o seu salario ?: "))

Reajsalarial = rea(salario)
print= (f"{Reajsalarial}")
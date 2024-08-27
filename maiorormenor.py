def ni(nome, idade):
    if idade >= 18:
        print("Seu nome é: "+nome)
        print("você e maior de idade")
    else:
        print("Você não e permitido por ser menor de idade")
    return (idade)

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

conta = ni(nome,idade)
print(f"{conta}")

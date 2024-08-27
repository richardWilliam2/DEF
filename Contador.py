def contador(início, fim, passo):
    if passo == 0:
        print("O passo não pode ser zero.")
        return
    if início < fim:
        print(f"Contagem de {início} até {fim}, de {passo} em {passo}:")
        for i in range(início, fim + 1, passo):
            print(i, end=' ')
        print() 
    else:
        print(f"Contagem de {início} até {fim}, de {-passo} em {-passo}:")
        for i in range(início, fim - 1, -passo):
            print(i, end=' ')
        print()
contador(1, 10, 1)
contador(10, 0, 2)

    
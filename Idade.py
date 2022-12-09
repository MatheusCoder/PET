idades = int(input("Insira a idade:"))
contador = 0
soma = 0
while idades >= 0:
    idades = int(input("Insira a idade:"))
    if idades >= 0:
        contador = contador + 1
        soma = soma + idades
media = soma / contador
print("A média é", media)

def calculaSalario(salarioBruto):
    descINSS = salarioBruto * 0.11
    descIR = (salarioBruto - descINSS) * 0.15
    salarioLiquido = (salarioBruto - descINSS - descIR)
    return salarioLiquido

x = calculaSalario(1212)
print (x)
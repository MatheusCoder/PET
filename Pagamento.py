def valorPagamento(valor, dias):
    juros = 0
    if dias == 0:
        return valor
    else:
        juros = 0.1 * dias

        return valor + ((3 * valor)/100) + juros 

total = 0
contador = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        break
    dias = int(input('Digite o número de dias em atraso: '))
    total += valorPagamento(valor, dias)
    contador += 1

print('Quantidade total de prestações no dia: %d' % contador)
print('Valor total das prestações: %.2f' % total)

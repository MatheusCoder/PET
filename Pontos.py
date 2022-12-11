import math
def xesque(ponto1x, ponto1y, ponto2x, ponto2y):
    result = math.sqrt(math.pow((ponto2x-ponto1x),2)+math.pow(ponto2y-ponto1y,2))
    return result

listaPontos = []

for i in range(5):
    x = float(input("informe o x do ponto:"))
    listaPontos.append(x)
    y = float(input("informe o y do ponto:"))
    listaPontos.append(y)

dist = xesque(listaPontos[0], listaPontos[1], listaPontos[8], listaPontos[9])
print(dist)  

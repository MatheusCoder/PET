par = 0
impar = 0
for i in range (5):
    num = int(input('digite o número: '))
    if num%2 == 0:
        par = par+1
    else:
        impar = impar+1
     
print("os pares são:", par)
print("os ímpares são:", impar)

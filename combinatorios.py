def isint(n):
    if n==int(n):
        return True
    return False
def factorial(n):
    if isint(n)==False or n<0:
        return "Valor incorrecto"
    if n==0:
        return 1
    a=1
    for i in range(n):
        a=a*(i+1)
    return a
def comb(n,k):
    if factorial(n)=="Valor incorrecto" or factorial(k)=="Valor incorrecto" or k>n:
        return "Valores incorrectos"
    x=factorial(n)
    y=factorial(k)*factorial(n-k)
    return x//y

print("Introduzca n:")
n=int(input())
while factorial(n)=="Valor incorrecto":
    print("Valor incorrecto. Vuelva a introducir n:")
    n=int(input())
print("Introduzca k:")
k=int(input())
a=comb(n,k)
while a=="Valores incorrectos":
    print("Valor incorrecto. Vuelva a introducir k:")
    k=int(input())
    a=comb(n,k)
print(f"El número combinatorio {n} sobre {k} es: {a}")
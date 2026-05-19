from sympy import isprime

print("Introduzca un número entero positivo 'n':")
n=int(input())

primos=[]
for j in range(n):
    if isprime(j+1)==True:
        primos.append(j+1)

print(f"En la factorización de {n}! (el factorial de {n}), la lista de primos es:  {primos}")

potencias=[]
for p in primos:
    a=0
    i=1
    while n//p**i >=1:
        i=i+1
    for k in range(i):
        a=a+n//p**(k+1)
    potencias.append(a)

print(f"mientras que la lista de sus respectivas potencias es: {potencias}")
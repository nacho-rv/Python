def IsInt(u):
    if u==int(u):
        return True
    return False

def baseb(n,b):
    if n<0 or b<=1 or IsInt(n)==False or IsInt(b)==False:
         return False
    if n==0:
         lista0=[0]
         return lista0
    a=n 
    r=a
    lista=[]
    lista2=[]
    k=1
    while a>=b**k:
         k+=1
    for i in range(k):
            if a<b**(i+1) and a>=b**i :
                j=i 
    if j==0:
          lista.append(r)
          return lista           
    while j>0 :
         aux=r
         r=  r%(b**j) 
         c=aux//(b**j)
         lista.append(c) 
         j=j-1
    lista.append(r)
    return lista

def debasebadeci(x,b):
    if b<=1 or IsInt(b)==False:
         return False
    if len(x)==0:
         return False
    k=0
    for j in range(len(x)):
         if x[j]>=b or x[j]<0 or IsInt(x[j])==False:
              k+=1
    if k>0:
         return False
    y=0
    for i in range(len(x)):
         y=y+x[i]*(b**(len(x)-1-i))
    return y

print("Introduzca una base mayor que 1:")
b=int(input())
while b<2:
     print("Inténtelo de nuevo:")
     b=int(input())
print("Introduzca un entero sin signo:")
n=int(input())
a=baseb(n,b)
while a==False:
     print("Inténtelo de nuevo:")
     n=int(input())
     a=baseb(n,b)
print(f"{n} en base {b} es: {baseb(n,b)}")
print("Introduzca nuevamente una base mayor que 1:")
b=int(input())
while b<2:
     print("Inténtelo de nuevo:")
     b=int(input())
print(f"Introduzca los dígitos de un número en base {b}, separados por comas:")
x=input()
x=x.split(',')
for i in range(len(x)):
     x[i]=int(x[i])
while debasebadeci(x,b)==False:
     print(f"Inténtelo de nuevo:")
     x=input()
     x=x.split(',')
     for i in range(len(x)):
      x[i]=int(x[i])
print(f"El número que ha introducido es en base 10: {debasebadeci(x,b)}")
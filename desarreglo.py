def IsInt(w):
 if w==int(w):
  return True
 return False


def desarreglo(s):
 if IsInt(s)==False or s<=0:
  return "NO"
 if s==1:
  return 0
 if s==2:
  return 1
 a=0
 b=1
 for i in range(s-2):
  d=b
  b=(a+b)*(i+2)
  a=d
 return b

n=0
while desarreglo(n)=="NO":
 print("Introduzca un entero positivo:")
 n=int(input())
print(f"El número de combinaciones para el amigo invisible con {n} personas es: {desarreglo(n)}")
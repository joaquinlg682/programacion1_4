print("EJERCICIO 1")

for num in range(0,101):
    print(num)


print("EJERCICIO 2")

num2=int(input("Ingrese un número para saber la cantidad de digitos que tiene: "))

contador=0
n=num2

while n>0:
    n=n//10

    contador+=1

print(f"la cantidad de digitos que tiene es: {contador}")


print("EJERCICIO 3")

num=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))

contador=0

for i in range(num+1,num2):
    contador=contador+i
    print(contador)


print("EJERCICIO 4")

num=int(input("ingrese numeros que quiera sumar(si ingresa 0 el programa se detiene): "))

total=num

while num!=0:
    num=int(input("ingrese otro numero: "))
    total=total+num
    print(total)
print(f"el numero final es: {total}")


print("EJERCICIO 5")

import random

computadora=random.randint(0,9)

jugador=int(input("adivina el numero entre 0 y 9: "))
intentos=1

while jugador != computadora:
    jugador=int(input("erraste, ingrese nuevamente otro numero: "))
    intentos+=1

print(f"¡Felicidades :D! El numero era: {computadora}")
print(f"Tus intentos fueron: {intentos}")


print("EJERCICIO 6")

for num in range(100,0, -2):
    print(num)


print("EJERCICIO 7")

num=int(input("Ingrese un numero: "))

total=0

for i in range(0,num+1):
    total=total+i
print(f"el total de las sumas es: {total}")


print("EJERCICIO 8")

pares=0
impares=0
positivos=0
negativos=0

cantidad=100

for i in range(cantidad):
    num=int(input(f"ingrese el número {i+1}: "))
    
    if num % 2==0:
        pares+=1
    else:
        impares+=1
    
    if num>0:
        positivos+=1
    else:
        negativos+=1

print(f"Números pares:{pares}")
print(f"Números impares:{impares}")
print(f"Números positivos:{positivos}")
print(f"Números negativos:{negativos}")


print("EJERCICIO 9")

suma=0
cantidad=100

for i in range(cantidad):
    num=int(input(f"ingrese el número {i+1}: "))

    suma+=num

media=suma/cantidad

print(f"la media de los 100 numeros es: {media}")


print("EJERCICIO 10")

num=int(input("Ingrese un número: "))
invertido=0

while num>0:
    digito=num%10
    invertido=invertido*10+digito
    num//=10

print(f"El número invertido sería: {invertido}")
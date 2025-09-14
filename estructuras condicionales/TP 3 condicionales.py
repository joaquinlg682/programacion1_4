print("EJERCICIO 1")

edad=int(input("ingrese su edad: "))

if edad>=18:
    print("usted es mayor de edad")
else:
    print("usted es menor de edad")


print("EJERCICIO 2")

nota=float(input("ingrese su nota: "))

if nota>=6:
    print("aprobado")
else:
    print("desaprobado")


print("EJERCICIO 3")

num=int(input("ingrese un numero par: "))

if num%2==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


print("EJERCICIO 4")

edad2=int(input("ingrese su edad: "))

if edad2<12:
    print("usted es niño/a")
elif edad2>=12 and edad2<18:
    print("usted es adolecente")
elif edad2>=18 and edad2<30:
    print("usted es adulto joven")
elif edad2>=30:
    print("usted es un adulto")


print("EJERCICIO 5")

contraseña=input("ingrese su contraseña (Debe de tener entre 8 a 14 caracteres): ")

if 8<=len(contraseña)<=14:

    print("ha ingresado una contraseña correcta")
else:
    print("ha ingresado una contraseña incorrecta")


print("EJERCICIO 6")

import statistics

import random

numeros_aleatorios=[random.randint(1,100) for i in range (50)]

media=statistics.mean(numeros_aleatorios)
mediana=statistics.median(numeros_aleatorios)
moda=statistics.mode(numeros_aleatorios)

print(f"numeros: {numeros_aleatorios}")
print(f"la media es: {media}")
print(f"la mediana es: {mediana}")
print(f"la moda es: {moda}")

if media>mediana>moda:
    print("es una distribucion con sesgo positivo")
elif moda>mediana>media:
    print("es una distribucion con sesgo negativo")
else:
    print("es una distribucion simetrica")


print("EJERCICIO 7")

frase=input("ingrese una frase o palabra: ")

ultima_letra=frase[len(frase)-1].lower()

if ultima_letra in ["a", "e","i","o","u"]:
    print(frase+"!")
else:
    print(frase)


print("EJERCICIO 8")

nombre=input("ingrese su nombre: ")
opciones_nombre=int(input("ingrese que le gustaria hacer con su nombre. 1 para poner las letras en mayusculas, 2 para poner las letras en minusculas y 3 para que solo la primer letra tenga mayusculas: "))

if opciones_nombre==1:
    print(nombre.upper())
elif opciones_nombre==2:
    print(nombre.lower())
elif opciones_nombre==3:
    print(nombre.title())
else:
    print("ingrese un numero valido")


print("EJERCICIO 9")

escala=float(input("ingrese la escala del terremoto: "))

if escala<3:
    print("muy leve (imperceptible)")
elif escala>=3 and escala<4:
    print("leve (ligeramente perceptible)")
elif escala>=4 and escala<5:
    print("moderado (sentido por personas, pero generalmente no causa daño)")
elif escala>=5 and escala<6:
    print("fuerte (puede causar daños en estructuras debiles)")
elif escala>=6 and escala<7:
    print("muy fuerte (puede causar daños significativos)")
elif escala>=7:
    print("extremo (puede causar graves daños a gran escala)")


print("EJERCICIO 10")

hemisferio=input("¿en que hemisferio se encuentra? (norte/sur): ")
mes=int(input("¿En que mes estas? (1-12): "))
dia=int(input("¿Que dia es? (1-31): "))

hemisferio.lower()

estacion=""

if hemisferio == "norte":
    if (mes==12 and dia >=21) or mes in [1, 2] or (mes==3 and dia<= 20):
        estacion="invierno"
    elif (mes==3 and dia >=21) or mes in [4,5] or (mes==6 and dia <=20):
        estacion="primavera"
    elif (mes==6 and dia >=21) or mes in [7,8] or (mes==9 and dia <=20):
        estacion="verano"
    elif (mes==9 and dia >=21) or mes in [10,11] or (mes==12 and dia <=20):
        estacion="otoño"

if hemisferio == "sur":
    if (mes==12 and dia >=21) or mes in [1, 2] or (mes==3 and dia<= 20):
        estacion="verano"
    elif (mes==3 and dia >=21) or mes in [4,5] or (mes==6 and dia <=20):
        estacion="otoño"
    elif (mes==6 and dia >=21) or mes in [7,8] or (mes==9 and dia <=20):
        estacion="invierno"
    elif (mes==9 and dia >=21) or mes in [10,11] or (mes==12 and dia <=20):
        estacion="primavera"

print(f"en el hemisferio {hemisferio} se encuentra ,segun la fecha, en: {estacion}")
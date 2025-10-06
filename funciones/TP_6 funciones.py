import math

print("EJERCICIO 1")

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

print("----------------")

print("EJERCICIO 2")

def saludar_usuario(nombre):
    print(f"hola {nombre}!")

nombre = input("ingrese su nombre: ")
saludar_usuario(nombre)

print("-------------------")

print("EJERCICIO 3")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
residencia = input("ingrese donde vive: ")

informacion_personal(nombre, apellido, edad, residencia)

print("-------------------")

print("EJERCICIO 4")

def calcular_area_circulo(radio):
    area = math.pi * radio**2

    print(f"el área es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio

    print(f"el perimetro es: {perimetro}")

radio = float(input("ingrese el radio del circulo: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print("-------------------")

print("EJERCICIO 5")

def segundos_a_horas(segundos):
    minutos = segundos/60
    horas = minutos/60
    horas = math.trunc(horas)
    print(f"en total son: {horas} hora/s")

segundos = int(input("ingrese una cantidad de segundos: "))
segundos_a_horas(segundos)

print("------------------------")

print("EJERCICIO 6")

def tabla_multiplicar(numero):
    for i in range(11):
        print(numero * i)

numero = int(input("ingrese un numero: "))
tabla_multiplicar(numero)

print("------------------------")

print("EJERCICIO 7")
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicar=a*b
    dividir=a/b
    print(f"los numeros sumados son: {suma}")
    print(f"los numeros restados dan: {resta}")
    print(f"los numeros multiplicados dan: {multiplicar}")
    print(f"los numeros divididos dan: {dividir}")

a = int(input("ingrese un número: "))
b = int(input("ingrese otro número: "))

operaciones_basicas(a,b)

print("---------------------------")

print("EJERCICIO 8")

def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    print(f"su indice de masa corporal es:  {imc}")
peso = float(input("ingrese su peso: "))
altura = float(input("ingrese su altura:  "))

calcular_imc(peso, altura)

print("---------------------------")

print("EJERCICIO 9")

def celsius_a_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius} celsius serian: {farenheit} farenheit")

celsius = float(input("ingrese la temperatura en grados celsius: "))

celsius_a_farenheit(celsius)

print("---------------------------")

print("EJERCICIO 10")

def calcular_promedio(a,b,c):
    promedio = (a+b+c)/3
    print(f"El promedio de los tres numeros es: {promedio}")

a = int(input("ingrese el valor del primer número: "))
b = int(input("ingrese el valor del segundo número: "))
c = int(input("ingrese el valor del tercer numero: "))

calcular_promedio(a,b,c)
print("EJERCICIO 1")

precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precio_frutas['Naranja'] = 1200
precio_frutas['Manzana'] = 1500
precio_frutas['Pera'] = 2300

print(precio_frutas)


print("---------------------------")

print("EJERCICIO 2")

precio_frutas['Banana'] = 1330
precio_frutas['Manzana'] = 1700
precio_frutas['Melón'] = 2800

print(precio_frutas)

print("---------------------------")

print("EJERCICIO 3")

print(precio_frutas.keys())


print("--------------------------")

print("EJERCICIO 4")

contactos = {}

for i in range(5):
    nombre = input(f"ingresá el nombre del contacto {i+1}: ")
    numeros =input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numeros


consultar =input(f"ingrese el nombre de la persona que desea saber su número: ")

if consultar in contactos:
    precio_frutas(f"el numero de {consultar} es: {contactos[consultar]}")
else:
    print(f"El nombre '{consultar}' no está disponible")


print("--------------------------")

print("EJERCICIO 5")

frase = input("ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print(f"palaras unicas: {palabras_unicas}")

frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(f"Frecuencia de cada palabra: {frecuencias}")


print("--------------------------")

print("EJERCICIO 6")

alumnos = {}

for i in range(3):
    nombre = input(f"ingresa el nombre del alumno {i+1}: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    notas = (nota1,nota2,nota3)

    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio del alumno {nombre} es de: {promedio:.2f}")


print("--------------------------")

print("EJERCICIO 7")


parcial1 = {"Ares", "Ismael", "Peque", "Zani"}
parcial2 = {"Ares", "Varela", "Ismael", "Tomás"}

ambos = parcial1 & parcial2
print(f"Los que aprobaron los dos parciales han sido: {ambos}")

solo_uno = parcial1 ^ parcial2
print(f"Los que aprobaron solo un parcial son: {solo_uno}")

al_menos_uno = parcial1 | parcial2
print(f"Los que al menos han aprobado un parcial fueron: {al_menos_uno}")


print("--------------------------")

print("EJERCICIO 8")

productos = {}

producto = input("ingrese el nombre del producto: ")

if producto in productos:
    print(f"el producto {productos[producto]} tiene {productos} unidades")
    agregar = int(input("¿Cuantas unidades quiere ingresar?: "))
    productos[producto] += agregar
    print(f"cantidad nueva de {producto}: {productos[producto]} unidades")
else:
    print(f"el producto {producto} no se encuentra")
    nuevo = int(input("¿Cuantas unidades quiere agregar?: "))
    productos[producto] = nuevo
    print(f"El producto {producto} ha sido agregado con {nuevo} unidades")


print("--------------------------")

print("EJERCICIO 9")

agenda = {
    ("lunes", "08:00"): "universidad",
    ("martes", "11:30"): "examen de org empresarial",
    ("miercoles", "16:00"): "gimnasio",
    ("jueves", "20:00"): "clases de curtir el mambo piola tranki y sin berretin",
    ("viernes", "16:00"): "gimnasio",
    ("sabado", "13:00"): "gimnasio",
    ("domingo", "12:00"): "dormir",
}

dia = input("ingrese el dia: ")
hora = input("ingrese la hora: ")

consulta = (dia, hora)

if consulta in agenda:
    print(f"A las {hora} del {dia} tenés: {agenda[consulta]}")
else:
    print(f"No hay actividades registradas el {dia} a las {hora}")


print("--------------------------")

print("EJERCICIO 10")

original = {
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago", 
    "Perú": "Lima", 
    "Mexico": "Ciudad de mexico", 
    "España": "Madrid"
    }

invertidos = {capital: pais for pais, capital in original.items()}

print(original)
print(invertidos)

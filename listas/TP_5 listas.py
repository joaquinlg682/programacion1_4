print("EJERCICIO 1")

lista=list(range(4,101,4))
print(lista)

print("EJERCICIO 2")

lista=[ "Eau de toilette", "Eau de parfum", "Parfum", "Absolu", "Elixir" ]
print(lista[-2])

print("EJERCICIO 3")

lista_vacia=[]

palabra1=input("ingrese cualquier palabra: ")
lista_vacia.append(palabra1)

palabra2=input("ingrese otra palabra: ")
lista_vacia.append(palabra2)

palabra3=input("introduzca una ultima palabra: ")
lista_vacia.append(palabra3)

print(lista_vacia)


print("EJERCICIO 4")

animales=["perro","gato","conejo","pez"]

animales.remove("pez")

animales.append("loro")

animales.append("oso")

print(animales)


print("EJERCICIO 5")

numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

print("la lo que hizo la linea: numeros.remove(max(numeros)) fue sacar al número mas grande de la lista")

print("EJERCICIO 6")

lista=list(range(10,31,5))
print(lista[:2])


print("EJERCICIO 7")

autos=["sedan", "polo", "suran", "gol"]
autos[1:3] = ["Jesko", "Masda"]
print(autos)


print("EJERCICIO 8")

dobles=[]

num=5*2
dobles.append(num)

num1=10*2
dobles.append(num1)

num2=15*2
dobles.append(num2)

print(dobles)

print("EJERCICIO 9")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")

print(compras)

print("EJERCICIO 10")

lista_anidada=[15,True,[25.5,57.9,30.6], False]

print(lista_anidada)

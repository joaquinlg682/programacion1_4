import csv
import os

#Funciones

def menu():

    while True:

        print("== Menu de productos == \n")

        print("|1| Mostrar todos los productos registrados")
        print("|2| Agregar nuevo producto ")
        print("|3| Eliminar un producto existente")
        print("|4| Salir del programa \n")

        opc = input("ELige una opcion: ")

        match opc:

            case "1":
                opcion_1()

            case "2":
                opcion_2()

            case "3":
                opcion_3()
                pass

            case "4":
                print("chau chau...")
                break
            case _:
                print("opcion no válida")


def opcion_1():

    with open("productos.csv", "r") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            print(f"{fila['producto']}  | precio: {fila['precio']}")

def opcion_2():
    
    producto = input("Ingrese el producto nuevo: ").lower()
    precio = int(input("Ingrese el precio del producto: "))

    

    with open("productos.csv", "a", newline="") as archivo:
        campos = ["producto", "precio"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow({"producto": producto, "precio": precio})


def opcion_3():

    producto_eliminado = input("Ingrese el producto a eliminar: ").lower()
    productos_actualizados = []
    encontrado = False

    try:
        with open("productos.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila["producto"].lower() != producto_eliminado:
                    productos_actualizados.append(fila)
                else:
                    encontrado = True

        with open("productos.csv", "w", newline="") as archivo:
            campos = ["producto", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos_actualizados)

        if encontrado:
            print(f"producto eliminado")

        else:
            print(f"producto no encontrado")

    except FileNotFoundError:
        print("El archivo de productos no existe")

#PRINCIPAL

productos = [
    {"producto": "galletas", "precio": 1000},
    {"producto": "papa", "precio": 100},
    {"producto": "camote", "precio": 10}
]

if not os.path.exists("productos.csv"):
    with open("productos.csv", "w", newline = "")as archivo:
        campos = ["producto", "precio"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)

menu()

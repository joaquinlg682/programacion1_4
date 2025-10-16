print("EJERCICIO 1")

with open("productos.txt", "w") as archivo_producto:
    archivo_producto.write("Jean Paul Gaultier Le Male Elixir,2000,3\n")
    archivo_producto.write("Jean Paul Gaultier Le Male Le Parfum,20000,8\n")
    archivo_producto.write("Jean Paul Gaultier Le Beau,3000,9\n")


print("------------------------------------------------")

print("EJERCICIO 2")

with open("productos.txt", "r") as archivo_producto:
    for linea in archivo_producto:
        linea = linea.strip()
        partes = linea.split(",")

        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]

        print(f"producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


print("------------------------------------------------")

print("EJERCICIO 3")


nuevo_nombre = input("Ingrese el nombre de un nuevo producto: ")
nuevo_precio = input("Ingrese el nuevo precio para el producto: ")
nueva_cantidad = input("Ingrese la cantidad del nuevo producto: ")

with open("productos.txt", "a") as archivo_producto:
    archivo_producto.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")


print("------------------------------------------------")

print("EJERCICIO 4")

productos = [


]

with open("productos.txt", "r") as archivo_producto:
    for linea in archivo_producto:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")

        precio = float(precio)
        cantidad = int(cantidad)

        producto_dict = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        if not any(p["nombre"] == nombre for p in productos):
            productos.append(producto_dict)


print("------------------------------------------------")

print("EJERCICIO 5")

producto_buscado = input("ingrese el nombre del producto que desea buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == producto_buscado.lower():
        print(f"El producto {p['nombre']} sale: ${p['precio']} y se encuentran {p['cantidad']} unidades")
        encontrado = True
        break

if not encontrado:
    print("Producto no disponible")


print("------------------------------------------------")

print("EJERCICIO 6")

with open("productos.txt", "w") as archivo_producto:
    for i in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo_producto.write(linea)

print("Archivo actualizado")
import csv
import os

# === FUNCIONES ===

def menu():
    while True:
        print("\n== MENÚ DE PRODUCTOS ==")
        print("|1| Mostrar todos los productos registrados")
        print("|2| Agregar nuevo producto")
        print("|3| Eliminar un producto existente")
        print("|4| Salir del programa\n")

        opc = input("Elige una opción (1-4): ").strip()

        if not opc:
            print("⚠️  No ingresaste ninguna opción.")
            continue

        if opc not in ("1", "2", "3", "4"):
            print("⚠️  Opción inválida. Debe ser un número del 1 al 4.")
            continue

        match opc:
            case "1":
                opcion_1()
            case "2":
                opcion_2()
            case "3":
                opcion_3()
            case "4":
                print("👋 Saliendo del programa...")
                break


def opcion_1():
    # Mostrar productos
    try:
        if not os.path.exists("productos.csv"):
            print("⚠️  No existe ningún archivo de productos aún.")
            return

        with open("productos.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            filas = list(lector)

            if not filas:
                print("⚠️  No hay productos registrados todavía.")
                return

            print("\n--- LISTA DE PRODUCTOS ---")
            for fila in filas:
                producto = fila.get("producto", "").strip()
                precio = fila.get("precio", "").strip()
                if not producto or not precio:
                    print("❌ Se detectó una fila con datos incompletos, ignorando...")
                    continue
                print(f"{producto.capitalize()} | Precio: ${precio}")

    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")


def opcion_2():
    # Agregar producto
    while True:
        producto = input("Ingrese el nombre del producto nuevo: ").strip().lower()
        if not producto:
            print("⚠️  El nombre del producto no puede estar vacío.")
            continue
        if ";" in producto or "," in producto:
            print("⚠️  No uses caracteres especiales como ',' o ';'.")
            continue
        break

    while True:
        precio = input("Ingrese el precio del producto (solo números): ").strip()
        if not precio:
            print("⚠️  El precio no puede estar vacío.")
            continue
        if not precio.isdigit():
            print("⚠️  El precio debe ser un número entero positivo.")
            continue
        precio = int(precio)
        if precio <= 0:
            print("⚠️  El precio debe ser mayor que cero.")
            continue
        break

    try:
        # Verificar si el archivo ya existe
        archivo_nuevo = not os.path.exists("productos.csv")
        with open("productos.csv", "a", newline="") as archivo:
            campos = ["producto", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            if archivo_nuevo or archivo.tell() == 0:
                escritor.writeheader()
            escritor.writerow({"producto": producto, "precio": precio})
        print(f"✅ Producto '{producto}' agregado correctamente con precio ${precio}.")
    except Exception as e:
        print(f"❌ Error al guardar el producto: {e}")


def opcion_3():
    # Eliminar producto
    if not os.path.exists("productos.csv"):
        print("⚠️  No existe el archivo de productos.")
        return

    producto_eliminado = input("Ingrese el producto a eliminar: ").strip().lower()
    if not producto_eliminado:
        print("⚠️  No ingresaste ningún nombre.")
        return

    productos_actualizados = []
    encontrado = False

    try:
        with open("productos.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                producto = fila.get("producto", "").strip().lower()
                if not producto:
                    print("⚠️  Fila inválida detectada, se omitirá.")
                    continue

                if producto != producto_eliminado:
                    productos_actualizados.append(fila)
                else:
                    encontrado = True

        # Reescribimos el archivo solo si hay cambios
        if encontrado:
            with open("productos.csv", "w", newline="") as archivo:
                campos = ["producto", "precio"]
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(productos_actualizados)
            print(f"✅ Producto '{producto_eliminado}' eliminado correctamente.")
        else:
            print("⚠️  No se encontró el producto a eliminar.")

    except Exception as e:
        print(f"❌ Error al intentar eliminar: {e}")


# === PROGRAMA PRINCIPAL ===

productos_iniciales = [
    {"producto": "galletas", "precio": 1000},
    {"producto": "papa", "precio": 100},
    {"producto": "camote", "precio": 10}
]

# Crear archivo inicial si no existe
if not os.path.exists("productos.csv"):
    try:
        with open("productos.csv", "w", newline="") as archivo:
            campos = ["producto", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos_iniciales)
        print("📁 Archivo 'productos.csv' creado con datos iniciales.")
    except Exception as e:
        print(f"❌ Error al crear el archivo inicial: {e}")

menu()

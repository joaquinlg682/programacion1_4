print("EJERCICIO FOR")


palabras_encriptadas = []

for i in range(5):
    palabra = input(f"Ingresá la palabra {i+1}: ")
    nueva_palabra = ""
    
    for ch in palabra:
        if ch.isalpha():
            ascii_val = ord(ch) + 2
            nueva_letra = chr(ascii_val)
            nueva_palabra += nueva_letra
        else:
            nueva_palabra += ch
    
    palabras_encriptadas.append(nueva_palabra)

print("\nPalabras encriptadas:")
for p in palabras_encriptadas:
    print(p)


print("EJERCICIO WHILE")

import random

jugador=input("elige piedra, papel o tijera: ")

jugador.lower()

opciones=["piedra", "papel", "tijera"]

computadora=random.choice(opciones)
print(f"la computadora eligió: {computadora}")

victoria_jugador=0
victoria_computadora=0

if jugador==computadora:
    print("empate")
elif (jugador=="piedra" and computadora=="tijera") or (jugador=="papel" and computadora=="piedra") or (jugador=="tijera" and computadora=="papel"):
    print("ganaste")
    print(f"jugador:{victoria_jugador+1}")
else:
    print("perdiste")
    print(f"computadora:{victoria_computadora+1}")

print("EJERCICIO FOR")

def cifrado_cesar(palabra,desplazamiento):
    resultado=""
    for char in palabra:
        if char.isaplha():
            base=ord('A') if char.isupper() else ord('a')
            nuevo=(ord(char)-base+desplazamiento)%26+base
            resultado+=chr(nuevo)
        else:
            resultado+=char
    return resultado

palabras_cifradas=[]

print("escribe 5 palabras: ")
for i in range(5):
    palabra = input(f"palabra {i+1}: ")
    cifrada = cifrado_cesar(palabra,2)
    palabras_cifradas.append(cifrada)

print("las palabras cifradas son: ")
for p in palabras_cifradas:
    print(p)        
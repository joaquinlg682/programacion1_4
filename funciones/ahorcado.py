import random

def elegir_palabra():
    
    palabras = ["chori", "morcilla", "asado", "empanada", "locro", "milanesa"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def pedir_letra():
    
    letra = input("Ingresa una letra: ").lower()
    return letra

def jugar():
    
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6
    ganaste = False

    print("Bienvenido al ahorcado")
    print(mostrar_tablero(palabra, letras_adivinadas))

    while intentos > 0 and not ganaste:
        letra = pedir_letra()

        if letra in palabra and letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            print("Adivinaste una letra")
        elif letra in letras_adivinadas:
            print("Ya ingresaste esa letra")
        else:
            intentos -= 1
            print(f"Letra incorrecta, te quedan {intentos} intentos")

        print(mostrar_tablero(palabra, letras_adivinadas))

        if all(l in letras_adivinadas for l in palabra):
            ganaste = True

    if ganaste:
        print(f"Felicidades Adivinaste la palabra: {palabra}, bien hecho campeón")
    else:
        print(f"Perdiste. La palabra era: {palabra}, no pasa nada, algunas veces se gana, otras se pierde")

jugar()

#TP recursividad

print("EJERCICIO 1")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n - 1)
    
num = int(input("ingrese un numero: "))
for i in range(1, num + 1):
    print(f"factorial de {i} = {factorial(i)}")

print("---------------------------------------------------")
print("EJERCICIO 2")
def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
pos = int(input("ingrese a cantidad de terminos: "))
for i in range(pos):
    print(fibonacci(i), end=" ")
    print(" ")


print("---------------------------------------------------")
print("EJERCICIO 3")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
b = int(input("ingrese la base: "))
e = int(input("ingrese el exponente: "))
print(f"{b}**{e} = {potencia(b, e)}")


print("---------------------------------------------------")
print("EJERCICIO 4")

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
numero = int(input("ingrese un numero decimal: "))
binario = decimal_a_binario(numero)
print(f"El numero {numero} en binario es: {binario if binario else '0'}")


print("---------------------------------------------------")
print("EJERCICIO 5")

def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

texto = input("ingrese una palabra: ").lower()
print("es palindromo" if palindromo(texto) else "no es palindromo")


print("---------------------------------------------------")
print("EJERCICIO 6")

def suma_digitos(n):
    if n<10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
num = int(input("ingrese un numero: "))
print(f"la suma de sus digitos es: {suma_digitos(num)}")


print("---------------------------------------------------")
print("EJERCICIO 7")

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
niveles = int(input("Ingrese el numero de bloques en el nivel mas bajo: "))
print(f"total de bloques necesarios: {contar_bloques(niveles)}")


print("---------------------------------------------------")
print("EJERCICIO 8")

def contar_dig(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_dig(numero // 10, digito)

num = int(input("ingrese un numero: "))
dig = int(input("ingrese un digito (del 0 al 9)"))
print(f"el digito {dig} aparece {contar_dig(num, dig)} veces")




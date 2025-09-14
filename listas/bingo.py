import random

numeros=random.sample(range(1,51),25)

filas=5
columnas=5
carton=[]
indice=0
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(numeros[indice])
        indice+=1
    carton.append(fila)

print("carton del bingo: ")
for fila in carton:
    print(fila)

num_aleatorio=random.sample(range(1,51),50)
print("\n Números seleccionados: ",num_aleatorio)

contador=25
for evaluador in num_aleatorio:
    print(f"\n Número seleccionado: {evaluador}")
    for i in range(filas):
        for j in range(columnas):
            if carton[i][j] == evaluador:
                carton[i][j]=0
                contador-=1
                print(" ")
                print("Número marcado")
                for fila in carton:
                    print(fila)
if contador==0:
    print("\n Carton completo")



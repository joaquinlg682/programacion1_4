print("EJERCICIO EN CLASES")

fecha=input("ingrese el dia, fecha y mes en el que se encuentra (formato dia, DD/MM): ")

dia, resto=fecha.split(",")

dd, mm=resto.split("/")

dia=dia.lower()

dias_permitidos=("lunes","martes","miercoles","jueves","viernes")
if dia not in dias_permitidos:
    print("ingrese un dia valido")

mm_permitidos=("01","02","03","04","05","06","07","08","09","10","11","12")
mm31=("01","03","05","07","08","10","12")
mm30=("04","06","09","11")

dd=int(dd)

if mm not in mm_permitidos:
    print("ingrese una fecha permitida")
if mm in mm31 and (dd<1 or dd>31):
    print("este mes tiene como maximo 31 dias")
if mm in mm30 and (dd<1 or dd>30):
    print("este mes tiene como maximo 30 dias")
if mm=="02" and (dd<1 or dd>29):
    print("este mes como maximo tiene 29 dias")

#2da parte

#lunes, martes y miercoles
if dia == "lunes" or dia == "martes" or dia == "miercoles":
    examen=input("¿Hubo examen este dia? (responder si o no): ")
    if examen=="si":
        alumnos_aprobados=int(input("ingrese la cantidad de alumnos aprobados: "))
        alumnos_desaprobados=int(input("ingrese la cantidad de alumnos desaprobados: "))
        alumnos_total=alumnos_desaprobados+alumnos_aprobados
        alumnos_aprobados_porc=(alumnos_aprobados/alumnos_total)*100
        print(f"el porcentaje de alumnos aprobados es de: {alumnos_aprobados_porc}")
    else:
        print("piola :D")

#jueves
if dia=="jueves":
    asistencia=float(input("ingrese el porcentaje de asistencia de la clase: "))
    if asistencia<50:
        print("no asistió la mayoria")
    else:
        print("asistió la mayoria")

#viernes
if dia=="viernes":
    if dd == 1 and mm == "01" or dd ==1 and mm == "01":
        print("Comienzo de nuevo ciclo")

        alumnos=int(input("ingrese la cantidad de alumnos: "))
        aranceles=float(input("ingrese el arancel por alumno: "))

        ingreso_total=alumnos*aranceles

        print(f"el ingreso en total es: {ingreso_total}")
    else:
        print("no es inicio de ciclo")
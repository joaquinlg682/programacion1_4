total_cuenta=float(input("ingrese el monto de la cuenta: "))

porcentaje10=float(total_cuenta*0.10)
total_pagar10=float(porcentaje10+total_cuenta)

print(f"propina surgerida (10%): {porcentaje10}")
print(f"total a pagar (10%): {total_pagar10}")

porcentaje15=float(total_cuenta*0.15)
total_pagar15=float(porcentaje15+total_cuenta)

print(f"propina surgerida (15%): {porcentaje15}")
print(f"total a pagar (15%): {total_pagar15}")
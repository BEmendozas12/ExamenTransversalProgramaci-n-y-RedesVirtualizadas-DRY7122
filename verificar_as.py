# verificar_as.py
numero_as = int(input("Ingrese el número de AS: "))

if (64512 <= numero_as <= 65534) or (4200000000 <= numero_as <= 4294967294):
    print("El número ingresado corresponde a un AS Privado.")
else:
    print("El número ingresado corresponde a un AS Público.")

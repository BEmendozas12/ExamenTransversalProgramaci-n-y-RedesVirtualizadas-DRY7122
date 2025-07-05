# verificar_vlan.py
vlan = int(input("Ingrese número de VLAN: "))

if 1 <= vlan <= 1005:
    print("VLAN del rango NORMAL.")
elif 1006 <= vlan <= 4094:
    print("VLAN del rango EXTENDIDO.")
else:
    print("VLAN inválida. Debe estar entre 1 y 4094.")

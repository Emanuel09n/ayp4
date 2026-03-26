import re

"""match: #buscar al inicio
search: #buscar en cualquier parte
findall: #buscar todas las coincidencias"""

texto= "ac abc abbc abbbc abbbbc"
resultado =re.findall(r"a[bd]{2,3}c", texto)
print(f"abc(cero o mas b): {resultado}")

#como validar si la placa es de un carro 
placa = "HCS 733"
if re.match(r"^[A-Z]{3}\s[0-9]{3}$", placa):
    print("La placa es válida para un carro.")
else:    
    print("La placa no es válida para un carro.")
   
   #como validar si es correo electronico,teniendo las variaciones del nombre de usuario
correo = "usuario@dominio.com"
if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
    print("El correo es válido.")
else:

    print("El correo no es válido.")


#como validar que una fecha este bien
def validar_fecha(fecha):
    correcta=re.search(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", fecha) 
    return bool(correcta)
print(validar_fecha("31/12/2024"))  # True
print(validar_fecha("31/13/2024"))  # False

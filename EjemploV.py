import re


# --------------------------------------------------
# VALIDACIONES CON EXPRESIONES REGULARES
# --------------------------------------------------

def validar_correo(correo):
    """
    Valida correos como:
    juan@gmail.com
    ana_23@outlook.co
    """
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo) is not None


def validar_placa(placa):
    """
    Valida placas como:
    ABC123
    ABC-123
    """
    return re.match(r'^[A-Z]{3}-?\d{3}$', placa) is not None


def validar_telefono(telefono):
    """
    Valida teléfonos como:
    3001234567
    300-123-4567
    """
    return re.match(r'^(\d{10}|\d{3}-\d{3}-\d{4})$', telefono) is not None


def validar_fecha(fecha):
    """
    Valida fechas con formato:
    dd/mm/aaaa

    Ejemplo:
    08/04/2026
    """
    return re.match(r'^\d{2}/\d{2}/\d{4}$', fecha) is not None


def validar_contraseña(password):
    """
    Debe tener:
    - mínimo 8 caracteres
    - al menos una mayúscula
    - al menos un número
    """
    return re.match(r'^(?=.*[A-Z])(?=.*\d).{8,}$', password) is not None


def validar_usuario(usuario):
    """
    Reglas:
    - empieza con letra
    - puede tener letras, números o _
    - entre 5 y 12 caracteres
    """
    return re.match(r'^[A-Za-z][A-Za-z0-9_]{4,11}$', usuario) is not None


def validar_codigo_producto(codigo):
    """
    Formato:
    2 letras mayúsculas - 4 dígitos

    Ejemplo:
    AB-1234
    """
    return re.match(r'^[A-Z]{2}-\d{4}$', codigo) is not None


def validar_documento(documento):
    """
    Valida un número de documento simple:
    solo dígitos, entre 6 y 10 caracteres
    """
    return re.match(r'^\d{6,10}$', documento) is not None


def validar_ip(ip):
    """
    Valida formato simple de IP:
    192.168.0.1

    Ojo: esta validación revisa el formato,
    no que cada número esté entre 0 y 255.
    """
    return re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip) is not None


def validar_hora(hora):
    """
    Valida una hora en formato:
    hh:mm

    Ejemplo:
    14:35
    """
    return re.match(r'^\d{2}:\d{2}$', hora) is not None


def validar_url(url):
    """
    Valida URLs simples como:
    http://google.com
    https://openai.com
    www.google.com
    """
    return re.match(r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$', url) is not None


# --------------------------------------------------
# EXTRACCIÓN CON EXPRESIONES REGULARES
# --------------------------------------------------

def extraer_hashtags(texto):
    """
    Extrae hashtags como:
    #python #100dias
    """
    return re.findall(r'#[A-Za-z0-9_]+', texto)


def extraer_menciones(texto):
    """
    Extrae menciones como:
    @juan @ana23
    """
    return re.findall(r'@[A-Za-z0-9_]+', texto)


def extraer_numeros(texto):
    """
    Extrae números enteros dentro de un texto.
    """
    return re.findall(r'\d+', texto)


def extraer_correos(texto):
    """
    Extrae correos dentro de un texto.
    """
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)


def extraer_mayusculas(texto):
    """
    Extrae palabras completamente en mayúsculas.
    """
    return re.findall(r'\b[A-ZÁÉÍÓÚÑ]+\b', texto)


def extraer_palabras_con_a(texto):
    """
    Extrae palabras que empiecen por a o A.
    """
    return re.findall(r'\b[aA][a-zA-ZÁÉÍÓÚáéíóúñÑ]*\b', texto)


def extraer_codigos(texto):
    """
    Extrae códigos como:
    #1234
    """
    return re.findall(r'#\d{4}\b', texto)


def extraer_años(texto):
    """
    Extrae años de 4 dígitos.
    """
    return re.findall(r'\b\d{4}\b', texto)


# --------------------------------------------------
# PRUEBAS
# --------------------------------------------------

print("----- VALIDACIONES -----")
print("Correo:", validar_correo("juan@gmail.com"))                  # True
print("Placa:", validar_placa("ABC-123"))                          # True
print("Teléfono:", validar_telefono("300-123-4567"))              # True
print("Fecha:", validar_fecha("08/04/2026"))                       # True
print("Contraseña:", validar_contraseña("Hola1234"))               # True
print("Usuario:", validar_usuario("juan_23"))                      # True
print("Código producto:", validar_codigo_producto("AB-1234"))      # True
print("Documento:", validar_documento("1032456789"))               # True
print("IP:", validar_ip("192.168.0.1"))                            # True
print("Hora:", validar_hora("14:35"))                              # True
print("URL:", validar_url("https://google.com"))                   # True

print("\n----- EXTRACCIONES -----")
print("Hashtags:", extraer_hashtags("Hola #python es #genial"))  
# ['#python', '#genial']

print("Menciones:", extraer_menciones("Hola @juan y @ana23"))
# ['@juan', '@ana23']

print("Números:", extraer_numeros("Compré 3 cuadernos y 12 lápices"))
# ['3', '12']

print("Correos:", extraer_correos("Escribe a ana@gmail.com y a juan@correo.co"))
# ['ana@gmail.com', 'juan@correo.co']

print("Mayúsculas:", extraer_mayusculas("Hoy hablé con ANA y LUIS"))
# ['ANA', 'LUIS']

print("Palabras con A:", extraer_palabras_con_a("Ana ama las arepas y Andrés también"))
# ['Ana', 'ama', 'arepas', 'Andrés']

print("Códigos:", extraer_codigos("Tus códigos son #1234 y #5678"))
# ['#1234', '#5678']

print("Años:", extraer_años("Nací en 2004 y mi hermano en 2010"))
# ['2004', '2010']
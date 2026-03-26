import re
import json
import os

ARCHIVO = "usuarios.json"


def cargar_usuarios():
    try:
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    except Exception as e:
        print("Error al cargar usuarios:", e)
        return {}
    finally:
        print("Proceso de carga finalizado.\n")


def guardar_usuarios(usuarios):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        print("Usuarios guardados correctamente.\n")
    except Exception as e:
        print("Error al guardar usuarios:", e)
    finally:
        print("Proceso de guardado finalizado.\n")


def validar_correo(correo):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.search(patron, correo) is not None


def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8:
        errores.append("Debe tener mínimo 8 caracteres.")
    if re.search(r"[A-Z]", contrasena) is None:
        errores.append("Debe tener al menos una letra mayúscula.")
    if re.search(r"[a-z]", contrasena) is None:
        errores.append("Debe tener al menos una letra minúscula.")
    if re.search(r"\d", contrasena) is None:
        errores.append("Debe tener al menos un número.")
    if re.search(r"[@$!%*?&.#_\-+=/]", contrasena) is None:
        errores.append("Debe tener al menos un carácter especial.")

    return errores


def registrar_usuario(usuarios):
    print("\n--- REGISTRO DE USUARIO ---")
    nombre_usuario = input("Ingrese nombre de usuario: ").strip()

    if nombre_usuario in usuarios:
        print("Ese nombre de usuario ya existe.\n")
        return

    correo = input("Ingrese correo electrónico: ").strip()

    if not validar_correo(correo):
        print("Correo inválido. Debe tener un formato correcto, por ejemplo: ejemplo@correo.com\n")
        return

    contrasena = input("Ingrese contraseña: ").strip()
    errores = validar_contrasena(contrasena)

    if errores:
        print("\nContraseña inválida:")
        for error in errores:
            print("-", error)
        print()
        return

    usuarios[nombre_usuario] = {
        "correo": correo,
        "contrasena": contrasena
    }

    guardar_usuarios(usuarios)
    print("Usuario registrado con éxito.\n")


def mostrar_usuarios(usuarios):
    print("\n--- USUARIOS REGISTRADOS ---")
    if not usuarios:
        print("No hay usuarios registrados.\n")
        return

    for nombre, datos in usuarios.items():
        print(f"Usuario: {nombre} | Correo: {datos['correo']}")
    print()


def menu():
    usuarios = cargar_usuarios()

    while True:
        try:
            print("===== MENÚ =====")
            print("1. Registrar usuario")
            print("2. Mostrar usuarios")
            print("3. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                registrar_usuario(usuarios)
            elif opcion == "2":
                mostrar_usuarios(usuarios)
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.\n")

        except Exception as e:
            print("Ocurrió un error:", e)
        finally:
            print("Regresando al menú...\n")


menu()


    
    


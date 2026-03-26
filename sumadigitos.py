def suma_digitos(numero):
    # Caso base
    if numero == 0:
        return 0
    # Caso recursivo
    return (numero % 10) + suma_digitos(numero // 10)


# Programa principal
numero = int(input("Ingrese un número: "))
resultado = suma_digitos(numero)

print("La suma de los dígitos es:", resultado)
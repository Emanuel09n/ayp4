#factorial con memoization,cache factorial
def factorial(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    resultado = n * factorial(n - 1, cache)
    cache[n] = resultado
    return resultado

print(factorial(5)) # 120
print(factorial(6)) # 720, utiliza el resultado de factorial(5)



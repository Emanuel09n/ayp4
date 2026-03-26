#total de monedas con cantidad=30,[1, 5, 10,25]
def cantidad(cantidad, monedas):
    if cantidad == 0:
        return 1
    if cantidad < 0:
        return 0
    total = 0
    for moneda in monedas:
        total += cantidad(cantidad - moneda, monedas)
    return total

print(cantidad(30, [1, 5, 10, 25])) # 18

#clase zapato con caravte2ris

class Zapato:
    def __init__(self, marca, talla, color):
        self.marca = marca
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"Zapato de marca {self.marca}, talla {self.talla}, color {self.color}"  
    
zapato1 = Zapato("Nike", 42, "Negro")
print(zapato1)







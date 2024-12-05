class Padre:
    def __init__(self, velocidad: int, direccion, x, y, pag, u, v, w, h, colkey):
        self.velocidad = velocidad
        self.direccion = direccion
        self.x = x
        self.y = y
        self.pag = pag
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

class Hija(Padre):
    def __init__(self, velocidad: int, direccion, x, y):
        # Solo usamos algunos atributos del padre
        super().__init__(velocidad, direccion, x, y)
        # Puedes agregar atributos específicos de la hija
        self.extra = "Atributo específico de la hija"

# Crear una instancia de la hija
hija = Hija(10, "norte", 5, 5)
print(hija.velocidad)  # 10
print(hija.direccion)  # norte
print(hija.extra)      # Atributo específico de la hija
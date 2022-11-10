class Electrodomestico:
    def __init__(self, codigo, precio, marca, color):
        self.codigo = codigo
        self.precio = precio
        self.marca = marca
        self.color = color
    
    def mostrar(self):
        print(f'''Código del producto: {self.codigo}
Precio: {self.precio}
Marca: {self.marca}
Color: {self.color}
        ''')
    
class Lavadora(Electrodomestico):
    def __init__(self, codigo, precio, marca, color, capacidad):
        super().__init__(codigo, precio, marca, color)
        self.capacidad = capacidad
    
    def mostrar(self):
        print(f'''Código del producto: {self.codigo}
Precio: {self.precio}
Marca: {self.marca}
Color: {self.color}
Capacidad: {self.capacidad}
        ''')

class HornoMicroondas(Electrodomestico):
    def __init__(self, codigo, precio, marca, color, control):
        super().__init__(codigo, precio, marca, color)
        self.control = control
    
    def mostrar(self):
        print(f'''Código del producto: {self.codigo}
Precio: {self.precio}
Marca: {self.marca}
Color: {self.color}
Control: {self.control}
        ''')

class Nevera(Electrodomestico):
    def __init__(self, codigo, precio, marca, color, inc_congelador, compartimientos):
        super().__init__(codigo, precio, marca, color)
        self.inc_congelador = inc_congelador
        self.compartimientos = compartimientos
    
    def mostrar(self):
        print(f'''Código del producto: {self.codigo}
Precio: {self.precio}
Marca: {self.marca}
Color: {self.color}
Incluye Congelador: {self.inc_congelador}
Compartimientos: {self.compartimientos}
        ''')

class Licuadora(Electrodomestico):
    def __init__(self, codigo, precio, marca, color, material_vaso, velocidades):
        super().__init__(codigo, precio, marca, color)
        self.material_vaso = material_vaso
        self.velocidades = velocidades

    def mostrar(self):
        print(f'''Código del producto: {self.codigo}
Precio: {self.precio}
Marca: {self.marca}
Color: {self.color}
Material del Vaso: {self.material_vaso}
Velocidades: {self.velocidades}
        ''')
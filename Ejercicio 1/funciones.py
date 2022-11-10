from articulos import *

def convertir_objetos(edd):
    products = {}
    for key,values in edd.items():
        if key == "washer":
            lavadoras = []
            for product in values:
                codigo = product["cod_p"]
                precio = product["price"]
                marca = product["brand"]
                color = product["color"]
                capacidad = product["capacity"]
                lavadoras.append(Lavadora(codigo, precio, marca, color, capacidad))
            products["lavadoras"] = lavadoras
            continue
        elif key == "microwave":
            microwaves = []
            for product in values:
                codigo = product["cod_p"]
                precio = product["price"]
                marca = product["brand"]
                color = product["color"]
                control = product["digital"]
                microwaves.append(HornoMicroondas(codigo, precio, marca, color, control))
            products["microwaves"] = microwaves
            continue
        elif key == "fridge":
            neveras = []
            for product in values:
                codigo = product["cod_p"]
                precio = product["price"]
                marca = product["brand"]
                color = product["color"]
                inc_congelador = product["cooler"]
                compartimientos = product["comp"]
                neveras.append(Nevera(codigo, precio, marca, color, inc_congelador, compartimientos))
            products["neveras"] = neveras
            continue
        else: 
            licuadoras = []
            for product in values:
                codigo = product["cod_p"]
                precio = product["price"]
                marca = product["brand"]
                color = product["color"]
                material_vaso = product["cup"]
                velocidad = product["speeds"]
                licuadoras.append(Licuadora(codigo, precio, marca, color, material_vaso, velocidad))
            products["licuadoras"] = licuadoras
            continue
    return products

def mostrar_inventario(products):
    for key, value in products.items():
        print(key)
        for product in value:
            product.mostrar()
        print("===================================================")

def encontrar_producto(products):
    code = input("Por favor introduzca el código del producto a eliminar: ")
    for key,value in products.items():
        for product in value:
            if code == product.codigo:
                return product
    else: 
        print("Producto no encontrado")

def borrar_producto(producto, productos):
    for key,value in productos.items():
        if producto in value: 
            value_nuevo = value.remove(producto)
    productos[key] = value_nuevo
    return productos

def ver_neveras(products):
    for key,value in products.items():
        if key == "neveras":
            for product in value:
                if product.inc_congelador == True:
                    product.mostrar()
                    

def ver_defectuosos(productos):
    for product in productos:
        product.mostrar()
        print("===================================================")

def ver_mas_costoso(products):
    all_products = []
    for key,value in products.items():
        for product in value:
            all_products.append(product)
    all_products.sort(key=lambda product: product.precio, reverse=True)
    all_products[0].mostrar()
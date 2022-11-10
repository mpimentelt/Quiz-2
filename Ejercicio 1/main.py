from funciones import *

def main():
    edd = {
    "washer":
    [
        {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
        {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
    ],
    "microwave":
    [
        {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
        {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
    ],
    "fridge":
    [
        {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
        {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
    ],
    "blender":
    [
        {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
        {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
    ]
    }
    products = convertir_objetos(edd)
    productos_borrados = []
    print("********** BIENVENIDO **********")
    while True:
        option = input('''Introduzca una opción válida: 
1. Mostrar el inventario
2. Borrar un producto defectuoso
3. Ver cantidad de neveras y si poseen congelador
4. Ver productos defectuosos
5. Ver producto más costoso
6. Salir
->''')
        if option.isnumeric():
            option = int(option)
            if option == 1:
                mostrar_inventario(products)
            elif option == 2:
                producto_borrar = encontrar_producto(products)
                productos_borrados.append(producto_borrar)
                products = borrar_producto(producto_borrar, products)
            elif option == 3:
                ver_neveras(products)
            elif option == 4:
                ver_defectuosos(productos_borrados)
            elif option == 5:
                ver_mas_costoso(products)
            elif option == 6:
                break
        else: 
            continue
    print("Gracias por su visita. Que tenga un feliz día.")


main()
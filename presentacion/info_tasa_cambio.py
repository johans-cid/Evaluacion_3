from negocio import conversion_moneda

def mostrar_conversor():
    cantidad = float(input("Ingrese la cantidad: "))
    origen = input("Moneda de origen (USD/CLP/EUR/ARS): ").upper()
    destino = input("Moneda de destino (USD/CLP/EUR/ARS): ").upper()

    conversion_moneda(cantidad, origen, destino)
    
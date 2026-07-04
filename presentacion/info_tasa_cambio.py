from negocio import conversion_moneda, num_correcto, texto_correcto
from prettytable import PrettyTable

def mostrar_conversor():
    print()
    cantidad = num_correcto(input("Ingrese una cantidad: $"))
    origen = texto_correcto(input("Moneda de origen (USD/CLP/EUR/ARS): "))
    destino = texto_correcto(input("Moneda de destino (USD/CLP/EUR/ARS): "))

    mostrar = conversion_moneda(cantidad, origen, destino)
    
    tabla_conversor = PrettyTable()
    tabla_conversor.field_names = ["Cantidad", "Moneda Origen","Moneda Destino", "Cantidad Convertida"]
    tabla_conversor.add_row([f"${cantidad}", origen, destino, f"${mostrar:.2f}"])
    print(tabla_conversor)

    
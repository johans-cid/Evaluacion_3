from prettytable import PrettyTable
from negocio import suma_y_promedio
from datos import compras

def mostrar_compras():
    tabla_compra = PrettyTable()
    tabla_compra.field_names = ["Valores de compra"]
    for i in compras:
        tabla_compra.add_row([f"$ {i}"])
    print(tabla_compra)

    tabla_suma_promedio = PrettyTable()
    tabla_suma_promedio.field_names = ["Suma total" , "Promedio"]
    tabla_suma_promedio.add_row(suma_y_promedio())
    print(tabla_suma_promedio)

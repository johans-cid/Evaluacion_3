from negocio import mejor_resultado
from prettytable import PrettyTable
from datos import deportistas

def mostrar_deportistas():
    tabla = PrettyTable()
    tabla.field_names = ["Deportistas", "resultados"]

    for nombre, puntaje in deportistas.items():
        tabla.add_row([nombre, puntaje])

    print(tabla)

    mejor_puntaje_tabla = PrettyTable()
    mejor_puntaje_tabla.field_names = ["Mejor deportista" , "Resultado"]

    mejor_puntaje_tabla.add_row(mejor_resultado())
    print(mejor_puntaje_tabla)

    

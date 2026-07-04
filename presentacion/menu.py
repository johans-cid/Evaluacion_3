from presentacion.info_deportistas import mostrar_deportistas
from presentacion.info_compras import mostrar_compras
from datos import nombre
from presentacion.info_tasa_cambio import mostrar_conversor

def menu_app():
    while True:    
        print()
        print(f"{nombre}")
        print(f'{'=' * len(nombre)}')
        print()
        print("""Opciones: 
              
[1] Ejercicio 1: Resultado de competencias
[2] Ejercicio 2: 
[3] Ejercicio 3:
[4] Salir""")
        
        print()
        opcion = input("Ingrese alguna de las opciones: ")
        
        if opcion == "1":
            print()
            mostrar_deportistas()
        elif opcion == "2":
            print()
            mostrar_compras()
        elif opcion == "3":
            mostrar_conversor()
        elif opcion == "4":
            break
        else:
            print("Opcion invalida, intentelo de nuevo.")
    
from datos import compras

def suma_y_promedio():
    suma = 0
    for i in compras:
        suma = i + suma
    
    promedio = suma / len(compras)
    
    return suma, promedio






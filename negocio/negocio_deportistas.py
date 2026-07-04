from datos import deportistas

def mejor_resultado():
    valor_mayor = 0
    for i in deportistas.values():
        if i > valor_mayor:
            valor_mayor = i 
    
    for clave, valor in deportistas.items():
        if valor == valor_mayor:
            nombre = clave
    
    return nombre, valor_mayor
     
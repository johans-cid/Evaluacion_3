from datos import tasas_cambio

def conversion_moneda(cantidad, moneda_origen, moneda_destino):
    valor_en_usd = cantidad / tasas_cambio[moneda_origen]
    resultado = valor_en_usd * tasas_cambio[moneda_destino]
    return resultado

def num_correcto(a):
    while True:
        
        try:
            cantidad_c = float(a)
            return cantidad_c
            break
        except ValueError:
            print("Error: la cantidad debe ser un número válido.")
            a = input("Ingrese una cantidad: $")

def texto_correcto(a):
    while True:
        try:
            for moneda in tasas_cambio:
                if a.upper() == moneda:
                    return a.upper()
            raise ValueError("Moneda no válida")
        except ValueError:
            print("Error: moneda no válida.")
            a = input("Ingrese la moneda nuevamente (USD/CLP/EUR/ARS): ")
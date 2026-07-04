from datos import tasas_cambio

def conversion_moneda(cantidad, moneda_origen, moneda_destino):
    valor_en_usd = cantidad / tasas_cambio[moneda_origen]
    resultado = valor_en_usd * tasas_cambio[moneda_destino]
    print(resultado)
from te import Te

te_1 = Te.retorna_tiempo_y_recomendacion(1)
te_2 = Te.retorna_precio(300)

tipo_1 = type(te_1) # Obtiene el tipo de te_1, que será <class 'Te'>
tipo_2 = type(te_2) # Obtiene el tipo de te_2, que será <class 'str'>

print(tipo_1) # Imprime <class 'Te'>
print(tipo_2) # Imprime <class 'str'>

if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")

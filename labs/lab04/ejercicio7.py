def calcula_calificacion(puntos):
    if puntos >= 0.9 and puntos <= 1.0: 
        print('Sobresaliente')
    elif puntos >= 0.8 and puntos < 0.9:
        print('Notable')
    elif puntos >= 0.7 and puntos < 0.8:
        print('Bien')
    elif puntos >= 0.6 and puntos < 0.7:
        print('Suficiente')
    elif puntos >0 and puntos <0.6:
        print('Insuficiente')
    else:
        puntos = "Error, calificación no válida " 
    return puntos

score = float(input("Ingrese calificación (0.01-1.00): "))
puntos = calcula_calificacion(score)
print("Su calificación es:", puntos)

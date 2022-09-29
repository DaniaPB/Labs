def calcularpago(horas, tarifa):
    MAX_HORAS_SEMANALES = 40 
    horas_extras = 0 
    if((horas) > MAX_HORAS_SEMANALES):
        horas_extras = horas - MAX_HORAS_SEMANALES
        horas = MAX_HORAS_SEMANALES
    calculo = (horas) * (tarifa) + (horas_extras * (tarifa * 1.5))
    return calculo 
horas = int(input("ingrese número de horas: "))
tarifa = int(input("ingrese tarifa"))
pago = calcularpago(horas, tarifa)

print(pago)

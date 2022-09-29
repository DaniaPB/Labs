contador = 0
suma = 0
while True: 
    try:
        numero = input("ingrese número: ")
        if numero == "fin":
            break
        else:
            contador = contador + 1 
            suma = suma + int (numero)
            promedio = suma / contador 
    except:
        print("Valor no es válido")
        continue 
print("Contador", suma)
print("Suma", contador)
print("promedio ", promedio)

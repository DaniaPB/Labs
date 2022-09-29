maximo = 0 
minimo = 0
primer_numero = True
while True: 
    try:
        lista = input("Ingrese los dígitos: ")
        if (lista == 'final'):
            break
        else:
            if (primer_numero):
                maximo = int(lista)
                minimo = int(lista)
                primer_numero = False 
            else:
                if (int(lista) > maximo): maximo = int(lista)
                if (int(lista) <minimo): minimo = int(lista)
    except: 
        print("Valor inválido")
        continue
print("Máximo", maximo)
print("Mínimo", minimo)

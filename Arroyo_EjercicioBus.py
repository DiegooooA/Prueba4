asientos = {1,2,3,4,5,6,7,8,9,10}
pasajeros = []
while True:
    print("Bienvenidos")
    print("1. Ver asientos disponibles")
    print("2. Comprar asientos")
    print("3. Ver pasajeros registrados")
    print("4. Salir")
    op=int(input("ingrese una opcion valida: "))
    if op==1:
        print(f"asientos disponibles: {asientos}")
    elif op==2:
        try:
            rut =int(input("ingresa tu rut para comprar: "))
            compra = int(input("ingresa el asiento que desea comprar: "))
            if compra in asientos:
                asientos.remove(compra)
                pasajeros.append({"rut: ",rut,"asiento:",compra}) 
                print("¿Como desea pagar ? ")
                print("1. Efectivo")
                print("2. Tarjeta")
                rep=(int(input("Ingrese una opcion: ")))
                print("la compra a sido realizada con exito")
            else:
                break
        except ValueError:
            print("ingrese datos validos")
    elif op==3:
         print("pasajeros registrados")
         print(pasajeros)
    elif op==4:
         print("adios")
         break
    else:
         print("ingrese una opcion valida")

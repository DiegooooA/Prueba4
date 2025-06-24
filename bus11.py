asientos = {1,2,3,4,5,6,7,8,9,10}
pasajeros = []
while True:
    print("bienvenidos")
    print("1. ver asientos disponibles")
    print("2. comprar asientos")
    print("3. ver ver pasajeros registrados")
    print("4. salir")
    op=int(input("ingrese una opcion valida: "))
    if op==1:
        print(f"asientos disponibles: {asientos}")
    elif op==2:
        rut =int(input("ingresa tu rut para comprar: "))
        compra = int(input("ingresa el asiento que desea comprar: "))
        if compra in asientos:
                asientos.remove(compra)
                pasajeros.append("rut: ",rut,"asiento:",compra) 
                print(f"la compra a sido realizada con exito")
        else:
             break
    elif op==3:
         print("pasajeros registrados")
         print(pasajeros)
    elif op==4:
         print("adios")
         break
    else:
         print("ingrese una opcion valida")
        
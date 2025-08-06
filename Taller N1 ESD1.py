x = False
    #creamos un inventario base
inventario = [[1,"tomate",3,400], [2, "aguacate",1,5000]]
while (True):
    ingreso_total = 0
    x = False
    #Le pedimos al usiario elegir el menu
    opcion = int(input("¿A qué menú deseas acceder?\n" \
    "-1 Crean nueva venta\n" \
    "-2 Listar ventas\n" \
    "-3 Buscar por ID\n" \
    "-4 Modificar\n" \
    "-5 Eliminar\n" \
    "-6 Calcular totales (ingreso total)\n" \
    "-7 Salir\n" \
    ": "
          ))
    if (opcion == 1):
        venta= (input("Digite el ID, Nombre, cantidad y valor unitaro del producto en orden y por espacios: ")).split()
        venta_real = [0,0,0,0]
        for i, e in enumerate(venta):
            if ( i == 1):
                venta_real[i] = e
            else:
                venta_real[i] = int(e)
        inventario.append(venta_real)
    elif (opcion == 2):
        print()
        print("---------VENTAS---------")
        for i in inventario:
            print(i)
    elif (opcion == 3):
        id = int(input("Digite el id de la compra que quiere mostrar: "))
        print("")
        for i in range(len(inventario)):
            if (inventario[i][0] == id):
                print(f"Nombre del producto: {inventario[i][1]}")
                print(f"Cantidad del producto: {inventario[i][2]}")
                print(f"Precio_unitario del producto: {inventario[i][3]}")
                x = True
        if (x == False):
            print("El ID del producto no se encuentra en las ventas registradas")
    
    elif (opcion == 4):
        while  (True):
            id = int(input("Digite la venta que desea modificar por medio del ID: "))
            print("")
            for i in range(len(inventario)):
                if (inventario[i][0] == id):
                    producto = input("Digite el nuevo nombre del producto: ")
                    inventario[i][1] = producto
                    producto = int(input("Digite la nueva cantidad del producto: "))
                    inventario[i][2] = producto
                    producto = int(input("Digite el nuevo precio unitario del producto: "))
                    inventario[i][3] = producto
                    print("Productos Modificados correctamente")
                    print(inventario[i])
                    x = True
            if (x):
                break
            else:
                 print("El ID del producto no se encuentra en las ventas registradas, intente nuevamente") 
                 print()  
    elif (opcion == 5):
        while (True):
            id = int(input("Digite la venta que desea eliminar por medio del ID: "))
            for i in range(len(inventario)):
                if (inventario[i][0] == id):
                    del inventario[i]
                    x = True
            if (x):
                break
            else:
                print("El ID del producto no se encuentra en las ventas registradas, intente nuevamente") 
                print()  
    elif (opcion == 6):
        for i in range(len(inventario)):
            total_venta = inventario[i][2] * inventario[i][3]
            ingreso_total = ingreso_total + total_venta
        print("")
        print(f"EL total vendido hoy fue de: {ingreso_total}")
        
    elif (opcion == 7):
        break 
    print()
    print()


       
    
from operator import itemgetter
# Clase para manejo de archivos
class clas_files:
    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f:
                print(linea.strip())

    def write(self, filename, contenido):
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(contenido)


# Variables para la parte de clientes
archivo = "clientes.txt"
files = clas_files()

# Inventario base (menú anterior)
inventario = [[1, "tomate", 3, 400], [2, "aguacate", 1, 5000]]

while (True):
    ingreso_total = 0
    x = False
    # Menú combinado
    opcion = int(input("¿A qué menú deseas acceder?\n" \
    "-1 Crear nueva venta\n" \
    "-2 Listar ventas\n" \
    "-3 Buscar por ID\n" \
    "-4 Modificar\n" \
    "-5 Eliminar\n" \
    "-6 Calcular totales (ingreso total)\n" \
    "-7 Salir (ventas)\n" \
    "-8 Crear archivo con clientes\n" \
    "-9 Consultar saldo por nombre\n" \
    "-10 Contar clientes con saldo > 50\n" \
    "-11 Listar clientes ordenados por saldo\n" \
    "-12 Salir del programa\n" \
    ": "
          ))

    # ---- Opciones del menú original ----
    if (opcion == 1):
        venta = (input("Digite el ID, Nombre, cantidad y valor unitario del producto en orden y por espacios: ")).split()
        venta_real = [0, 0, 0, 0]
        for i, e in enumerate(venta):
            if (i == 1):
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
        while (True):
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
        print("Saliendo del menú de ventas...")
        continue

    elif (opcion == 8):
        clientes = ["Cedula,Nombre,Saldo\n","12345,Jose,50.43\n","54321,Dario,43.12\n","12121,Carlos,32.2\n",
        "32143,Gustavo,12.23\n","14235,Diego,41.34\n","11112,Juan,42.31\n"]
        files.write(archivo, clientes)
        print("El archivo de clientes ha sido creado con datos iniciales.")

    elif (opcion == 9):
        nombre = input("Ingrese el nombre del cliente: ")
        encontrado = False
        with open(archivo, "r", encoding="utf-8") as file:
            next(file)
            for i in file: 
                partes = i.strip().split(",")
                cedula= partes[0]
                nom = partes[1]
                saldo = partes[2]
                if nom.lower() == nombre.lower():
                    print(f"El saldo de {nom} es: {saldo}")
                    encontrado = True
        if not encontrado:
            print("Cliente no encontrado.")

    elif (opcion == 10):
        contador = 0
        with open(archivo, "r", encoding="utf-8") as file:
            next(file)
            for linea in file:
                partes = linea.strip().split(",")
                saldo = partes[-1]
                if float(saldo) > 50:
                    contador += 1
        print(f"Cantidad de clientes con saldo mayor a 50: {contador}")

    elif (opcion == 11):
        clientes = []
        with open(archivo, "r", encoding="utf-8") as file:
            next(file)
            for i in file:
                partes = i.strip().split(",")
                cedula= partes[0]
                nom = partes[1]
                saldo = partes[2]
                clientes.append((nom, float(saldo)))
        clientes = sorted(clientes, key=itemgetter(1))
        print("Clientes ordenados por saldo:")
        for nom, saldo in clientes:
            print(f"{nom} - {saldo}")

    elif (opcion == 12):
        print("El programa ha sido cerrado")
        break

    else:
        print("Opcion no valida, intente de nuevo.")

    print()
    print()

from clasegestor import GestorVenta

if __name__== '__main__':
    def menu():
        print("1. Ingresar venta")
        print("2. Total de facturación de una sucursal")
        print("3. Sucursal que más facturó en un día")
        print("4. Sucursal con menos facturación en la semana")
        print("5. Total facturado por todas las sucursales en la semana")
        print("6. Salir")
        return int(input("Seleccione una opción: "))

    gestor = GestorVenta()

    while True:
        opcion = menu()
        if opcion == 1:
            num_dia = int(input("Ingrese el día de la semana (1-7): "))
            num_suc = int(input("Ingrese el número de sucursal (1-5): "))
            importe = float(input("Ingrese el importe de la factura: "))
            gestor.acumular((num_suc-1),(num_dia-1))

        elif opcion == 2:
            num_suc = int(input("Ingrese el número de sucursal (1-5): "))
            total = gestor.total_fact_suc(num_suc-1)
            print(f"Total facturado por la sucursal {num_suc+1}: {total}") #LA "f" PERMITE PONER LLAVES Y CONCATENAR CADENAS

        elif opcion == 3:
            dia = int(input("Ingrese el día de la semana (1-7): "))
            num_suc = gestor.mayor_fact(num_dia-1)
            print(f"La sucursal que más facturó el día {num_dia} fue: {num_suc+1}")

        elif opcion == 4:
            num_suc = gestor.menor_fact()
            print(f"La sucursal con menos facturación en la semana fue: {num_suc+1}")

        elif opcion == 5:
            total = gestor.total_fact()
            print(f"Total facturado por todas las sucursales en la semana: {total}")

        elif opcion == 6:
            break


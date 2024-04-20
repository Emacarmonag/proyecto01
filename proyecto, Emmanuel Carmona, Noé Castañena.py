class Gasolinera:
    def _init_(self):
        self.inventario = {"Regular": 80.0, "Super": 80.0, "Diesel": 80.0}
        self.trabajadores = {"Diurna": 1, "Vespertina": 1, "Nocturna": 1}
        self.costos_almacenamiento = {"Regular": 7.0, "Super": 8.0, "Diesel": 6.0}
        self.precios_venta = {"Regular": 29.0, "Super": 30.0, "Diesel": 26.5}
        self.salarios = {"Diurna": 14.0, "Vespertina": 14.5, "Nocturna": 15.5}

    def gestionar_inventario(self):
        print("Nivel de inventario:")
        for tipo_combustible, nivel in self.inventario.items():
            print(f"{tipo_combustible}: {nivel} galones")
        agregar = input("¿Desea agregar combustible? (si/no): ")
        if agregar.lower() == "si":
            for tipo_combustible in self.inventario:
                cantidad = float(input(f"Ingrese la cantidad de {tipo_combustible}: "))
        if cantidad > 0:
 if self.inventario[tipo_combustible] + cantidad <= 80:
                        self.inventario[tipo_combustible] += cantidad
                        print(f"Se agregaron {cantidad} galones de {tipo_combustible} al inventario.")
        else:
                        print(f"No es posible agregar {cantidad} galones de {tipo_combustible}, excede la capacidad.")
        else:
                    print("La cantidad ingresada es inválida.")
        else:
            print("Operación finalizada.")

    def venta_combustible(self):
        print("Inventario actual y precios:")
        for tipo_combustible, nivel in self.inventario.items():
            print(f"{tipo_combustible}: {nivel} galones - Q{self.precios_venta[tipo_combustible]} por galón")
        tipo_combustible = input("Seleccione el tipo de combustible: ")
        if self.inventario[tipo_combustible] <= 5:
            print("No hay suficiente inventario.")
            return
        cantidad = float(input(f"Ingrese la cantidad de {tipo_combustible} a vender: "))
        if cantidad > self.inventario[tipo_combustible]:
            print("No es posible realizar la venta, cantidad solicitada excede el inventario.")
            return
        modo_venta = input("Seleccione el modo de venta (galones/dinero): ")
        if modo_venta.lower() == "dinero":
            cantidad = float(input("Ingrese el monto en quetzales: ")) / self.precios_venta[tipo_combustible]
        nombre = input("Ingrese su nombre completo: ")
        nit = input("Ingrese su NIT: ")
        num_bomba = int(input("Ingrese el número de bomba (1-4): "))
        total_venta = cantidad * self.precios_venta[tipo_combustible]
        print(f"Resumen de la compra:\nNombre: {nombre}\nNIT: {nit}\nNúmero de bomba: {num_bomba}\nTotal: Q{total_venta}")
        self.inventario[tipo_combustible] -= cantidad
        print("Venta realizada con éxito.")

    def gestionar_turnos(self):
        print("Trabajadores por jornada:")
        for jornada, cantidad in self.trabajadores.items():
            print(f"{jornada}: {cantidad}")
        agregar = int(input("¿Cuántos trabajadores desea agregar en total?: "))
        for _ in range(agregar):
            jornada = input("Ingrese la jornada del nuevo trabajador (Diurna/Vespertina/Nocturna): ")
            self.trabajadores[jornada] += 1
        retirar = int(input("¿Cuántos trabajadores desea retirar en total?: "))
        for _ in range(retirar):
            jornada = input("Ingrese la jornada del trabajador a retirar (Diurna/Vespertina/Nocturna): ")
        if self.trabajadores[jornada] > 0:
                self.trabajadores[jornada] -= 1
            else:
                print("No hay trabajadores disponibles para retirar en esa jornada.")

    def reporte_rentabilidad(self):
        ingresos_venta = sum(self.inventario[tipo_combustible] * self.precios_venta[tipo_combustible] for tipo_combustible in self.inventario)
        materia_prima = sum(self.inventario[tipo_combustible] * self.costos_almacenamiento[tipo_combustible] for tipo_combustible in self.inventario)
        costo_mano_obra = sum(self.trabajadores[jornada] * self.salarios[jornada] for jornada in self.trabajadores)
        costos_fijos = 10
        utilidad_bruta = ingresos_venta - materia_prima - costo_mano_obra - costos_fijos
        print("Reporte de Rentabilidad:")
        print(f"Ingresos totales: Q{ingresos_venta:.2f}")
        print("Materia Prima:")
        for tipo_combustible in self.inventario:
            print(f"\tCosto combustible {tipo_combustible}: Q{self.inventario[tipo_combustible] * self.costos_almacenamiento[tipo_combustible]:.2f}")
        print(f"Mano de obra: Q{costo_mano_obra:.2f}")
        print(f"Costos Fijos: Q{costos_fijos:.2f}")
        print(f"Utilidad Bruta: Q{utilidad_bruta:.2f}")

    def ejecutar(self):
        while True:
            print("\n  Menú Principal ")
            print("1. Gestionar inventario")
            print("2. Venta de combustible")
            print("3. Gestión de turnos")
            print("4. Reporte de rentabilidad")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

     if opcion == "1":
                self.gestionar_inventario()
            elif opcion == "2":
                self.venta_combustible()
            elif opcion == "3":
                self.gestionar_turnos()
            elif opcion == "4":
                self.reporte_rentabilidad()
            elif opcion == "5":
                print("¡Adiós, si no es inge no vuelva!")
                break
            else:
                print("Esta opcion no se puede")


gasolinera = Gasolinera()
gasolinera.ejecutar()

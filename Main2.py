from Clases import *

ListaAutos = []
ListaMecanicos = []
ListaReparaciones = []

def insertarDatosTesting():
    A = Auto('GHFG23','GTSFDRSF343434','ROJO', 'KIA','RIO 5', 2013)
    A2 = Auto('WESD17','HSTDGDRSF34332','BLANCO', 'NISSAN','TERRANO', 2010)
    A3 = Auto('HTDG22','IKYUHHFTDG2323','GRIS', 'MAZDA','CX 5', 2020)
    ListaAutos.append(A)
    ListaAutos.append(A2)
    ListaAutos.append(A3)

    M = Mecanico('1.123.123-1','ALEXIS', 'SANCHEZ', 35, 'CURICO')
    M2 = Mecanico('2.123.123-1','ARTURO', 'VIDAL', 30, 'MOLINA')
    M3 = Mecanico('3.123.123-1','GARY', 'MEDEL', 40, 'TENO')
    ListaMecanicos.append(M)
    ListaMecanicos.append(M2)
    ListaMecanicos.append(M3)
insertarDatosTesting()

while True:

    Menu.LimpiarConsola()
    Menu.MostrarMenu()

    OpcionSeleccionada = input(" : ")

    if OpcionSeleccionada == "8":
        #Eliminar Auto
        Menu.LimpiarConsola()
        i = 1
        for A in ListaAutos:
            print(f"{i}, - {A.GetInfo()}")
            i += 1
        opcion = int(input("Seleccione Auto a Eliminar: "))

        ListaAutos.remove(ListaAutos[opcion - 1])
        
        input("Auto Eliminado Correctamente! Presione Enter para Continuar...")


    if OpcionSeleccionada == "7":
        #Editar un Auto
        Menu.LimpiarConsola()
        i = 1
        for A in ListaAutos:
            print(f"{i}, - {A.GetInfo()}")
            i += 1
        opcion = int(input("Seleccione Auto a Modificar: "))

        ListaAutos[opcion - 1].setPatente(input("Ingrese Patente: "))
        ListaAutos[opcion - 1].setNChasis(input("Ingrese Numero Chasis: "))
        ListaAutos[opcion - 1].setColor(input("Ingrese Color: "))
        ListaAutos[opcion - 1].setMarca(input("Ingrese Marca: "))
        ListaAutos[opcion - 1].setModelo(input("Ingrese Modelo: "))
        ListaAutos[opcion - 1].setYear(input("Ingrese Año: "))

        input("Auto Modificado Correctamente! Presione Enter para Continuar...")

    if OpcionSeleccionada == "1":

        Menu.LimpiarConsola()

        #Logica para Agregar Auto
        print("-----------Opcion Seleccionada 1: Ingresando Auto----------------")
        print("-----------------------------------------------------------------")
        pat = input("Ingrese Patente: ")
        nchas = input("Ingrese Numero Chasis: ")
        col = input("Ingrese Color: ")
        marca = input("Ingrese Marca: ")
        modelo = input("Ingrese Modelo: ")
        year = pat = input("Ingrese Año: ")

        A = Auto(pat,nchas,col,marca,modelo,year)

        #Insertarlo en la Base de Datos
        ListaAutos.append(A)

        input("Auto Ingresado Correctamente! Presione Enter para Continuar...")

    if OpcionSeleccionada == "2":
        Menu.LimpiarConsola()

        #Logica para Agregar Mecanico
        print("-----------Opcion Seleccionada 2: Ingresando Mecanicos ----------------")
        print("-----------------------------------------------------------------")

        nom = input("Ingrese Nombres: ")
        ape = input("Ingrese Apellidos: ")
        edad = int(input("Ingrese Edad: "))

        M = Mecanico(nom, ape, edad)

        ListaMecanicos.append(M)

        input("Mecanico Ingresado Correctamente! Presione Enter para Continuar...")



    if OpcionSeleccionada == "3":
        Menu.LimpiarConsola()

        #Logica para Agregar Mecanico
        print("-----------Opcion Seleccionada 3: Ingresando Reparacion ----------------")
        print("-----------------------------------------------------------------")

        #print(ListaMecanicos.count())
        if (len(ListaMecanicos) > 0) & (len(ListaAutos) > 0): #Y OR NOT
            #OK: Puedo agregar una Raparacion
            i = 1
            for M in ListaMecanicos:
                print(f"{i}, - {M.GetInfo()}")
                i += 1

            opcion = int(input("Seleccione Mecanico: "))
            mec = ListaMecanicos[opcion-1]
            i = 1
            for A in ListaAutos:
                print(f"{i}, - {A.GetInfo()}")
                i += 1
            opcion = int(input("Seleccione Auto: "))
            auto = ListaAutos[opcion-1]
            costo = input("Ingrese Valor de la Reparacion: ")
            repuesto = input("Ingrese Repuesto Utilizado: ")
            R = Reparacion(mec, auto, costo, repuesto)
            ListaReparaciones.append(R)
            input("Reparacion Ingresada Correctamente! Presione Enter para Continuar...")
            #print(mec.GetInfo())
        else:
            print("Para Agregar una Reparacion debe tener al menos ingresado Un(1) Auto y Un(1)Mecanico!")
            input("Presione Enter para Continuar...")

    if OpcionSeleccionada == "4":
        Menu.LimpiarConsola()
        print("-----------Opcion Seleccionada 4: Viendo Autos----------------")
        print("-----------------------------------------------------------------")
        for A in ListaAutos:
            print(A.GetInfo())
        input("Presione una Tecla para Continuar...")

    if OpcionSeleccionada == "5":
        Menu.LimpiarConsola()
        print("-----------Opcion Seleccionada 5: Viendo Mecanicos----------------")
        print("-----------------------------------------------------------------")
        for M in ListaMecanicos:
            print(M.GetInfo())
        input("Presione una Tecla para Continuar...")

    if OpcionSeleccionada == "6":
        Menu.LimpiarConsola()
        print("-----------Opcion Seleccionada 5: Viendo Reparaciones----------------")
        print("-----------------------------------------------------------------")
        for R in ListaReparaciones:
            print(R.GetInfo())
        input("Presione una Tecla para Continuar...")
    
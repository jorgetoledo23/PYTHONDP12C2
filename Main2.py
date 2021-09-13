from Clases import *

ListaAutos = []
ListaMecanicos = []
ListaReparaciones = []

while True:

    Menu.LimpiarConsola()
    Menu.MostrarMenu()

    OpcionSeleccionada = input(" : ")

    if OpcionSeleccionada == "1":
        #Logica para Agregar Auto
        print("Opcion Seleccionada 1: Ingresando Auto")
        pat = input("Ingrese Patente: ")
        nchas = input("Ingrese Numero Chasis: ")
        col = input("Ingrese Color: ")
        marca = input("Ingrese Marca: ")
        modelo = input("Ingrese Modelo: ")
        year = pat = input("Ingrese Año: ")
        tipoMotor = input("Ingrese Tipo Motor: ")
        cil = input("Ingrese Cilindrada: ")
        tipoAuto = input("Ingrese Tipo Auto: ")
        tipoComb = input("Ingrese Tipo Combustible: ")

        A = Auto(pat,nchas,col,marca,cil,tipoComb,tipoMotor,tipoAuto,modelo,year)

        #Insertarlo en la Base de Datos
        ListaAutos.append(A)

    if OpcionSeleccionada == "4":
        for A in ListaAutos:
            print(A.GetInfo())
        input("Presione una Tecla para Continuar : ")

    
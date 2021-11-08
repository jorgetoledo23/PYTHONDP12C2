from Model.Clases import *
from ConexionMySql import DAO

dao = DAO()
mP = MenuPrincipal()

while True:
    mP.LimpiarConsola()
    mP.MostrarMenu()

    oP = str(input(" : "))

    #Gestion de Clientes
    if oP == "1":
        mP.LimpiarConsola()
        mP.MenuSecundario("Cliente")
        oP = str(input(" : "))

        if oP == "1":
            #Agregar Cliente a la base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Cliente =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            C = Cliente(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarCliente(C)

            mP.ConfirmacionIngreso("Cliente")

        if oP == "2":
            #Leer Todos los Clientes almacenados en mi BD
            mP.LimpiarConsola()
            print("======= Listando Clientes =======")
            print("=================================")
            print("")    

            for C in dao.ListarClientes():
                print(C.getInfo())

            print("")
            input("Presione Enter para Continuar...")

        if oP == "5":
            pass

    #Gestion de Mecanicos
    if oP == "2":
        mP.LimpiarConsola()
        mP.MenuSecundario('Mecanico')
        oP = str(input(" : "))

        if oP == "1":
            #Agregar Mecanico a la base de Datos
            mP.LimpiarConsola()
            print("======= Agregando Mecanico =======")
            print("Complete la Informacion Solicitada:")
            print("")

            Rut = str(input("Rut: "))
            Nombres = str(input("Nombres: "))
            Apellidos = str(input("Apellidos: "))
            Telefono = str(input("Telefono: "))
            Correo = str(input("Correo: "))
            Direccion = str(input("Direccion: "))
            Comuna = str(input("Comuna: "))

            M = Mecanico(Rut,Nombres,Apellidos,Correo,Telefono,Direccion,Comuna)

            dao.InsertarMecanico(M)

            mP.ConfirmacionIngreso("Mecanico")

        if oP == "2":
            #Leer Todos los Clientes almacenados en mi BD
            mP.LimpiarConsola()
            print("======= Listando Mecanicos =======")
            print("=================================")
            print("")    

            for M in dao.ListarMecanicos():
                print(M.getInfo())

            print("")
            input("Presione Enter para Continuar...")

        if oP == "5":
            pass




import mysql.connector
from mysql.connector import errorcode
from Model.Clases import *

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='',
                host='127.0.0.1',
                database='d_n2_p12_c2')
            #
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


    def InsertarCliente(self, C):
        add_cliente = ("insert into tbl_clientes"
                        "(rut, nombres, apellidos, direccion, correo, telefono, comuna)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_cliente = (C.getRut(), C.getNombres(), C.getApellidos(), C.getDireccion(), C.getCorreo(), C.getTelefono(), C.getComuna())

        cursor = self.cnx.cursor()
        cursor.execute(add_cliente, data_cliente)
        self.cnx.commit()

    def ActualizarCliente(self, C, Rut):
        add_cliente = ("UPDATE tbl_clientes SET rut = %s, nombres = %s, apellidos = %s, correo = %s, telefono = %s, "
                    " direccion = %s, comuna = %s"
                    " WHERE rut = %s")

        data_cliente = (C.getRut(), C.getNombres(), C.getApellidos(), C.getCorreo(), C.getTelefono(), C.getDireccion(), C.getComuna(), Rut)

        cursor = self.cnx.cursor()
        cursor.execute(add_cliente, data_cliente)
        self.cnx.commit()

    def EliminarCliente(self, Rut):
        eliminar_cliente = ("DELETE FROM tbl_clientes WHERE rut = %s")

        data_cliente = (Rut,)

        cursor = self.cnx.cursor()
        cursor.execute(eliminar_cliente, data_cliente)
        self.cnx.commit()


    def InsertarMecanico(self, M):
        add_mecanico = ("insert into tbl_mecanicos"
                        "(rut, nombres, apellidos, direccion, correo, telefono, comuna)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_mecanico = (M.getRut(), M.getNombres(), M.getApellidos(), M.getDireccion(), M.getCorreo(), M.getTelefono(), M.getComuna())

        cursor = self.cnx.cursor()
        cursor.execute(add_mecanico, data_mecanico)
        self.cnx.commit()

    def ActualizarMecanico(self, M, Rut):
        add_mecanico = ("UPDATE tbl_mecanicos SET rut = %s, nombres = %s, apellidos = %s, correo = %s, telefono = %s, "
                    " direccion = %s, comuna = %s"
                    " WHERE rut = %s")

        data_mecanico = (M.getRut(), M.getNombres(), M.getApellidos(), M.getCorreo(), M.getTelefono(), M.getDireccion(), M.getComuna(), Rut)

        cursor = self.cnx.cursor()
        cursor.execute(add_mecanico, data_mecanico)
        self.cnx.commit()

    def EliminarMecanico(self, Rut):
        eliminar_mecanico = ("DELETE FROM tbl_mecanicos WHERE rut = %s")

        data_mecanico = (Rut,)

        cursor = self.cnx.cursor()
        cursor.execute(eliminar_mecanico, data_mecanico)
        self.cnx.commit()


    def InsertarVehiculo(self, V):
        add_vehiculo = ("insert into tbl_autos"
                        "(patente, marca, modelo, year, color, numero_chasis, rut_cliente)"
                        "values"
                        "(%s,%s,%s,%s,%s,%s,%s)")

        data_vehiculo = (V.getPatente(), V.getMarca(), V.getModelo(), V.getYear(), V.getColor(), V.getChasis(), V.getCliente())

        cursor = self.cnx.cursor()
        cursor.execute(add_vehiculo, data_vehiculo)
        self.cnx.commit()


    def EliminarVehiculo(self, Patente):
        eliminar_Vehiculo = ("DELETE FROM tbl_Autos WHERE Patente = %s")

        data_Vehiculo = (Patente,)

        cursor = self.cnx.cursor()
        cursor.execute(eliminar_Vehiculo, data_Vehiculo)
        self.cnx.commit()


    def ListarClientes(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM tbl_clientes")
        listaClientes = []

        for (rut, nombres, apellidos, telefono, correo, direccion, comuna) in cursor:
            C = Cliente(rut, nombres, apellidos, correo, telefono, direccion, comuna)
            listaClientes.append(C)

        return listaClientes

    def ListarMecanicos(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM tbl_mecanicos")
        listaMecanicos = []

        for (rut, nombres, apellidos, telefono, correo, direccion, comuna) in cursor:
            M = Mecanico(rut, nombres, apellidos, correo, telefono, direccion, comuna)
            listaMecanicos.append(M)

        return listaMecanicos

    def ListarVehiculos(self):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * FROM tbl_autos")
        lista = []
        for(patente, marca, modelo, year, color, numero_chasis, rut_cliente) in cursor:
            A = Auto(patente, numero_chasis,color, marca, year, modelo, rut_cliente)
            lista.append(A)
        return lista


#CRUD 

#C => Create => Insertar => INSERT INTO tbl_x VALUES etc etc.

#R => Read => Leer => SELECT * FROM tbl_x

#U => Update => Actualizar

#D => Delete => Eliminar


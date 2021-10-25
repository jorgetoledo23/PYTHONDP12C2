import os

class Auto:
    #Atributos de Clase
    cantidadRuedas = 4

    #Constructor
    def __init__(self, pat, nchasis, color, marca, model, year):
        #Encapsulacion
        self.__Patente = str(pat).upper()
        self.__NumeroChasis = nchasis
        self.__Color = color
        self.__Marca = marca
        self.__Modelo = model
        self.__Year = year

    def getPatente(self):
        return self.__Patente

    def getColor(self):
        return self.__Color
    
    def setColor(self, color):
        self.__Color = color

    def setNChasis(self, nchas):
        self.__NumeroChasis = nchas

    def setMarca(self, marca):
        self.__Marca = marca

    def setModelo(self, modelo):
        self.__Modelo = modelo

    def setPatente(self, pat):
        self.__Patente = pat

    def setYear(self, year):
        self.__Year = year

    def GetInfo(self):
        return f"Instancia: {self} ,Auto Patente: {self.__Patente}, Numero Chasis: {self.__NumeroChasis}, Marca: {self.__Marca},  Modelo: {self.__Modelo}, Color: {self.__Color}, Año: {self.__Year}"

    def EncenderLuces():
        pass

    def getCantidadRuedas():
        return Auto.cantidadRuedas


class Mecanico:
    #Constructor
    def __init__(self, rut, nomb, ape, edad, dir):
        self.__Rut = rut
        self.__Nombres = nomb
        self.__Apellidos = ape
        self.__Edad = edad
        self.__Direccion = dir

        if self.__Edad >= 18:
            self.__MayorEdad = True
        else:
            self.__MayorEdad = False

    def GetInfo(self):
        return f"Mecanico RUT: {self.__Rut} Nombre: {self.__Nombres}, Apellidos: {self.__Apellidos}, Edad: {self.__Edad}, Direccion: {self.__Direccion}"


class Reparacion:

    def __init__(self, mecanico, auto, costo, repuestos):
        self.__Mecanico = mecanico
        self.__Auto = auto
        self.__Costo = costo
        self.__Repuesto = repuestos

    def GetInfo(self):
        #return "Auto Reparado: " + self.__Auto.getPatente() + " Color: " + self.autoAsignado.getColor() + " Mecanico Asignado: " + self.mecanicoAsignado.nombres + " Costo Total: $" + str(self.costo)
        return f"Info Reparacion: Auto Instancia: {self.__Auto} ,Auto: {self.__Auto.GetInfo()}, Mecanico: {self.__Mecanico.GetInfo()}"

    def setNewColor(self, color):
        self.autoAsignado.setColor(color)
    

class Menu:

    def MostrarMenu():
        print("---------------------------SISTEMA DE REPARACIONES---------------------------------------")
        print(" ")
        print("Presione 1 para Agregar Automoviles: ")
        print("Presione 2 para Agregar Mecanicos: ")
        print("Presione 3 para Agregar Reparaciones: ")

        print("Presione 4 para Ver Automoviles: ")
        print("Presione 5 para Ver Mecanicos: ")
        print("Presione 6 para Ver Reparaciones: ")

        print("Presione 7 para Modificar un Automovil: ")
        print("Presione 8 para Eliminar un Automovil: ")
        

    def LimpiarConsola():
        os.system("cls" if os.name=="nt" else "clear" )
import os

class Auto:
    #Atributos de Clase
    cantidadRuedas = 4

    #Constructor
    def __init__(self, pat, nchasis, color, marca, cilin, comb, tmotor, tauto, model, year):
        #Encapsulacion
        self.__patente = str(pat).upper()
        self.numeroChasis = nchasis
        self.__color = color
        self.marca = marca
        self.cilindrada = cilin
        self.tipoCombustible = comb
        self.tipoMotor = tmotor
        self.tipoAuto = tauto
        self.modelo = model
        self.year = year

    def getPatente(self):
        return self.__patente

    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color

    def GetInfo(self):
        return f"Auto Marca: {self.marca}, Patente: {self.__patente}, Modelo: {self.modelo}, Color: {self.__color}, Año: {self.year}"

    def EncenderLuces():
        pass

    def getCantidadRuedas():
        return Auto.cantidadRuedas


class Mecanico:
    #Constructor
    def __init__(self, nomb, ape, edad):
        self.nombres = nomb
        self.apellidos = ape,
        self.edad = edad

        if self.edad >= 18:
            self.mayorEdad = True
        else:
            self.mayorEdad = False

    def GetInfo(self):
        return f"Mecanico Nombre: {self.nombres}, Apellidos: {self.apellidos}, Edad: {self.edad}"


class Reparacion:

    def __init__(self, mecanico, auto, costo, repuestos):
        self.mecanicoAsignado = mecanico
        self.autoAsignado = auto
        self.costo = costo
        self.repuestos = repuestos

    def GetInfo(self):
        return "Auto Reparado: " + self.autoAsignado.getPatente() + " Color: " + self.autoAsignado.getColor() + " Mecanico Asignado: " + self.mecanicoAsignado.nombres + " Costo Total: $" + str(self.costo)

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
        

    def LimpiarConsola():
        os.system("cls" if os.name=="nt" else "clear" )
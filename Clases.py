class Auto:
    #Atributos de Clase

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

    def GetInformacion(self):
        return "Auto Marca: ", self.marca, " Año: ", self.year, " Modelo: ", self.modelo, " Patente N: ", self.patente

    def EncenderLuces():
        pass


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


class Reparacion:

    def __init__(self, mecanico, auto, costo, repuestos):
        self.mecanicoAsignado = mecanico
        self.autoAsignado = auto
        self.costo = costo
        self.repuestos = repuestos

    def getInfoReparacion(self):
        return "Auto Reparado: " + self.autoAsignado.getPatente() + " Color: " + self.autoAsignado.getColor() + " Mecanico Asignado: " + self.mecanicoAsignado.nombres + " Costo Total: $" + str(self.costo)

    def setNewColor(self, color):
        self.autoAsignado.setColor(color)
    


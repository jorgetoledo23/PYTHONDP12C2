class Auto:
    #patente = None
    __patente = ""
    numeroChasis = ""
    color = ""
    marca = ""
    year = 0
    cilindrada = 0
    tipoCombustible = ""
    tipoMotor = ""
    tipoAuto = ""
    modelo = ""

    def __init__(self, pat, nchasis):
        self.__patente = pat
        self.numeroChasis = nchasis

    def getPatente(self):
        return self.__patente


    def GetInformacion(self):
        return "Auto Marca: ", self.marca, " Año: ", self.year, " Modelo: ", self.modelo, " Patente N: ", self.__patente

    def EncenderLuces():
        pass



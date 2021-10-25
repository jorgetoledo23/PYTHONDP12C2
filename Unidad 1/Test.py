from Clases import Auto

#Instanciar un Objeto
miAuto = Auto("FSKR34", "JKASJKDJKJJAJ23423")
miAuto.cilindrada = 2000
miAuto.color = "Blanco"
miAuto.marca = "KIA"
miAuto.modelo = "Rio 5"
miAuto.tipoAuto = "HashBack"
miAuto.year = 2010

print(miAuto.getPatente())



print(miAuto.GetInformacion())

otroAuto = Auto("DDGT54", "JASDASDWASD23423")
otroAuto.cilindrada = 1600
otroAuto.color = "Rojo"
otroAuto.marca = "AUDI"
otroAuto.modelo = "A7"
otroAuto.tipoAuto = "HashBack"
otroAuto.year = 2014  

print(otroAuto.GetInformacion())


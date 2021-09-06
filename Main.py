from Clases import Auto, Mecanico, Reparacion

autoDos = Auto(
    pat="fsHR54",
    nchasis="HGGHDGHASD45",
    color="Rojo",
    marca="KIA",
    cilin=2000,
    comb="Bencina",
    tmotor="V12 Cilindros",
    tauto="Sedan",
    model="Cerato",
    year=2018)

autoUno = Auto(
    pat="jhGF16",
    nchasis="KJGHDFSASD23",
    color="Azul",
    marca="NISSAN",
    cilin=1600,
    comb="Bencina",
    tmotor="4 Cilindros en Linea",
    tauto="Sedan",
    model="XD",
    year=2013)


mecanicoJuan = Mecanico(nomb="Juan", ape="Valdes Gonzalez", edad=25)
mecanicoPedro = Mecanico(nomb="Pedro", ape="Roman Ramirez", edad=40)

listaRepuestos1 = ["Empaquetadura de Culata","Pegamento Firme","Sellante"]

reparacion1 = Reparacion(mecanico=mecanicoPedro, auto=autoDos, costo=170800, repuestos=listaRepuestos1)
reparacion1.setNewColor("Azul")

print(reparacion1.getInfoReparacion())







#print(autoDos.patente) #FSHR54
#
#print(mecanicoJuan.mayorEdad)



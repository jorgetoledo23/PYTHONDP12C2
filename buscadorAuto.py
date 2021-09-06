from Clases import Auto, Mecanico

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

listadoAutos = []
listadoAutos.append(autoUno)
listadoAutos.append(autoDos)

patenteBuscada = str(input("Ingresa la Patente del Auto que estas buscando: "))
encontrado = False

for auto in listadoAutos:
    if (auto.patente == patenteBuscada):
        encontrado = auto
        break

if encontrado:
    print("Auto Encontrado!!")
    print(encontrado.GetInformacion())
else:
    print("Auto NO ENCONTRADO! Lo siento!")
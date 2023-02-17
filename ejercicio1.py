""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control: """

def crear_grupo(nombre):
    if seleccion==1:
        global grupoArtemis
        grupoArtemis=[]
        print("Se creo el grupo de ", nombre)
        return grupoArtemis
    elif seleccion ==2:
        global grupoSputnik
        grupoSputnik=[]
        print("Se creo el grupo de ", nombre)
        return grupoSputnik

def listarCampers():
    if seleccion==1.1:
        print("Lista de campers, Grupo Artemis")
        j=0
        while j < len(grupoArtemis):
            print(grupoArtemis[j])
            j+=1
    else:
        print("Lista de campers, Grupo Sputnik")
        j=0
        while j < len(grupoSputnik):
            print(grupoSputnik[j])
            j+=1

def agregarCampers():
    n=input("Ingrese el nombre del Camper: ")
    if seleccion==1.2:
        grupoArtemis.append(n)
        print("Se agrego nuevo camper")
    else:
        grupoSputnik.append(n)
        print("se agrego nuevo camper")

def eliminarCamper():
    n=input("Ingrese nombre de camper a Eliminar: ")
    if seleccion==1.3:
        grupoArtemis.remove(n)
        print(f'Se elimino correctamente el camper {n}')
    else:
        grupoSputnik.remove(n)
        print(f'Se elimino correctamente el camper {n}')

def ordenarCampers():
    print("Lista de campers alfabeticamente")
    if seleccion==1.4:
        grupoArtemis.sort()
        print(f'{grupoArtemis}')
    else:
        grupoSputnik.sort()
        print(f'{grupoSputnik}')

def buscarCamper():
    n=input("Ingresa el nombre del camper a Buscar: ")
    nB=(n in grupoArtemis)
    if nB:
        print("El camper fue Encontrado")
    else:
        print("Nombre no registrado")

global grupoArtemis
global grupoSputnik
i=0
contGS=0
contGA=0
while i==0:
    print("------MENU PRINCIPAL-------")
    print("1. CREAR GRUPO DE ARTEMIS")
    print("1.1. LISTAR CAMPERS DE ARTEMIS")
    print("1.2. AGREGAR CAMPERS A ARTEMIS")
    print("1.3. ELIMINAR CAMPERS DE ARTEMIS")
    print("1.4. ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
    print("1.5. BUSCAR CAMPERS EN LISTA DE ARTEMIS")
    print("2. CREAR GRUPO DE SPUTNIK")
    print("2.1. LISTAR CAMPERS DE SPUTNIK")
    print("2.2. AGREGAR CAMPERS A SPUTNIK")
    print("2.3. ELIMINAR CAMPERS DE SPUTNIK")
    print("2.4. ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
    print("2.5. BUSCAR CAMPERS EN LISTA DE SPUTNIK")
    seleccion = float(input("Selecciona una opcción: "))

    if seleccion == 1 and contGA == 0:
        contGA=1
        nombreGrupoArtemis="Artemis"
        crear_grupo(nombreGrupoArtemis)
    elif seleccion == 1.1 and contGA==1:
        listarCampers()
    elif seleccion == 1.2 and contGA==1:
        agregarCampers()
    elif seleccion == 1.3 and contGA==1:
        eliminarCamper()
    elif seleccion == 1.4 and contGA==1:
        ordenarCampers()
    elif seleccion == 1.5 and contGA==1:
        buscarCamper()
    elif seleccion == 2 and contGS==0:
        contGS=1
        nombreGrupoSputnik="Sputnik"
        crear_grupo(nombreGrupoSputnik)
    elif seleccion == 2.1 and contGS==1:
        listarCampers()
    elif seleccion == 2.2 and contGS==1:
        agregarCampers()
    elif seleccion == 2.3 and contGS==1:
        eliminarCamper()
    elif seleccion == 2.4 and contGS==1:
        ordenarCampers()
    elif seleccion == 2.5 and contGS==1:
        buscarCamper()
    else:
        if seleccion == 1:
            print("Grupo de Artemis ya se creo")
        elif seleccion == 2:
            print("Grupo de Sputnik ya se creo")
        elif seleccion == 1.2 or seleccion==1.1:
            print("Se debe crear primero el Grupo de Artemis")
        else:
            print("Opccion Errada")
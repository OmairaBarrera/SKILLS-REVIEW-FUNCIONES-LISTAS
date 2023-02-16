""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control: """

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

seleccion = int(input("Selecciona una opcción: "))
contGS=0
contGA=0

if seleccion == 1 and contGA == 0:
    print("seleccionaste 1")
    contGA=1
elif seleccion == 1.1:
    print("seleccionaste 1.1")
elif seleccion == 1.2:
    print("seleccionaste 1.1")
elif seleccion == 1.3:
    print("seleccionaste 1.1")
elif seleccion == 1.4:
    print("seleccionaste 1.1")
elif seleccion == 1.5:
    print("seleccionaste 1.1")
elif seleccion == 2:
    print("seleccionaste 1.1")
elif seleccion == 2.1:
    print("seleccionaste 1.1")
elif seleccion == 2.2:
    print("seleccionaste 1.1")
elif seleccion == 2.3:
    print("seleccionaste 1.1")
elif seleccion == 2.4:
    print("seleccionaste 1.1")
elif seleccion == 2.5:
    print("seleccionaste 1.1")
else:
    if seleccion == 1:
        print("Grupo de Artemis ya se creo")
    elif seleccion == 2:
        print("Grupo de Sputnik ya se creo")
    else:
        print("Opccion Errada")
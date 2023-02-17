""" 2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """

def atletaGanador():
    pos=max(finalistasMarca)
    valor=finalistasMarca.index(pos)
    print(f'El ganador de la medalla de oro es: {finalistasNombre[valor]} con {finalistasMarca[valor]} metros')
    if pos > 15.50:
        print(f'Rompio el record muldial, recibe 500 millones')

def ingresarAtleta(atletas):
    j=0
    while j != atletas:
        nombre=input("Ingrese el nombre del atleta: ")
        marca=float(input("Ingrese marca de salo en metros: "))
        finalistasNombre.append(nombre)
        finalistasMarca.append(marca)
        j+=1

def mostrarAtletas():
    print("Atletas Finalistas")
    j=0
    while j < len(finalistasMarca):
        print(f'{finalistasNombre[j]} = {finalistasMarca[j]}')
        j+=1

#menu
i=0
cont=0
finalistasNombre=[]
finalistasMarca=[]
while i==0:
    print(f'----------MENU-----------')
    print(f'1. INGRESAR CANTIDAD DE ATLETAS')
    print(f'2. AGREGAR ATLETAS')
    print(f'3. MOSTRAR ATLETAS')
    print(f'4. INDICAR CAMPEON')
    print(f'5. salir')

    opcion=int(input('Selecciona un opcion: '))

    if opcion==1:
        atletas=int(input('Ingrese la cantidad de atletas: '))
        cont=1
    elif opcion ==2 and cont==1:
        ingresarAtleta(atletas)
    elif opcion==3 and cont==1:
        mostrarAtletas()
    elif opcion==4 and cont==1:
        atletaGanador()
    elif opcion==5:
        exit()
    else:
        if opcion==1 or opcion==2 or opcion==3:
            print(f'INGRESAR PRIMERO CANTIDAD DE ATLETAS')
        else:
            print(f'OPCIÓN ERRADA')

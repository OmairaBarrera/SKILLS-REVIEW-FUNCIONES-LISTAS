""" 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """

#menu
i=0
cont=0
finalistasNombre=[]
finalistasMarca=[]
while i==0:
    print(f'----------MENU-----------')
    print(f'1. INGRESAR CANTIDAD DE CICLISTAS')
    print(f'2. AGREGAR DATOS CICLISTAS')
    print(f'3. MOSTRAR DATOS CICLISTAS')
    print(f'4. INDICAR CAMPEON DE LA VUELTA')
    print(f'5. SALIR')

    opcion=int(input('Selecciona un opcion: '))

    if opcion==1:
        ciclistas=int(input('Ingrese la cantidad de ciclistas: '))
        cont=1
    elif opcion ==2 and cont==1:
        ingresarCiclista(ciclistas)
    elif opcion==3 and cont==1:
        mostrarCiclistas()
    elif opcion==4 and cont==1:
        ciclistaGanador()
    elif opcion==5:
        exit()
    else:
        if opcion==1 or opcion==2 or opcion==3:
            print(f'INGRESAR PRIMERO CANTIDAD DE CICLISTAS')
        else:
            print(f'OPCIÓN ERRADA')
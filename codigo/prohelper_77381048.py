# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:56:42 2021

@author: lucia
"""
import matplotlib.pyplot as plt


def pedirEntero(mensaje, unidades, minimo = 0, maximo = 100000):
    """
    Pide las medidas de las diferentes zonas del cuerpo
    
    Argumentos: 
        mensaje -- indica que tenemos que introducir
        unidades -- indica en qué unidades tienen que estar las medidas introducidas
        minimo -- el valor minimo que tiene que tener esta medida
        máximo -- el valor máximo que tiene que tener esta medida
    
    Valor de retorno: 
        Devuelve el valor de la medida
    """
    
    while True: #se ha creado un bucle para que nos pregunte de nuevo por los datos si estos son inválidos
        try:
            dato = int(input(mensaje + " (entre " + str(minimo) + " y " + str(maximo) + unidades + ".): "))
            if dato < minimo or dato > maximo:
                print("Error. El dato debe estar entre", minimo, " y ", maximo)
            else:
                break
        except ValueError:#si el valor no es numérico vuelve a pedirnos el valor 
            print("Error. El dato debe ser un valor numerico")
    return dato

def pedirOpcion(mensaje, opciones):
    """Pide la región del cuerpo de la que se va a realizar la prótesis
    
    Argumentos: 
        mensaje -- indica que tenemos que introducir
        opciones -- indica las diferentes partes que podemos introducir
    
    Valor de retorno: 
        Devuelve la región del cuerpo de la que se va a realizar la prótesis 
    """ #la región estará almacenada en la variable opción
    
    while True:
        opcion = input(mensaje + "(" + ", ".join(opciones) + "): ") #almacena la zona del cuerpo de la que se va a realizar la protesis 
        if opcion not in opciones:
            print("Error debe ser una de las opciones listadas.") #volvería a entrar en el bucle
        else:
            break
    return opcion



def nuevaProtesis(protesis, nextId):
    """
    Selecciona qué parámetros son los necesarios y pide sus medidas 
    
    Argumentos: 
        protesis -- contiene la parte, la subparte y las medidas de los parámetros específicos
        nextId -- cuantifica el número de prótesis 
        
    Valor de retorno: 
        Devuelve el identificador 
    """
    
    print("ALTA PROTESIS".center(50, "*"))
    parte = pedirOpcion("Introduce donde ", ["Cabeza", "Parte superior", "Tren inferior"])
    if parte == "Cabeza":
        subparte = pedirOpcion("Introduce unidad", ["Nasal", "Auricular"])#nos pide con la función pedirOpcion la subparte
        if subparte == "Nasal":#se exigirán las medidas de los siguientes parámetros específicos
            ojos = pedirEntero("Distancia entre los ojos", "mm", 23, 28) #se introducen los valores de las medidas usando la funcion pedirEntero y se almacenan en esas variables 
            longitud = pedirEntero("Longitud", "mm", 42, 60)
            anchura = pedirEntero("Anchura", "mm", 25, 38)
            profundidad = pedirEntero("Profundidad", "mm",2,6)
            protesis[nextId] = [(parte, subparte), ojos, longitud, anchura, profundidad] #se crea una lista con toda la información de la prótesis
        else: #como solo hay dos subpartes para cada parte, si no es nasal tendrá que se por obligación auricular (por lo que he usado un else)
            anchuraPomulos = pedirEntero("Anchura entre pomulos", "mm", 127, 152)
            anchuraOrificios = pedirEntero("Anchura entre orificios", "mm", 137, 157)
            longitudOreja = pedirEntero("Longitud de la oreja", "mm", 55, 65)
            anchuraOreja = pedirEntero("Anchura de la oreja", "mm", 30, 45)
            protesis[nextId] = [(parte, subparte), anchuraPomulos, anchuraOrificios, longitudOreja, anchuraOreja]
            
    elif parte == "Parte superior":#Se usan los condicionales y las funciones del mismo modo que anteriormente para obtener las medidas de los parámetros específicos de cada parte y subparte
        subparte = pedirOpcion("Intoduce unidad", ["Brazo", "Codos"])
        if subparte == "Brazo":
            longitudBrazo = pedirEntero("Longitud del brazo", "cm", 75, 95)
            longitudAntebrazo = pedirEntero("Longitud del antebrazo", "cm", 15, 25)
            diametroArriba = pedirEntero("Diametro parte de arriba", "cm", 18, 45)
            diametroAbajo = pedirEntero("Diametro parte de abajo", "cm", 12, 22)
            protesis[nextId] = [(parte, subparte), longitudBrazo, longitudAntebrazo, diametroArriba, diametroAbajo]
        else:
            longitudCubito = pedirEntero("Logitud del cubito", "cm", 22, 33)
            longitudRadio = pedirEntero("Longitud del radio", "cm", 20, 30)
            diametroCubito = pedirEntero("Diametro del cubito", "cm", 1, 3)
            diametroRadio = pedirEntero("Diametro del radio", "cm",  1, 3)
            protesis[nextId] = [(parte, subparte), longitudCubito, longitudRadio, diametroCubito, diametroRadio]
    else:
        subparte = pedirOpcion("Introduce unidad", ["Cesta pelvica", "Pierna"])
        if subparte == "Cesta pelvica":
            cadera = pedirEntero("Cadera", "cm", 78, 120)
            cintura = pedirEntero("Cintura", "cm", 58, 90)
            longitud = pedirEntero("Longitud (desde cintura a cadera)", "cm", 32, 40)
            protesis[nextId] = [(parte, subparte), cadera, cintura, longitud]
        else:
            longitudPierna = pedirEntero("Longitud de la pierna", "cm", 75, 100)
            longitudCaderaRodilla = pedirEntero("Longitud desde la cadera a la rodilla", "cm", 0, 50)
            diametroSuperior = pedirEntero("Diametro parte superior", "cm", 35, 65)
            diametroInferior = pedirEntero("Diametro parte abajo", "cm", 22, 30)
            protesis[nextId] = [(parte,  subparte), longitudPierna, longitudCaderaRodilla, diametroSuperior,diametroInferior]
    
    nextId = nextId + 1 # incrementamos la variable para que vaya cuantificando el número de prótesis que debemos fabricar
    return nextId
    
def menu():
    while True:
        """Muestra todas las funciones principales del programa y almacena cuál se quiere ejecutar
       
        Valor de retorno: 
            número asociado a la función que se quiere realizar
        """ 
        
        try: 
            print("menu".center(50, "*"))
            print("1. Introducir protesis")
            print("2. Listar protesis")
            print("3. Inventario")
            print("4. Porcentajes")
            print("5. Salir", end = "")
            opcion = int(input("Introduce opcion: ")) #se almacena el número asociado a la función que se quiere ejecutar
            return opcion
        except ValueError:
            print("La opcion debe ser un valor numerico")

def listarProtesis(protesis, dicTextos):
    """
    Crea una lista con todas las prótesis con sus partes, subpartes, los parámetros necesarios para fabricarlos y los valores con las medidas de estos
    
    Argumentos: 
        protesis-- contiene la parte, la subparte y las medidas de los parámetros específicos
        dicTextos-- diccionario que contiene las partes y subpartes con sus correspondientes parámetros especificos
    """
    print("LISTADO DE PROTESIS".center(50, "-"))
    for p in protesis: #entramos en la lista protesis
        parte, subparte = protesis[p][0] #se accede al elemento 0 de la lista protesis y se guarda en esta variable
        print(("ID:" +  str(p)).center(40, "-"))
        print(parte, "-", subparte)
        resto = protesis[p][1:] #se accede a todos los elementos a partir del primero y se almacenan en esta variable
        for i in range(len(resto)): #i irá tomando los valores de la longitud del resto 
            print(dicTextos[(parte, subparte)][i], resto[i]) #va al dicTextos e imprime los elementos en posición i y los elementos con posición i del resto 

def inventario(protesis, mostrar = True):
    """
    Crea un inventario cuantificando el número de prótesis que tenemos que realizar y de qué tipo son 
    
    Argumentos: 
        protesis -- contiene la parte, la suparte y las medidas de los parámetros específicos
        mostrar -- 
    Valor de retorno: 
        Devuelve el diccionario donde está la parte, la subparte y el número de prótesis
    """
    
    if mostrar:
        print("INVENTARIO DE PROTESIS".center(50, "-"))
    inventario = {} # la clave del inventario es el tipo de prótesis y el valor cuántas hay y de qué tipo
    for c in protesis:
        clave = (protesis[c][0]) 
        if clave in inventario: 
            inventario[clave] = inventario[clave] + 1 #al valor que tenemos se le sumará 1
        else:
            inventario[clave] = 1 #si no, el valor seguirá siendo 1 
    if mostrar:
        if len(inventario) == 0:
            print("No existen protesis dadas de alta.")
        else:
            print("{0:30} {1:20} {2:8}".format("PARTE", "SUBPARTE", "CUANTAS"))
            for c in inventario:
                print("{0:<30} {1:20} {2:8d}".format(c[0], c[1], inventario[c]))#se accede al diccionario y se imprimen la parte, subparte y tamaño del inventario 
    return inventario


def porcentajes(protesis):
    """ 
    Muestra los porcentajes y un diagrama de sectores de la información del inventario 
    
    Argumentos: 
        protesis -- Indica la parte, la subparte, las medidas de los parámetros específicos 
    """ 
    
    inv = inventario(protesis, False)
    labels = []
    valores = []
    # pasamos el diccionario a listas
    for c in inv:
        labels.append(c[0] + "-" + c[1]) #se añade a la lista la parte y la subparte 
        valores.append(inv[c]) #se añade a la lista el tamaño del inventario (que es el número de prótesis)
    plt.title("Porcentajes de protesis")
    plt.pie(valores, labels = labels, autopct = "%0.1f %%", shadow = True)
    plt.show()

def leer(nextId):
    """
    Permite leer el fichero
   
    Argumentos: 
        NextId -- Cuantifica el número de prótesis
        
    Valor de retorno: 
        Devuelve el diccionario con 
    """
    protesis = {}
    fich = open("protesis.txt", "r")
    for linea in fich:
        trozos = linea.rstrip().split(",") #se eliminan espacios en blanco y se convierte a lista los elementos separados por , 
        protesis[nextId] = [(trozos[0],trozos[1])]
        for t in trozos[2:]:
            protesis[nextId].append(t)
        nextId = nextId + 1
    return protesis


def guardar(protesis):
    """ 
    Almacena los datos de las prótesis en el fichero 
    
    Argumentos: 
        protesis -- Indica la parte, la subparte y las medidas de los parámetros específicos
    """
    
    fich = open("protesis.txt", "w")
    for p in protesis:
        parte, subparte = protesis[p][0]
        fich.write(parte + "," + subparte) #se escribe las partes y subpartes en el fichero
        medidas = protesis[p][2:]
        for m in medidas:
            fich.write(","+ str(m)) #se escriben las medidas en el fichero
        fich.write("\n")
    fich.close()
    
    
def programa():
    """" Hace que se ejecute el programa entero integrando todas las funciones """
    protesis = {}
    nextId = 1 # identificador de la protesis, se asignan comenzando desde 1.
    dicTextos = {("Cabeza", "Nasal"):("Distancia ojos: ", "Longitud: ", "Anchura: ", "Profundidad: "),
                 ("Cabeza", "Auricular"): ("Anchura pomulos: ", "Anchura cabeza: ", "Longitud oreja: ", "Anchura oreja: "),
                 ("Parte superior", "Brazo"): ("Longitud entero: ", "Longitud antebrazo: ", "Diametro arriba: ", "Diametro abajo:"),    
                ("Parte superior", "Codos"): ("Long. cubito: ", "Long. radio: ", "Diametro cubito: ", "Diametro radio: "),
                ("Tren inferior", "Cesta pelvica"): ("Cadera: ", "Cintura: ", "Longitud: "),
                ("Tren inferior", "Pierna"): ("Longitud pierna: ", "Longitud cadera rodilla: ", "Diametro parte superior: ", "Diametro partea abajo: ")}
    protesis = leer(nextId)
    nextId = len(protesis) + 1
    while True:
        opcion = menu()
        if opcion == 1:
            nextId = nuevaProtesis(protesis, nextId)
        elif opcion == 2:
            listarProtesis(protesis, dicTextos)
        elif opcion == 3:
            inventario(protesis)
        elif opcion == 4:
            porcentajes(protesis)
        elif opcion == 5:
            print("Adios...")
            print("Guardando datos...")
            guardar(protesis)
            break
        else:
            print("Error. Opcion incorrecta")
    
    
programa()
    
    
    
    
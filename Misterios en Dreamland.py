import random

class ObjetoKirby:
    def __init__(self, nombre, accion, lugar):
        self.nombre = nombre
        self.accion = accion
        self.lugar = lugar
        self.limiteDeSoluciones = 2
        self.resuelto = False

casos_resueltos = 0
casos_disponibles = 5
historia_mostrada = False
# Lista de nombres de objetos de Kirby
nombres_objetos = ["Kirby Rojo", "Kirby Azul", "Kirby Amarillo", "Kirby Morado", "Kirby Rosa"]
acciones_posibles = ["se ha dormido", "ha roto el espejo de los laberintos", "se ha comodido un Waddle Dee", "ha usado la espada sagrada", "ha tirado el pastel universal"]
lugares_posibles = ["en la Mansion Luz de luna", "en la Montaña mostaza", "en la Ruta arcoiris", "en el Mar de Olivo", "en la Gruta del repollo"]

acciones = ["se ha dormido", "ha roto el espejo de los laberintos", "se ha comodido un Waddle Dee", "ha usado la espada sagrada", "ha tirado el pastel universal"]
ubicaciones = ["en la Mansion Luz de luna", "en la Montaña mostaza", "en la Ruta arcoiris", "en el Mar de Olivo", "en la Gruta del repollo"]


# Crear instancias de objetos de Kirby con acciones y lugares aleatorios
objetos_kirby = []
for nombre_objeto in nombres_objetos:
    accion_aleatoria, lugar_aleatorio = random.sample(acciones_posibles, 1), random.sample(lugares_posibles, 1)
    objeto = ObjetoKirby(nombre_objeto, accion_aleatoria[0], lugar_aleatorio[0])
    objetos_kirby.append(objeto)
    # Eliminar las acciones y lugares usados para evitar repeticiones
    acciones_posibles.remove(accion_aleatoria[0])
    lugares_posibles.remove(lugar_aleatorio[0])


#Funcion para mostrar la historia del juego
def mostrar_historia():
    global historia_mostrada
    
    if(historia_mostrada==False):
        print("En Dreamland, el Rey Dedede se encontraba desconcertado por una serie de incidentes misteriosos que habían estado ocurriendo en su reino. Valiosos tesoros y objetos habían desaparecido sin dejar rastro, y el Rey Dedede estaba decidido a descubrir quiénes eran los culpables detrás de estos misteriosos robos.")
        print("")
        print("Sin embargo, había un problema: había cinco Kirbies, cada uno de un color diferente (Rojo, Azul, Amarillo, Morado y Rosa), y el Rey Dedede no sabía quién había hecho qué ni dónde. Todos los Kirbies se veían inocentes a simple vista, y el Rey Dedede necesitaba ayuda para resolver el enigma.")
        print("")
        print("El Rey Dedede, decidido a descubrir la verdad, convocó a su leal asistente, Escargot, para que lo ayudara en la investigación. Juntos, idearon un plan para interrogar a cada uno de los Kirbies y descubrir qué habían estado haciendo y dónde habían estado en el momento de los robos.")
        print("")
        print("Los cinco Kirbies fueron interrogados uno por uno. Cada uno tenía una historia diferente sobre su paradero y actividades en el momento de los robos. Kirby Rojo decía estar en la Montaña mostaza, Kirby Azul afirmaba haber estado en el Mar de Olivo, Kirby Amarillo mencionaba estar en la Ruta arcoiris, Kirby Morado decía haber estado en la Gruta del repollo, y Kirby Rosa aseguraba estar en la Mansion Luz de luna.")
        print("")
        print("El Rey Dedede y Escargot, armados con estas declaraciones, comenzaron a investigar los lugares en busca de pistas y pruebas que confirmaran o refutaran las afirmaciones de los Kirbies. Pero la tarea no sería fácil, ya que los Kirbies eran conocidos por su habilidad para moverse rápidamente y desaparecer en un abrir y cerrar de ojos.")
        print("")
        print("Ayuda al Rey Dedede y a Escargot a descubrir la verdad detrás de los robos y a determinar qué Kirbies hicieron qué y dónde en Dreamland. La justicia en el reino depende de tu habilidad para resolver el misterio y exponer a los verdaderos culpables.")
        print("")
        print("Ingresa una tecla para continuar...")
        print("")
        input()
        print("")
        print("")
        print("")
        print("")
        print("")
        historia_mostrada = True
# Función para buscar un objeto de Kirby por su nombre
def buscar_objeto_por_nombre(nombre_objeto, lista_objetos):
    for objeto in lista_objetos:
        if objeto.nombre == nombre_objeto:
            return objeto
    return None


#Función para buscar un kirby de una lista de kirbies:
def buscar_kirby(lista_objetos):    
    while True:
        print("Ingresa el número de un kirby sospechoso: (1,2,3,4,5)")
        print("Ingresa una de las siguientes ubicaciones: ")
        print("<<1>>", "Kirby Rojo")
        print("<<2>>", "Kirby Azul")
        print("<<3>>", "Kirby Amarillo")
        print("<<4>>", "Kirby Morado")
        print("<<5>>", "Kirby Rosa")
        numeroKirby = int(input()) 
        if numeroKirby < 0 or numeroKirby > 5:
            print("Ingresa un número correcto")

        elif(lista_objetos[numeroKirby- 1].limiteDeSoluciones<1):
            print(lista_objetos[numeroKirby - 1].nombre, "ya no esta disponible, selecciona otro...")
        else:    
            numeroKirby = numeroKirby - 1
            return lista_objetos[numeroKirby]
    
#Función para buscar el nommbre de un kirby de una lista de kirbies:
def buscar_nombre_kirby(lista_objetos):    
    while True:
        print("Ingresa el número de un kirby sospechoso: (1,2,3,4,5)")
        print("Ingresa una de las siguientes ubicaciones: ")
        print("<<1>>", "Kirby Rojo")
        print("<<2>>", "Kirby Azul")
        print("<<3>>", "Kirby Amarillo")
        print("<<4>>", "Kirby Morado")
        print("<<5>>", "Kirby Rosa")
        numeroKirby = int(input()) 
        if numeroKirby < 0 or numeroKirby > 5:
            print("Ingresa un número correcto")

        else:
            numeroKirby = numeroKirby - 1
            return lista_objetos[numeroKirby].nombre

#Funcion para buscar una ubicacion de un kirby sospechoso
def buscar_ubicacion(kirby_sospechoso_nombre):
    while True:
        print("¿En qué ubicación crees que estaba", kirby_sospechoso_nombre,"?")
        print("Ingresa una de las siguientes ubicaciones: ")
        print("<<1>>", "en la Mansion Luz de luna")
        print("<<2>>", "en la Montaña mostaza")
        print("<<3>>", "en la Ruta arcoiris")
        print("<<4>>", "en el Mar de Olivo")
        print("<<5>>", "en la Gruta del repollo")
        numero_ubicacion_kirby_sospechoso = int(input())
        if(numero_ubicacion_kirby_sospechoso >5 or numero_ubicacion_kirby_sospechoso<0):
            print("Ingresa una ubicacion de la forma correcta")
        else:
            numero_ubicacion_kirby_sospechoso = numero_ubicacion_kirby_sospechoso-1
            ubicacion_kirby_sospechoso = ubicaciones[numero_ubicacion_kirby_sospechoso]
            return ubicacion_kirby_sospechoso
        
#funcion para buscar una accion de un kirby sospechoso        
def buscar_accion(kirby_sospechoso_nombre):
    while True:
        print("¿Cuál acción crees que realizó", kirby_sospechoso_nombre,"?")
        print("Ingresa una de las siguientes ubicaciones: ")
        print("<<1>>", "se ha dormido")
        print("<<2>>", "ha roto el espejo de los laberintos")
        print("<<3>>", "se ha comodido un wadle")
        print("<<4>>", "ha usado la espada sagrada")
        print("<<5>>", "ha tirado el pastel universal")
        numero_accion_kirby_sospechoso = int(input())
        if(numero_accion_kirby_sospechoso >5 or numero_accion_kirby_sospechoso<0):
            print("Ingresa una acción de la forma correcta")
        else:
            numero_accion_kirby_sospechoso = numero_accion_kirby_sospechoso-1
            accion_kirby_sospechoso = acciones[numero_accion_kirby_sospechoso]
            return accion_kirby_sospechoso

#funcion para comprobar las conclusiones realizadas y realizar bonificacion o castigo
def comprobar_conclusiones(kirby_sospechoso, kirby_sospechoso_nombre, kirby_sospechoso_ubicacion, kirby_sospechoso_accion):
    global casos_resueltos
    global casos_disponibles
    contadorAciertos = 0
    print("El", kirby_sospechoso_nombre, ":")
    if (kirby_sospechoso.accion == kirby_sospechoso_accion):
        print("+++Correcto:", kirby_sospechoso_accion)
        contadorAciertos = contadorAciertos + 1
    else:
        print("---Incorrecto:", kirby_sospechoso_accion)
    
    if (kirby_sospechoso.lugar == kirby_sospechoso_ubicacion):
        print("+++Correcto:", kirby_sospechoso_ubicacion)
        contadorAciertos = contadorAciertos + 1
    else:
        print("---Incorrecto:", kirby_sospechoso_ubicacion)
    if(contadorAciertos != 2):
        kirby_sospechoso.limiteDeSoluciones = kirby_sospechoso.limiteDeSoluciones - 1
        print("Has perdido un intento para poder utilizar este kirby, intentos disponibles: ", kirby_sospechoso.limiteDeSoluciones)
    else:
        casos_resueltos += 1
        casos_disponibles -= 1
        kirby_sospechoso.limiteDeSoluciones = 0
        kirby_sospechoso.resuelto = True

#Función para dar pistas sobre la ubicación o acción de un Kirby sospechoso
def dar_pista(kirby_sospechoso):
    while kirby_sospechoso.limiteDeSoluciones != 0:
        print("¿Necesitas una pista sobre la ubicación o la acción de", kirby_sospechoso.nombre,"?")
        print("<<1>> Pista sobre la ubicación")
        print("<<2>> Pista sobre la acción")
        print("<<3>> No necesito pistas")
        
        opcion = int(input())
        if opcion == 1:
            print(f"Pista sobre la ubicación de {kirby_sospechoso.nombre}: {kirby_sospechoso.lugar}")
            break
        elif opcion == 2:
            print(f"Pista sobre la acción de {kirby_sospechoso.nombre}: {kirby_sospechoso.accion}")
            break
        elif opcion == 3:
            break
        else:
            print("Elige una opción válida")
            
#Comprobar el kirby actual y si no tiene más intentos reducir el número de casos disponibles
def comprobar_casos_disponibles(kirby_sospechoso):
    global casos_disponibles
    if (kirby_sospechoso.limiteDeSoluciones == 0 and kirby_sospechoso.resuelto == False):
        casos_disponibles -= 1
        
        
#Juego    
while True:
    mostrar_historia()
    print(f"Hay <<{casos_resueltos}>> casos resueltos, y <<{casos_disponibles}>> casos disponibles...")
    kirby_sospechoso = buscar_kirby(objetos_kirby)
    kirby_sospechoso_nombre = kirby_sospechoso.nombre
    kirby_sospechoso_ubicacion = buscar_ubicacion(kirby_sospechoso_nombre)
    kirby_sospechoso_accion = buscar_accion(kirby_sospechoso_nombre)        
    comprobar_conclusiones(kirby_sospechoso, kirby_sospechoso_nombre, kirby_sospechoso_ubicacion, kirby_sospechoso_accion)
    comprobar_casos_disponibles(kirby_sospechoso)
    if(casos_disponibles > 0):
        dar_pista(kirby_sospechoso)
    else: 
        print("ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº")
        print(f"El juego ha terminado, tu puntuacion es de <<{casos_resueltos}>> casos resuletos")
        print("¿Desea volver a jugar? s/n")
        if("s" == input()):
            casos_resueltos = 0
            casos_disponibles = 5
            historia_mostrada = False
            # Lista de nombres de objetos de Kirby
            nombres_objetos = ["Kirby Rojo", "Kirby Azul", "Kirby Amarillo", "Kirby Morado", "Kirby Rosa"]
            acciones_posibles = ["se ha dormido", "ha roto el espejo de los laberintos", "se ha comodido un Waddle Dee", "ha usado la espada sagrada", "ha tirado el pastel universal"]
            lugares_posibles = ["en la Mansion Luz de luna", "en la Montaña mostaza", "en la Ruta arcoiris", "en el Mar de Olivo", "en la Gruta del repollo"]

            # Crear instancias de objetos de Kirby con acciones y lugares aleatorios
            del objetos_kirby
            objetos_kirby = []
            for nombre_objeto in nombres_objetos:
                accion_aleatoria, lugar_aleatorio = random.sample(acciones_posibles, 1), random.sample(lugares_posibles, 1)
                print("")
                objeto = ObjetoKirby(nombre_objeto, accion_aleatoria[0], lugar_aleatorio[0])
                objetos_kirby.append(objeto)
                # Eliminar las acciones y lugares usados para evitar repeticiones
                acciones_posibles.remove(accion_aleatoria[0])
                lugares_posibles.remove(lugar_aleatorio[0])
                
                print("ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº")
                
        else:    
            print("ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº")
            break
    print("-------------------------------------------------------------------------------------------------------------------------")
            
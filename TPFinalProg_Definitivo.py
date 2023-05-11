##Trabajo Practico Final:

libros = [['1984', 'George Orwell', 'ZigZag', 2005, 'Ciencia Ficcion', 380, 180699], 
              ['Nada', 'Carmen Laforet', 'Destino', 2011, 'Novela', 283, 180698], 
              ['Los Miserables', 'Victor Hugo', 'JAR', 1970, 'Ficcion', 1090, 847699], 
              ['La Divina Comedia', 'Dante', 'Akal', 2005, 'Comedia', 1984, 187458], 
              ['El Alquimista', 'Paulo Coehlo', 'Grijalbo', 2015, 'Novela', 172, 158799],
              ['Rebelión en la Granja', 'George Orwell', 'ZigZag', 2006, 'Ciencia Ficcion', 380, 180700]]


    
##Alta de Libros
def alta_libro(libros):
    print("Se va a registrar un libro")
    nuevo_libro = [] ##esta es la lista vacia para el nuevo libro
    while True:##mientras este todo bien
        ISBN = input("Ingresar el ISBN del libro nuevo(Escribir -salir- para volver hacia atras): ")
        if ISBN == "salir": ##esto esta hecho por si te equivocaste de opcion para que quede mas lindo 
            return None ##para que no devuelva mas y solo vaya para atras
        elif ISBN.isdecimal(): ##si el numero ingresado es verdaderamente un numero
            ISBN = int(ISBN)##lo convertimos a un numero integrador
            datos = ["titulo", "autor", "editorial", "año", "genero", "paginas", "ISBN"]
            if any(l[6] == ISBN for l in libros): ##si hay algun numero que concuerde con el numero isbn de cualquier libro
                print("Este libro ya se encuentra en la base de datos")
                pass ##el pass se agrego pra que no se cuelgue si el libro esta en la base de datos
            else:
                print("Nuevo libro para ingresar")
                for d in datos: ##d seria como cada item adentro de los datos para el libro
                    if d == "ISBN":
                        nuevo_libro.append(ISBN) ##si es un numero isbn con el append lo agrego a la lista vacia
                    else:
                        item = input(f"Ingrese {d} del libro (Escribir -salir- para volver hacia atras o -cancelar- para empezar de nuevo): ")##esta f' al principio es para poder poner una variable adentro del texto
                        if item == "cancelar":
                            nuevo_libro = []##si escribimos cancelar la lista vuelve a estar vacia 
                            break ##este break lo que hace es parar el programa para que vuelva para atras, si no sigue
                        elif item == "salir":
                            nuevo_libro = []
                            return None ##lo mismo con esto si no sigue
                        else:
                            if d == "año" or d == "paginas":    ##este else esta hecho para que si o si en año y paginas se ponga un numero
                                while not item.isdecimal():
                                    print("Este item debe ser un numero")
                                    item = input(f"Ingrese {d} del libro (Escribir -salir- para volver hacia atras o -cancelar- para empezar de nuevo): ")
                            else:
                                pass  ##si tiene numero que siga maestro
                            nuevo_libro.append(item) ##con este agrefariamos todos los items anteriores a la lista
        else:
            print("El valor ingresado no es numerico, por favor intentelo de nuevo")

        if d == datos[-1] and len(nuevo_libro) == 7:
            libros.append(nuevo_libro)
            return nuevo_libro


##Baja de Libros
def baja_libro(libros):
    while True:
        ISBN = input("Ingresar el ISBN del libro deseado(Escribir -salir- para volver hacia atras): ")
        if ISBN == "salir":
            return None ##para que no devuelva mas y solo vaya para atras
        elif ISBN.isdecimal(): ##si es un numero
            ISBN = int(ISBN)#convertir este numero en int (y todos los demas tmb) es para que sea compatible con todos los numeros por si hay algun integrer
            if any(l[6] == ISBN for l in libros):   ##si hay aalgun numero isbn que concuerde con alguno de los libros
                print("Este libro ya se encuentra en la base de datos")
                respuesta = input("seguro que se quiere dar de baja?(si o no): ") 
                if respuesta == "si":
                    libros = [l for l in libros if not l[6] == ISBN] ##la primera l la puse porque si no tira error si empiezo con el for
                    print("El libro se ha eliminado")
                    print(libros)
                    print(ISBN)
                    return libros ##lo que hace este return es que te devuelve directo al menu principal si no te pide denuevo otro isbn y tenes que escribir salir para volver
                elif respuesta == "no":
                    pass
                else:
                    print("Debe de responder con si y no!!!!!")
            else:
                print("El libro no se encuentra en la base de datos")
        else:
            print("Tiene que ser un numero!!")


##Buscar Libros
def buscar_libro(libros):
    while True:
        titulo = input("Ingresar el titulo del libro deseado(Escribir -salir- para volver hacia atras): ")
        if titulo == "salir":
            return None ##para que vuelva al menu principal y no pase nada
        else:
            if any(l[0].lower() == titulo.lower() for l in libros): ##los lowers agregados son para que no se tenga que poner una mayuscula al principio
                print("El libro se encuentra en la base datos")
                libro = [l for l in libros if titulo in l[0]. lower()]
                print(libro)
                return None ##para que devuelva la variable libro de mas arriba(aca por lo visto se puede poner un return libros tambien ya que es lo mismo(si se borra te vuelve a preguntar constantemente que libro queres y tenes que escribir salir para volver al menu))
            else:
                print("No hay libros en la base de datos")

##Modificar Libros
def modificar_libro(libros):
    while True:
        libro = input("Ingresar el titulo del libro deseado(Escribir -salir- para volver hacia atras): ")
        if libro == "salir":
            return None
        else:
            if any(l[0].lower() == libro.lower() for l in libros):
                print("El libro se encuentra en la base datos")
                libro = [l for l in libros if libro in l[0]. lower()]
                print(libro)
                ##en esta parte y mas arriba tambien se copio y pego lo mismo que esta en buscar libros ya que si se llamaba a la funcion no funcionaba bien
            
                print("Que desea modificar?")
                print("<3================Ɛ>")
                print("1) Titulo")
                print("2) Autor")
                print("3) Editorial")
                print("4) Año")
                print("5) Genero")
                print("6) Paginas")
                print("7) ISBN")
                print("8) Cancelar")
                print("<3================Ɛ>")
                seleccion = input("Elija una opcion(Escribir -salir- para volver hacia atras): ")
                if seleccion == "salir":
                    return None
                elif seleccion.isdecimal():
                    seleccion = int(seleccion)
                    if seleccion == 8:
                        break
                    else:
                        modificar = input("Introduzca su reemplazo(Escribir -salir- para volver hacia atras o -cancelar- para empezar de nuevo): ")
                        if modificar == "cancelar":
                            pass
                        elif modificar == "salir":
                            return None
                        else:
                            if seleccion == 4 or seleccion == 6 or seleccion == 7:
                                while not modificar.isdecimal(): ##esto se agrego para que solo se pueda contestar con numeros
                                    print("Debe ser un numero!!")
                                    modificar = input("Ingrese un dato numerico: ")
                                modificar = int(modificar)
                            else:
                                pass
                            indice = libros.index(libro[0])
                            libros[indice][seleccion-1] = modificar ##el [indice] indica la posicion del libro que se busca y el [seleccion-1] busca la posicion del dato que estas cambiando
                else:
                    print("Por favor, ingrese un numero")
            else:
                print("No hay libros en la base de datos")

##Listados(esta hecho de la misma forma que el menu principal pero aca se imprime las diferentes opciones)
def listados(libros):
    while True:
        print("Que quiere inspeccionar?")
        print("<3====================Ɛ>")
        print("1) Todos los autores")
        print("2) Todos los libros")
        print("3) Libros por genero")
        print("4) Libros por autor")
        print("5) Autores por editorial")
        print("6) Libros por editorial")
        print("7) Salir")
        seleccion = input("Ingrese alguna opcion: ")
        if seleccion == "salir":
            return None
        elif seleccion.isdecimal():
            seleccion = int(seleccion)
            if seleccion == 7:
                break
            else:
                if seleccion == 1:
                    todos_autores = list(set([a[1] for a in libros])) ##el list se agrego ya que note que si no imprimia lo mismo pero con llaves, de esta manera me lo convierte a una lista[]
                    print(todos_autores)##el set se agrego para que no se me repitan los items 

                elif seleccion == 2:
                    print(libros)

                elif seleccion == 3:
                    genero = input("Elija un genero(Escribir -salir- para volver hacia atras): ")
                    libros_genero = [i for i in libros if i[4].lower() == genero.lower()]
                    print(libros_genero)

                elif seleccion == 4:
                    autor = input("Elija un autor(Escribir -salir- para volver hacia atras): ")
                    libros_autor = [i for i in libros if i[1].lower() == autor.lower()]
                    print(libros_autor)

                elif seleccion == 5:
                    editorial = input("Elija una editorial(Escribir -salir- para volver hacia atras): ")
                    autores_editorial = list(set([i[1] for i in libros if i[2].lower() == editorial.lower()]))##lo mismo con el list y el set de mas arriba
                    print(autores_editorial)

                elif seleccion == 6:
                    editorial1 = input("Elija una editorial(Escribir -salir- para volver hacia atras): ")
                    libros_editorial = [i for i in libros if i[2].lower() == editorial1.lower()] ##los i al principio de cada corchete esta puesto por que si no no me deja poner el for ahi adentro como esta
                    print(libros_editorial)

                else:
                    print("Esta opcion no existe por favor intentelo de nuevo!")




##Menu principal(donde se llaman a las funciones y si imprime el "menu")


while True:
    print("<3==============Ɛ>")
    print("La mejor bilioteca")
    print("<3==============Ɛ>")
    print("1) Alta de Libros")
    print("2) Baja de Libros")
    print("3) Buscar Libros")
    print("4) Modificar Libros")
    print("5) Listados")

    opcion = int(input("Ingrese alguna opcion: "))
    if opcion == 1:
        alta_libro(libros)
    elif opcion == 2:
        baja_libro(libros)
    elif opcion == 3:
        buscar_libro(libros)
    elif opcion == 4:
        modificar_libro(libros)
    elif opcion == 5:
        listados(libros)
    else:
        print("Esa opcion no existe, intenta de nuevo por favor")

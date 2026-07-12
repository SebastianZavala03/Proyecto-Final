# Listas
# Datos de los productos
codigosVestidos = [1, 2, 3, 4, 5, 6]

# Datos de tipo cadena
nombresVestidos = [
    "Vestido rojo",
    "Vestido azul",
    "Vestido verde",
    "Vestido anaranjado",
    "Vestido turquesa",
    "Vestido negro"
]

# Datos de tipo cadena
descripcionesVestidos = [
    "Perfecto para Salir",
    "Perfecto para la noche",
    "Perfecto para la playa",
    "Perfecto para Fiestas",
    "Perfecto para un día de otoño",
    "Perfecto para gala"
]

# Datos de tipo float
preciosVestidos = [
    75.00,
    80.90,
    130.00,
    190.60,
    65.20,
    190.50
]

# Datos de tipo entero
stockVestidos = [
    10,
    8,
    3,
    2,
    20,
    30
]
# Se crea una función para registrar la venta de un producto.
def registrarVenta():
    nombreCliente = input("Nombre del cliente: ")





# Se crea una función para mostrar el catálogo.
def mostrarCatalogo():

    # Muestra el título del catálogo.
    print("CATÁLOGO DE VESTIDOS")

    # Se utiliza un ciclo for para recorrer todos los productos de la lista.
    # La función len(codigosVestidos) obtiene la cantidad total de productos registrados.
    # Luego, range() genera las posiciones desde el indice 0 hasta el último producto de la lista.

    for i in range(len(codigosVestidos)):

        # Se muestran los datos de cada producto utilizando la misma posición
        # de las listas paralelas.
        print(
            codigosVestidos[i],
            "-",
            nombresVestidos[i],
            "- S/.",
            preciosVestidos[i],
            "- Stock:",
            stockVestidos[i]
        )

    # Espera que el usuario presione Enter para regresar al menú.
    input("Presione Enter para continuar")



def mostrarProducto():

     #El usuario ingresa el código del vestido.
    codigoVestido = int(input("Ingrese el código del vestido: "))

     #Se inicializa la variable en -1 porque eso da a indicar que el valor no se a encontrado.
    posicionVestido = -1

    #Recorre la lista de los productos por medio del codigo de vestido 
    for i in range(len(codigosVestidos)):

        # Si el código ingresado es igual al código de la lista,
        # se guarda la posición donde fue encontrado.
        if codigosVestidos[i] == codigoVestido:
            posicionVestido = i

    #Realizamos una condicional que indique si esque el codigo no fue encontrado nos mande un mensaje y en caso si se encuentre recorre el producto.
    if posicionVestido == -1:
        print("Ese código que ingresaste no existe")
    else:
        print("Vestido:", nombresVestidos[posicionVestido])
        print("Descripción:", descripcionesVestidos[posicionVestido])
        print("Precio:", preciosVestidos[posicionVestido])
        print("Stock:", stockVestidos[posicionVestido])

    input("Presione Enter para continuar")




# Función que muestra el menú
def menu():

    # Variable que almacena la opción elegida por el usuario.
    opcion = 0

    # Repite el menú mientras el usuario no seleccione la opcion 4.
    while opcion != 4:

        print("MIRIAN ATELIER")
        print("1. Ver catálogo")
        print("2. Buscar vestido")
        print("3. Registrar venta")
        print("4. Salir")

        # Solicita al usuario una opcion que este dentro del menu
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            mostrarCatalogo()
        elif opcion == 2:
            mostrarProducto()
        

# Llama 
menu()
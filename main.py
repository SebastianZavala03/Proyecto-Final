#Listas
# Datos de los Productos
codigosVestidos = [1, 2, 3, 4, 5, 6]

#Datos de tipo cadena
nombresVestidos = [
    "Vestido rojo",
    "Vestido azul",
    "Vestido verde",
    "Vestido anaranjado",
    "Vestido turquesa",
    "Vestido negro"
]

#Datos de tipo cadena
descripcionesVestidos = [
    "Perfecto para Salir",
    "Perfecto para la noche",
    "Perfecto para la playa",
    "Perfecto para Fiestas",
    "Perfecto para un dia de otoño",
    "Perfecto para gala"
]

#Datos de tipo float
preciosVestidos = [
    75.00,
    80.90,
    130.00,
    190.60,
    65.20,
    190.50
]


#Datos de tipo entero
stockVestidos = [
    10,
    8,
    3,
    2,
    20,
    30
]


# Función que muestra el menú
def menu():
    # Variable que almacena la opcion a eligir                      
    opcion = 0                  

    # Repite el menú mientras el usuario no seleccione la opción 4 (Salir).
    while opcion != 4:          

        print("MIRIAN ATELIER")  
        print("1. Ver catálogo")               
        print("2. Buscar vestido")            
        print("3. Registrar venta")           
        print("4. Salir")                     

        # Solicita al cliente una opción por terminal, la convierte a entero y la guarda en la variable opcion.
        opcion = int(input("Elige una opción: "))  

#Llama a la funcion
menu()  
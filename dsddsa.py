# Definimos una lista para almacenar las notas
copilador_de_notas = [
    "Metodos de investigacion",
    "Manera de auto lecionarse",
    "No idea",
]

# Creamos un diccionario para caractalogar

carpetas = {
    "General": copilador_de_notas,
}


# Mostrar catalogos disponibles
def imprimir_carpetas():
    carpetas_vista = carpetas.keys()
    carpetas_vista2 = "\n".join(map(str, carpetas_vista))
    print(carpetas_vista2)


# Seleccionar carpetas para agregar notas
def imprimir_carpeta():
    carpeta_seleccionada = input("Seleccione la carpeta para agregar la nota: ")

    if carpeta_seleccionada in carpetas:
        nueva_nota = input("Ingrese la nueva nota: ")
        carpetas[carpeta_seleccionada].append(nueva_nota)
        print(f"Nota agregada a la carpeta '{carpeta_seleccionada}' con éxito. \n")
    else:
        print(f"La carpeta '{carpeta_seleccionada}' no existe.")


# Funcion para crear un catalogo
def agregar_catalogo():
    nuevo_catalogo = input("Ingrese el nombre de la carpeta: ").capitalize()
    carpetas[nuevo_catalogo] = []
    print(f"Carpeta {nuevo_catalogo} creada con exito")


# Función para imprimir las notas disponibles
def imprimir_notas():
    contado = len(copilador_de_notas)

    if contado == 0:
        print("No hay ninguna nota disponible.")
    elif contado == 1:
        print(f"1 nota disponible:\n")
    else:
        print(f"{contado} notas disponibles:\n")
    listas_notas = "\n".join(map(str, copilador_de_notas))
    print(listas_notas)


# Función para agregar una nueva nota
def agregar_nota():
    nueva_nota = input("Ingrese la nueva nota: ")
    copilador_de_notas.append(nueva_nota)
    print("Nota agregada con éxito.")


# Función para editar una nota existente
def editar_nota():
    imprimir_notas()
    indice = int(input("Ingrese el número de la nota que desea editar: ")) - 1
    if 0 <= indice < len(copilador_de_notas):
        nueva_nota = input("Ingrese la nueva versión de la nota: ")
        copilador_de_notas[indice] = nueva_nota
        print("Nota editada con éxito.")
    else:
        print("Índice no válido.")


# Función para eliminar una nota existente
def eliminar_nota():
    indice = int(input("Ingrese el número de la nota que desea eliminar: ")) - 1
    if 0 <= indice < len(copilador_de_notas):
        nota_eliminada = copilador_de_notas.pop(indice)
        print(f"Nota '{nota_eliminada}' eliminada con éxito.")
    else:
        print("Índice no válido.")


# Función para buscar notas por palabra clave
def buscar_notas():
    palabra_clave = input("Ingrese la palabra clave para buscar notas: ")
    notas_encontradas = [
        nota for nota in copilador_de_notas if palabra_clave.lower() in nota.lower()
    ]

    if notas_encontradas:
        print(f"\nNotas que contienen '{palabra_clave}':\n")
        print("\n".join(notas_encontradas))
    else:
        print(f"No se encontraron notas que contengan '{palabra_clave}'.")


def seleccionar_carpeta():
    seleccionar_carpeta = input("Abrir carpeta: ").capitalize()

    if seleccionar_carpeta in carpetas:
        print(f"\n Notas en la carpeta '{seleccionar_carpeta}':")
        for nota in carpetas[seleccionar_carpeta]:
            print(f"\n -{nota}")

        while True:
            print("\nOpciones para la carpeta:")
            print("1. Ver notas")
            print("2. Agregar nota")
            print("3. Editar nota")
            print("4. Eliminar nota")
            print("5. Buscar notas")
            print("6. Volver al menú principal")

            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                for nota in carpetas[seleccionar_carpeta]:
                    print(f"\n -{nota}")
            elif opcion == "2":
                nueva_nota = input("Ingrese la nueva nota: ")
                carpetas[seleccionar_carpeta].append(nueva_nota)
                print(f"Nota agregada a la carpeta '{seleccionar_carpeta}' con éxito.")
            elif opcion == "3":
                editar_nota()
                pass
            elif opcion == "4":
                eliminar_nota()
                pass
            elif opcion == "5":
                buscar_notas()
                pass
            elif opcion == "6":
                # Volver al menu principal.
                break
            else:
                print("Opción no válida. Por favor, elija una opción del 1 al 6.")
    else:
        print(f"La carpeta '{seleccionar_carpeta}' no existe.")


# Bienvenida
print("\nBienvenido a la Gestión de Notas Estudiantiles.\n ")

print(f"Carpetas disponibles: \n" + "\n ".join(carpetas))

while True:
    # print(f"\n Carpetas disponibles: \n" + "\n ".join(carpetas))
    # Menú de opciones
    print("\nMenú:")
    print("1. Ver carpetas")
    print("2. Crear nueva carpeta  ")
    # print("3. Agregar nota a carpeta")
    print("3. Abrir carpeta")
    print("4. Salir y borrar el programa")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        imprimir_carpetas()
    elif opcion == "2":
        agregar_catalogo()
    elif opcion == "3":
        seleccionar_carpeta()
    elif opcion == "5":
        seleccionar_carpeta()
    elif opcion == "10":
        buscar_notas()
    elif opcion == "6":
        buscar_notas()
    elif opcion == "7":
        imprimir_carpetas()
    elif opcion == "8":
        imprimir_carpeta()
    elif opcion == "9":
        seleccionar_carpeta()
    elif opcion == "4":
        print("Gracias por utilizar la Gestión de Notas Estudiantiles. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 9.")
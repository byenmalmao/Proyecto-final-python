# Gestion De Notas creado por Enmanuel Gonzalez 2022-0228 y Breylin Ureña 2020-1055

# Creamos un diccionario para caractalogar y alamcenar datos en forma de lista
notas = {
    "General": [
        "Metodos de investigacion",
        "Manera de autocontrol",
        "No idea",
    ]
}


# Mostrar catalogos disponibles
def imprimir_carpetas():
    carpetas_vista = notas.keys()
    # carpetas_vista2 = "\n".join(map(str, carpetas_vista))
    print(f"\nCarpetas disponibles: \n" + "\n".join(carpetas_vista))


# Función para imprimir las notas disponibles
def imprimir_notas(carpeta):
    notas_carpeta = notas.get(carpeta, [])
    cantidad = len(notas_carpeta)

    if cantidad == 0:
        print("No hay ninguna nota disponible en esta carpeta.")
    elif cantidad == 1:
        print(f"1 nota disponible en la carpeta '{carpeta}':\n")
    else:
        print(f"{cantidad} notas disponibles en la carpeta '{carpeta}':\n")

    for i, nota in enumerate(notas_carpeta):
        print(f"{i + 1}. {nota}")


# Función para agregar una nueva nota
def agregar_nota(carpeta):
    nueva_nota = input("Ingrese la nueva nota: ")
    notas[carpeta].append(nueva_nota)

    print(f"Nota agregada a la carpeta '{carpeta}' con éxito.")


# Función para editar una nota existente
def editar_nota(carpeta):
    imprimir_notas(carpeta)

    indice = int(input("Ingrese el número de la nota que desea editar: ")) - 1
    if 0 <= indice < len(notas[carpeta]):
        nueva_nota = input("Ingrese la nueva versión de la nota: ")
        notas[carpeta][indice] = nueva_nota
        print("Nota editada con éxito.")
    else:
        print("Índice no válido.")


# Función para eliminar una nota existente
def eliminar_nota(carpeta):
    imprimir_notas(carpeta)

    if notas[carpeta]:
        indice = int(input("Ingrese el número de la nota que desea eliminar: ")) - 1
        if 0 <= indice < len(notas[carpeta]):
            nota_eliminada = notas[carpeta].pop(indice)
            print(f"Nota '{nota_eliminada}' eliminada con éxito.")
        else:
            print("Índice no válido.")
    else:
        print("No hay notas para eliminar.")


# Función para buscar notas por palabra clave
def buscar_notas():
    palabra_clave = input("Ingrese la palabra clave para buscar notas: ")
    notas_encontradas = []

    for carpeta, notas_carpeta in notas.items():
        for nota in notas_carpeta:
            if palabra_clave.lower() in nota.lower():
                notas_encontradas.append((carpeta, nota))

    if notas_encontradas:
        print(f"\nNotas que contienen '{palabra_clave}':\n")
        for carpeta, nota in notas_encontradas:
            print(f"{carpeta}: {nota}")
    else:
        print(f"No se encontraron notas que contengan '{palabra_clave}'.")


def seleccionar_carpeta():
    carpeta_seleccionada = input("Abrir carpeta: ").capitalize()

    if carpeta_seleccionada in notas:
        print(f"\nNotas en la carpeta '{carpeta_seleccionada}':")
        imprimir_notas(carpeta_seleccionada)

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
                imprimir_notas(carpeta_seleccionada)
            elif opcion == "2":
                agregar_nota(carpeta_seleccionada)
            elif opcion == "3":
                editar_nota(carpeta_seleccionada)
            elif opcion == "4":
                eliminar_nota(carpeta_seleccionada)
            elif opcion == "5":
                buscar_notas()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, elija una opción del 1 al 6.")
    else:
        print(f"La carpeta '{carpeta_seleccionada}' no existe.")


# Funcion para crear un catalogo
def agregar_carpeta():
    nueva_carpeta = input("Ingrese el nombre de la carpeta: ").capitalize()
    notas[nueva_carpeta] = []
    print(f"Carpeta '{nueva_carpeta}' creada con éxito.")


# Funcion para editar un catalogo
def editar_carpeta():
    carpeta_a_editar = input(
        "Ingrese el nombre de la carpeta que desea editar: "
    ).capitalize()

    if carpeta_a_editar in notas:
        nuevo_nombre = input("Ingrese el nuevo nombre de la carpeta: ").capitalize()
        notas[nuevo_nombre] = notas[carpeta_a_editar]
        del notas[carpeta_a_editar]
        return f"Carpeta '{carpeta_a_editar}' editada con éxito. Nuevo nombre: '{nuevo_nombre}'."
    else:
        return f"La carpeta '{carpeta_a_editar}' no existe. No se pudo editar."


# Funcion para eliminar un catalogo
def eliminar_carpeta():
    carpeta_a_eliminar = input(
        "Ingrese el nombre de la carpeta que desea eliminar: "
    ).capitalize()

    if carpeta_a_eliminar in notas:
        notas.pop(carpeta_a_eliminar)
        return f"Carpeta '{carpeta_a_eliminar}' eliminada con éxito."
    else:
        return f"La carpeta '{carpeta_a_eliminar}' no existe. No se pudo eliminar."


# Bienvenida
print("\nBienvenido a la Gestión de Notas Estudiantiles.\n")
print(f"\nCarpetas disponibles: \n" + "\n ".join(notas))
while True:
    # Menú de opciones
    print("\nMenú:")
    print("1. Ver carpetas")
    print("2. Crear nueva carpeta")
    print("3. Abrir carpeta")
    print("4. Editar carpeta")
    print("5. Eliminar carpeta")
    print("6. Salir")
    print("7. Información del programa")

    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        imprimir_carpetas()
    elif opcion == "2":
        agregar_carpeta()
    elif opcion == "3":
        seleccionar_carpeta()
    elif opcion == "4":
        editar_carpeta()
    elif opcion == "5":
        eliminar_carpeta()
    elif opcion == "6":
        print("Gracias por utilizar la Gestión de Notas Estudiantiles. ¡Hasta luego!")
        break
    elif opcion == "7":
        print(
            "Esta aplicación es un gestor de notas con el objetivo de organizar y almacenar información,\n",
            "como apuntes o tareas de manera digital. Facilita la gestión y el acceso rápido a la información,\n"
            "ayudando a los usuarios a mantenerse organizados y tener un mejor seguimiento de sus actividades.",
        )
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 7.")

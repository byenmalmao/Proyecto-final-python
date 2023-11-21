copilador_de_notas = [
    "Metodos de investigacion",
    "Manera de auto lecionarse",
    "No idea",
]
carpetas = {"General": copilador_de_notas}


def imprimir_carpetas():
    print("\n".join(carpetas.keys()))


def imprimir_carpeta():
    carpeta_seleccionada = input("Seleccione la carpeta para agregar la nota: ")
    if carpeta_seleccionada in carpetas:
        nueva_nota = input("Ingrese la nueva nota: ")
        carpetas[carpeta_seleccionada].append(nueva_nota)
        print(f"Nota agregada a la carpeta '{carpeta_seleccionada}' con éxito.")
    else:
        print(f"La carpeta '{carpeta_seleccionada}' no existe.")


def agregar_catalogo():
    nuevo_catalogo = input("Ingrese el nombre de la carpeta: ").capitalize()
    carpetas[nuevo_catalogo] = []
    print(f"Carpeta {nuevo_catalogo} creada con exito")


def imprimir_notas():
    notas = "\n".join(copilador_de_notas)
    print(f"{len(copilador_de_notas)} notas disponibles:\n{notas}")


def agregar_nota():
    nueva_nota = input("Ingrese la nueva nota: ")
    copilador_de_notas.append(nueva_nota)
    print("Nota agregada con éxito.")


def editar_nota():
    imprimir_notas()
    indice = int(input("Ingrese el número de la nota que desea editar: ")) - 1
    if 0 <= indice < len(copilador_de_notas):
        nueva_nota = input("Ingrese la nueva versión de la nota: ")
        copilador_de_notas[indice] = nueva_nota
        print("Nota editada con éxito.")
    else:
        print("Índice no válido.")


def eliminar_nota():
    imprimir_notas()
    if copilador_de_notas:
        indice = int(input("Ingrese el número de la nota que desea eliminar: ")) - 1
        if 0 <= indice < len(copilador_de_notas):
            nota_eliminada = copilador_de_notas.pop(indice)
            print(f"Nota '{nota_eliminada}' eliminada con éxito.")
        else:
            print("Índice no válido.")
    else:
        print("No hay notas para eliminar.")


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
                break
            else:
                print("Opción no válida. Por favor, elija una opción del 1 al 6.")
    else:
        print(f"La carpeta '{seleccionar_carpeta}' no existe.")


print("\nBienvenido a la Gestión de Notas Estudiantiles.\n ")

while True:
    print("\nMenú:")
    print("1. Ver carpetas")
    print("2. Crear nueva carpeta")
    print("3. Abrir carpeta")
    print("4. Salir y borrar el programa")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        imprimir_carpetas()
    elif opcion == "2":
        agregar_catalogo()
    elif opcion == "3":
        seleccionar_carpeta()
    elif opcion == "4":
        print("Gracias por utilizar la Gestión de Notas Estudiantiles. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 4.")

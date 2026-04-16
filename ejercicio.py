agenda = {}

while True:
    print("\n1.Agregar  2.Consultar  3.Eliminar  4.Mostrar  5.Salir")
    op = input("Opción: ")

    if op == "1":
        n = input("Nombre: ").upper()
        agenda[n] = input("Teléfono: ")

    elif op == "2":
        n = input("Nombre: ").upper()
        print("Tel:", agenda.get(n, "No existe"))

    elif op == "3":
        n = input("Nombre: ").upper()
        print("Eliminado" if agenda.pop(n, None) else "No existe")

    elif op == "4":
        print(agenda if agenda else "Agenda vacía")

    elif op == "5":
        print("Saliste. Presiona 't' para volver o cualquier otra tecla para terminar.")
        if input().lower() != "t":
            break

    else:
        print("Opción inválida")
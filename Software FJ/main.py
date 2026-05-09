from modelos import *
from excepciones import *

clientes = []
reservas = []

servicios = [
    Sala("Sala Premium", 50),
    Equipo("Portátil", 40),
    Asesoria("Consultoría", 80)
]


def registrar_cliente():
    try:
        nombre = input("Nombre: ")
        documento = input("Documento: ")
        correo = input("Correo: ")

        c = Cliente(nombre, documento, correo)
        clientes.append(c)

        print("Cliente registrado.")
        registrar_log("INFO", "Cliente registrado")

    except Exception as e:
        print("Error:", e)
        registrar_log("ERROR", str(e))


def ver_clientes():
    if not clientes:
        print("No hay clientes.")
        return

    for i, c in enumerate(clientes, 1):
        print(i, "-", c.mostrar_info())


def crear_reserva():
    try:
        if not clientes:
            print("Debe registrar clientes primero.")
            return

        ver_clientes()
        pos = int(input("Seleccione cliente: ")) - 1

        print("\nServicios:")
        for i, s in enumerate(servicios, 1):
            print(i, "-", s.nombre)

        ser = int(input("Seleccione servicio: ")) - 1
        horas = int(input("Horas: "))

        r = Reserva(clientes[pos], servicios[ser], horas)
        total = r.procesar()

        reservas.append(r)

        print("Reserva exitosa.")
        print("Total a pagar:", total)

    except Exception as e:
        print("Error:", e)
        registrar_log("ERROR", str(e))


def ver_reservas():
    if not reservas:
        print("No hay reservas.")
        return

    for r in reservas:
        print(
            r.cliente.nombre,
            "-",
            r.servicio.nombre,
            "-",
            r.estado,
            "-",
            r.horas,
            "horas"
        )


def pruebas_automaticas():
    datos = [
        ("Jose", "1010", "josebarrios@gmail.com"),
        ("vargas", "2020", "vargas@gmail.com"),
        ("Yesid", "3030", "yesid@gmail.com"),
        ("Yesid", "1020", "yesid@gmail.com"),
    ]

    for d in datos:
        try:
            c = Cliente(*d)
            clientes.append(c)
            print("Cliente creado:", c.nombre)
        except Exception as e:
            print("Error:", e)

    try:
        r1 = Reserva(clientes[0], servicios[0], 2)
        print("Total:", r1.procesar())
        reservas.append(r1)

        r2 = Reserva(clientes[1], servicios[2], -1)

    except Exception as e:
        print("Error prueba:", e)


def menu():
    while True:
        print("\n===== SOFTWARE FJ =====")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Crear reserva")
        print("4. Ver reservas")
        print("5. Ejecutar pruebas")
        print("6. Salir")

        op = input("Seleccione: ")

        if op == "1":
            registrar_cliente()

        elif op == "2":
            ver_clientes()

        elif op == "3":
            crear_reserva()

        elif op == "4":
            ver_reservas()

        elif op == "5":
            pruebas_automaticas()

        elif op == "6":
            print("Sistema cerrado.")
            break

        else:
            print("Opción inválida")


menu()
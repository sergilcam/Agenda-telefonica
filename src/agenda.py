"""Agenda telefonica de consola.

Proyecto educativo de 2.o de Bachillerato.
Usa programacion estructurada: solo funciones y una lista de diccionarios.
Cada contacto es un diccionario: {"nombre": ..., "telefono": ...}.
El telefono se guarda como texto para conservar ceros y el prefijo +34.
"""

RUTA_DATOS = "data/contactos.txt"
SEPARADOR = ";"


def mostrar_menu():
    """Muestra por pantalla las opciones disponibles."""
    print("\n--- AGENDA TELEFONICA ---")
    print("1. Anadir contacto")
    print("2. Buscar por nombre")
    print("3. Buscar por numero")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("0. Salir")


def pedir_opcion():
    """Pide la opcion del menu y la devuelve sin espacios."""
    opcion = input("Elige una opcion: ")
    return opcion.strip()


def pedir_nombre():
    """Pide un nombre y lo devuelve sin espacios delante ni detras."""
    nombre = input("Nombre: ")
    return nombre.strip()


def pedir_telefono():
    """Pide un telefono y lo devuelve sin espacios delante ni detras."""
    telefono = input("Telefono: ")
    return telefono.strip()


def crear_contacto(nombre, telefono):
    """Crea un contacto con un nombre y un telefono."""
    return {"nombre": nombre, "telefono": telefono}


def anadir_contacto(agenda, contacto):
    """Anade un contacto a la lista agenda."""
    agenda.append(contacto)


def buscar_por_nombre(agenda, nombre):
    """Busca contactos cuyo nombre contenga el texto dado.

    No distingue entre mayusculas y minusculas.
    Devuelve una lista con los encontrados (puede estar vacia).
    """
    encontrados = []
    texto = nombre.strip().lower()
    for contacto in agenda:
        if texto in contacto["nombre"].lower():
            encontrados.append(contacto)
    return encontrados


def buscar_por_numero(agenda, numero):
    """Busca contactos cuyo telefono contenga el texto dado.

    El numero se compara como texto.
    Devuelve una lista con los encontrados (puede estar vacia).
    """
    encontrados = []
    texto = numero.strip()
    for contacto in agenda:
        if texto in contacto["telefono"]:
            encontrados.append(contacto)
    return encontrados


def eliminar_contacto(agenda, nombre):
    """Elimina el primer contacto con ese nombre exacto.

    No distingue mayusculas ni espacios.
    Devuelve True si lo borra y False si no lo encuentra.
    """
    texto = nombre.strip().lower()
    for i in range(len(agenda)):
        if agenda[i]["nombre"].lower() == texto:
            del agenda[i]
            return True
    return False


def mostrar_contactos(agenda):
    """Muestra todos los contactos de la agenda por pantalla."""
    if len(agenda) == 0:
        print("La agenda esta vacia.")
        return
    print("\nContactos:")
    for contacto in agenda:
        print("- " + contacto["nombre"] + ": " + contacto["telefono"])


def mostrar_lista(contactos):
    """Muestra una lista de contactos (para resultados de busqueda)."""
    if len(contactos) == 0:
        print("No se han encontrado contactos.")
        return
    for contacto in contactos:
        print("- " + contacto["nombre"] + ": " + contacto["telefono"])


def guardar_contactos(agenda, ruta=RUTA_DATOS):
    """Guarda la agenda en un fichero de texto.

    Cada linea tiene el formato: nombre;telefono
    """
    with open(ruta, "w", encoding="utf-8") as fichero:
        for contacto in agenda:
            linea = contacto["nombre"] + SEPARADOR + contacto["telefono"] + "\n"
            fichero.write(linea)


def cargar_contactos(ruta=RUTA_DATOS):
    """Carga la agenda desde un fichero de texto.

    Si el fichero no existe, devuelve una lista vacia sin dar error.
    Las lineas mal formadas se ignoran.
    """
    agenda = []
    try:
        with open(ruta, "r", encoding="utf-8") as fichero:
            for linea in fichero:
                linea = linea.strip()
                if linea == "":
                    continue
                partes = linea.split(SEPARADOR)
                if len(partes) != 2:
                    continue
                nombre = partes[0].strip()
                telefono = partes[1].strip()
                if nombre == "" or telefono == "":
                    continue
                agenda.append(crear_contacto(nombre, telefono))
    except FileNotFoundError:
        agenda = []
    return agenda


def main():
    """Bucle principal: carga, muestra el menu, actua y guarda al salir."""
    agenda = cargar_contactos()

    seguir = True
    while seguir:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            nombre = pedir_nombre()
            telefono = pedir_telefono()
            if nombre == "" or telefono == "":
                print("El nombre y el telefono no pueden estar vacios.")
            else:
                contacto = crear_contacto(nombre, telefono)
                anadir_contacto(agenda, contacto)
                print("Contacto anadido.")
        elif opcion == "2":
            nombre = pedir_nombre()
            resultados = buscar_por_nombre(agenda, nombre)
            mostrar_lista(resultados)
        elif opcion == "3":
            numero = pedir_telefono()
            resultados = buscar_por_numero(agenda, numero)
            mostrar_lista(resultados)
        elif opcion == "4":
            nombre = pedir_nombre()
            if eliminar_contacto(agenda, nombre):
                print("Contacto eliminado.")
            else:
                print("No se ha encontrado ese contacto.")
        elif opcion == "5":
            mostrar_contactos(agenda)
        elif opcion == "0":
            guardar_contactos(agenda)
            print("Agenda guardada. Hasta pronto.")
            seguir = False
        else:
            print("Opcion no valida. Elige un numero del 0 al 5.")


if __name__ == "__main__":
    main()


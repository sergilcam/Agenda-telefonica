"""Pruebas de la agenda telefonica (version 2: Excel .xlsx y orden).

Cada prueba comprueba un comportamiento del programa.
Se ejecutan con: python -m pytest -q
"""

import openpyxl

from src.agenda import (
    anadir_contacto,
    buscar_por_nombre,
    buscar_por_numero,
    cargar_contactos,
    crear_contacto,
    eliminar_contacto,
    guardar_contactos,
    mostrar_contactos,
    ordenar_contactos,
)


def crear_agenda_ejemplo():
    """Crea una agenda pequena para usar en las pruebas."""
    agenda = []
    anadir_contacto(agenda, crear_contacto("Ana", "600111222"))
    anadir_contacto(agenda, crear_contacto("Beto", "600333444"))
    return agenda


def test_anadir_contacto():
    agenda = []
    anadir_contacto(agenda, crear_contacto("Ana", "600111222"))
    assert len(agenda) == 1
    assert agenda[0]["nombre"] == "Ana"
    assert agenda[0]["telefono"] == "600111222"


def test_buscar_por_nombre_encuentra():
    agenda = crear_agenda_ejemplo()
    resultados = buscar_por_nombre(agenda, "ana")
    assert len(resultados) == 1
    assert resultados[0]["telefono"] == "600111222"


def test_buscar_por_nombre_sin_resultado():
    agenda = crear_agenda_ejemplo()
    resultados = buscar_por_nombre(agenda, "Zoe")
    assert resultados == []


def test_buscar_por_numero_encuentra():
    agenda = crear_agenda_ejemplo()
    resultados = buscar_por_numero(agenda, "333")
    assert len(resultados) == 1
    assert resultados[0]["nombre"] == "Beto"


def test_buscar_por_numero_sin_resultado():
    agenda = crear_agenda_ejemplo()
    resultados = buscar_por_numero(agenda, "999")
    assert resultados == []


def test_eliminar_contacto_existente():
    agenda = crear_agenda_ejemplo()
    borrado = eliminar_contacto(agenda, "Ana")
    assert borrado is True
    assert len(agenda) == 1
    assert agenda[0]["nombre"] == "Beto"


def test_eliminar_contacto_inexistente():
    agenda = crear_agenda_ejemplo()
    borrado = eliminar_contacto(agenda, "Zoe")
    assert borrado is False
    assert len(agenda) == 2


def test_guardar_y_cargar(tmp_path):
    agenda = crear_agenda_ejemplo()
    ruta = tmp_path / "contactos.xlsx"
    guardar_contactos(agenda, str(ruta))
    cargada = cargar_contactos(str(ruta))
    assert cargada == agenda


def test_guardar_crea_dos_columnas_con_cabecera(tmp_path):
    agenda = crear_agenda_ejemplo()
    ruta = tmp_path / "contactos.xlsx"
    guardar_contactos(agenda, str(ruta))
    libro = openpyxl.load_workbook(str(ruta))
    hoja = libro["Contactos"]
    assert hoja["A1"].value == "nombre"
    assert hoja["B1"].value == "telefono"
    assert hoja["A2"].value == "Ana"
    assert str(hoja["B2"].value) == "600111222"


def test_cargar_sin_fichero(tmp_path):
    ruta = tmp_path / "no_existe.xlsx"
    agenda = cargar_contactos(str(ruta))
    assert agenda == []


def test_ordenar_ascendente():
    agenda = []
    anadir_contacto(agenda, crear_contacto("Zoe", "1"))
    anadir_contacto(agenda, crear_contacto("Ana", "2"))
    anadir_contacto(agenda, crear_contacto("Beto", "3"))
    ordenados = ordenar_contactos(agenda)
    nombres = [c["nombre"] for c in ordenados]
    assert nombres == ["Ana", "Beto", "Zoe"]


def test_ordenar_descendente():
    agenda = crear_agenda_ejemplo()
    anadir_contacto(agenda, crear_contacto("Zoe", "600999888"))
    ordenados = ordenar_contactos(agenda, descendente=True)
    nombres = [c["nombre"] for c in ordenados]
    assert nombres == ["Zoe", "Beto", "Ana"]


def test_ordenar_ignora_mayusculas():
    agenda = []
    anadir_contacto(agenda, crear_contacto("beto", "1"))
    anadir_contacto(agenda, crear_contacto("Ana", "2"))
    anadir_contacto(agenda, crear_contacto("CARLOS", "3"))
    ordenados = ordenar_contactos(agenda)
    nombres = [c["nombre"] for c in ordenados]
    assert [n.lower() for n in nombres] == ["ana", "beto", "carlos"]


def test_mostrar_agenda_vacia_no_falla(capsys):
    mostrar_contactos([])
    texto = capsys.readouterr().out
    assert "vacia" in texto.lower()


def test_mostrar_contactos_ordenados(capsys):
    agenda = []
    anadir_contacto(agenda, crear_contacto("Zoe", "1"))
    anadir_contacto(agenda, crear_contacto("Ana", "2"))
    mostrar_contactos(agenda, descendente=False)
    texto = capsys.readouterr().out
    assert texto.index("Ana") < texto.index("Zoe")
    mostrar_contactos(agenda, descendente=True)
    texto = capsys.readouterr().out
    assert texto.index("Zoe") < texto.index("Ana")

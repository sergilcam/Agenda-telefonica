 # Historial de cambios

## [Sin publicar]
### Añadido
- Estructura inicial del proyecto.
- Documentación de contexto y continuidad.
- Versión 1 de la agenda: `src/agenda.py` con menú, añadir,
  buscar por nombre y número, eliminar, mostrar, guardar y
  cargar en `data/contactos.txt` (formato `nombre;telefono`).
- Pruebas en `tests/test_agenda.py` (10 pruebas con pytest).

## [Sin publicar] - Versión 2: hoja de cálculo y orden
### Añadido
- Guardado y carga en `data/contactos.xlsx` (hoja `Contactos`,
  columnas `nombre | telefono`) con `openpyxl`.
- Orden alfabético al mostrar todos: `ordenar_contactos`,
  `pedir_orden` y opción 5 con A-Z / Z-A.
- Dependencia `openpyxl` en `requeriments.txt`.
- 5 pruebas nuevas en `tests/test_agenda.py` (15 en total).

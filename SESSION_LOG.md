 # Diario de sesiones

## Sesión 1 - 2026-10-02
### Objetivo
Preparar la estructura y la memoria del proyecto.

### Realizado
- Creadas las carpetas y plantillas iniciales.

### Comprobaciones
- Ninguna hasta la fecha.

### Pendiente
- Inicializar Git y crear el plan de la versión 1.

### Primer paso de la próxima sesión
Lee README.md, AGENTS.md, TODO.md, SESSION_LOG.md y CHANGELOG.md.; después solicitar un plan sin programar.

## Sesión 2 - 2026-10-07
### Objetivo
Implementar la versión 1 aprobada en el plan.

### Realizado
- Creado `src/agenda.py` con funciones pequeñas y menú de consola.
- Creadas 10 pruebas en `tests/test_agenda.py`.
- Actualizados `TODO.md` y `CHANGELOG.md`.

### Comprobaciones
- Prueba manual de `python -m src.agenda`: añadir, mostrar,
  buscar por nombre y número, eliminar y guardar. Todo correcto.
- Batería de comprobaciones con `python3 -c` (sin pytest):
  8 grupos de asserts, todos OK.
- Pendiente `python -m pytest -q`: no hay pip ni pytest en el equipo.

### Pendiente
- Instalar pip/pytest y ejecutar la suite.
- Commit inicial y commit de la v1 en Git.

## Sesión 3 - 2026-10-14
### Objetivo
Guardar en hoja de cálculo `.xlsx` y mostrar ordenado A-Z / Z-A.

### Realizado
- Instalado pip para usuario y `openpyxl` + `pytest`.
- Añadida dependencia `openpyxl` en `requeriments.txt`.
- `src/agenda.py`: `guardar_contactos`/`cargar_contactos` con
  hoja `Contactos` (columnas `nombre | telefono`, teléfono como texto);
  nuevas `ordenar_contactos` y `pedir_orden`; opción 5 pregunta A-Z/Z-A.
- `tests/test_agenda.py`: 15 pruebas (cabecera y 2 columnas, A-Z, Z-A,
  mayúsculas, mostrar ordenado).
- Migrados `pepe` y `juan` de `data/contactos.txt` a `data/contactos.xlsx`.
- Actualizados `README.md`, `CHANGELOG.md` y `TODO.md`.

### Comprobaciones
- `python3 -m py_compile src/agenda.py`: OK.
- `python -m pytest -q`: 15 passed.
- Excel verificado: hoja `Contactos`, A1=nombre, B1=telefono,
  B2 como texto `654321789`, 3 filas.
- Menú opción 5 con `1`: muestra `juan` antes que `pepe` (A-Z).
- Menú opción 5 con `2`: muestra `pepe` antes que `juan` (Z-A).

### Pendiente
- Commit de la v2 en Git.

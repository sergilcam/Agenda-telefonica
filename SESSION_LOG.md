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

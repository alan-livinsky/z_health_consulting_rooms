z_health_consulting_rooms
=========================

Módulo GNU Health HMIS — FIUNER
--------------------------------

**Versión:** 4.2.0
**Framework:** Tryton (GNU Health HMIS)
**Licencia:** GPL-3
**Python:** >= 3.10, < 3.11

Descripción
-----------

Módulo de administración de consultorios para el sistema GNU Health HMIS,
desarrollado para la FIUNER (Facultad de Ingeniería, Universidad Nacional
de Entre Ríos).

Agrega un ítem de menú bajo la sección de **Turnos** (Appointments) para
gestionar los consultorios definidos por el módulo
``health_appointment_screen_fiuner``. No define modelos propios; actúa
como capa de interfaz sobre el modelo ``gnuhealth.consulting_room``
existente.

Funcionalidad
-------------

- **Menú Consultorios:** accesible desde *Salud → Turnos → Consultorios*.
- **Vista árbol (lista):** muestra todos los consultorios con su nombre.
- **Vista formulario:** permite ver y editar el nombre de cada consultorio.

Estructura del módulo
---------------------

::

    z_health_consulting_rooms/
    ├── __init__.py                              # Registro del módulo (vacío)
    ├── consultorios.xml                         # Menú, acción y definiciones de vistas
    ├── view/
    │   ├── gnuhealth_consulting_room_form.xml   # Vista formulario
    │   └── gnuhealth_consulting_room_tree.xml   # Vista árbol/lista
    ├── tryton.cfg                               # Metadatos del módulo Tryton
    ├── setup.py                                 # Configuración de instalación
    ├── pyproject.toml                           # Backend de construcción (PEP 517)
    └── MANIFEST.in                              # Manifiesto del paquete

Dependencias
------------

- ``health`` — módulo base de GNU Health
- ``health_appointment_fiuner`` — gestión de turnos FIUNER
- ``health_appointment_screen_fiuner`` — pantalla de turnos FIUNER (define el modelo ``gnuhealth.consulting_room``)

Modelo de datos
---------------

El módulo referencia el modelo ``gnuhealth.consulting_room``, definido en
``health_appointment_screen_fiuner``. Dicho modelo expone un único campo:

============  =============  ==========================================
Campo         Tipo           Descripción
============  =============  ==========================================
``name``      Char           Nombre o identificador del consultorio
============  =============  ==========================================

Los turnos del sistema utilizan este modelo a través del campo
``consulting_room`` (Many2One) en ``AppointmentData``, vinculando cada
turno a un consultorio específico.

Instalación
-----------

1. Copiar el directorio ``z_health_consulting_rooms`` dentro de
   ``trytond/modules/``.
2. Instalar el paquete Python::

       pip install -e .

3. Actualizar la base de datos desde el cliente Tryton o con::

       trytond-admin -d <base_de_datos> --all

Seguridad
---------

No define reglas de acceso propias. Hereda el modelo de permisos de
Tryton y de los módulos ``health`` padre.

Integración
-----------

Este módulo forma parte de una implementación específica FIUNER del
sistema GNU Health HMIS. El flujo típico es:

1. El administrador define los consultorios disponibles desde el menú
   *Consultorios*.
2. Al registrar un turno con pantalla de atención (``health_appointment_screen_fiuner``),
   se asigna el consultorio correspondiente al turno.

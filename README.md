# Proyecto Crowdfunding Morelia (Backend Django + Frontend Vue.js)

Plataforma de crowdfunding para promover el desarrollo económico en el municipio de Morelia, permitiendo el financiamiento de proyectos municipales, PYMES, MIPYMES, personas físicas y la ciudadanía en general.

## Descripción General

El sistema permite a los usuarios (identificados con un "ID Morelia") registrarse, presentar "casos" (proyectos o necesidades), y buscar financiamiento. Otros usuarios pueden ver estos casos, interactuar con ellos y, eventualmente, realizar aportaciones (el mecanismo de aportación directa se maneja con confirmación manual y evidencia). El municipio también puede publicar programas y asignar fondos.

**Tecnologías Principales:**
*   **Backend:** Python con Django Framework.
*   **Frontend:** Vue.js (estructura básica creada).
*   **Base de Datos:** PostgreSQL.

## Estructura del Proyecto

```
proyecto_crowdfunding/      # Directorio raíz del proyecto Django
├── config_django/          # Configuración del proyecto Django (settings.py, urls.py, etc.)
├── nucleo_crowdfunding/    # Aplicación Django principal para la lógica del crowdfunding
│   ├── migrations/
│   ├── models.py           # Modelos de la base de datos
│   ├── views.py            # Lógica de las vistas/API endpoints
│   ├── urls.py             # URLs específicas de la app
│   ├── tests.py            # Pruebas de la app
│   └── ...
├── frontend/               # Directorio para la aplicación Vue.js
│   ├── publico/
│   │   └── index.html      # HTML principal para la SPA de Vue
│   ├── src/
│   │   ├── componentes/    # Componentes Vue reutilizables
│   │   ├── vistas/         # Componentes Vue para las páginas/rutas
│   │   ├── App.vue         # Componente raíz de Vue
│   │   ├── main.js         # Punto de entrada de la app Vue (simulado)
│   │   └── router.js       # Definiciones de rutas de Vue (simulado)
│   └── ...
├── mediafiles/             # (Se creará por Django) Directorio para archivos subidos por usuarios (MEDIA_ROOT)
└── manage.py               # Utilidad de línea de comandos de Django
```

## Configuración del Backend (Django)

### Prerrequisitos
*   Python 3.8+
*   pip (manejador de paquetes de Python)
*   PostgreSQL (servidor de base de datos)

### Pasos de Configuración (Desarrollo Local)

1.  **Clonar el Repositorio (si aplica):**
    ```bash
    # git clone <url-del-repositorio>
    # cd <directorio-del-proyecto>
    ```

2.  **Crear y Activar un Entorno Virtual:**
    Asegúrate de estar en el directorio raíz del proyecto (el que contendrá `proyecto_crowdfunding` y este README).
    ```bash
    python -m venv venv
    # En Windows:
    # venv\Scripts\activate
    # En macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Instalar Dependencias de Python:**
    Navega al directorio `proyecto_crowdfunding` (donde está `manage.py`).
    ```bash
    pip install django psycopg2-binary Pillow
    ```
    *(En un proyecto compartido, estas estarían en un archivo `requirements.txt`. Puedes generar uno con `pip freeze > requirements.txt`)*

4.  **Configurar la Base de Datos PostgreSQL:**
    *   Asegúrate que PostgreSQL está instalado y corriendo.
    *   Crea una base de datos para el proyecto, ej: `morelia_crowdfunding_db`.
    *   Crea un usuario de base de datos con permisos para acceder a esta base de datos.
    *   Actualiza la configuración `DATABASES` en `proyecto_crowdfunding/config_django/settings.py` con tus credenciales de PostgreSQL:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'tu_nombre_de_bd',    # Ej: morelia_crowdfunding_db
                'USER': 'tu_usuario_de_bd',
                'PASSWORD': 'tu_contraseña_de_bd',
                'HOST': 'localhost',      # O la IP/host de tu servidor de BD
                'PORT': '5432',           # Puerto por defecto de PostgreSQL
            }
        }
        ```

5.  **Aplicar Migraciones de la Base de Datos:**
    Desde el directorio `proyecto_crowdfunding` (donde está `manage.py`):
    ```bash
    python manage.py makemigrations nucleo_crowdfunding
    python manage.py migrate
    ```

6.  **Crear un Superusuario (Opcional, para el Admin de Django):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Ejecutar el Servidor de Desarrollo de Django:**
    ```bash
    python manage.py runserver
    ```
    El backend estará disponible usualmente en `http://127.0.0.1:8000/`.
    Los endpoints de la API estarán bajo `http://127.0.0.1:8000/api/v1/crowdfunding/`.

## Configuración del Frontend (Vue.js) - Conceptual

La estructura básica de Vue.js ha sido creada en `proyecto_crowdfunding/frontend/`. Para un desarrollo completo:

1.  **Prerrequisitos:**
    *   Node.js y npm (o yarn).

2.  **Instalar Dependencias del Frontend:**
    Navega al directorio `proyecto_crowdfunding/frontend/`. Si hubiera un `package.json`:
    ```bash
    # npm install
    # o
    # yarn install
    ```
    *(Esto requeriría un archivo `package.json` con dependencias como `vue`, `vue-router`. Para este proyecto, los archivos Vue se han creado manualmente.)*

3.  **Ejecutar el Servidor de Desarrollo de Vue (si se usa Vue CLI):**
    Si se estructura como un proyecto Vue CLI:
    ```bash
    # npm run serve
    # o
    # yarn serve
    ```
    El frontend estaría disponible usualmente en `http://localhost:8080/` (o el puerto que configure Vue CLI).
    Se necesitaría configurar un proxy en `vue.config.js` para redirigir las llamadas a API (ej. `/api/v1/`) al backend de Django que corre en el puerto 8000, para evitar problemas de CORS durante el desarrollo.
    Alternativamente, abrir `proyecto_crowdfunding/frontend/publico/index.html` directamente en un navegador podría mostrar la estructura básica, pero sin el enrutamiento completo ni el servidor de desarrollo de Vue.

## API Endpoints Principales (Backend)

Los endpoints están definidos en `proyecto_crowdfunding/nucleo_crowdfunding/urls.py` y la lógica en `views.py`.

*   `POST /api/v1/crowdfunding/usuarios/registrar/`
    *   Registra un nuevo usuario.
    *   **Request Body (JSON):** `{ "id_morelia": "...", "email": "...", "password": "...", "first_name": "...", "last_name": "...", "usuario_tipo_id": (opcional), "nivel_id": (opcional) }`
    *   **Response (201 Created):** `{ "mensaje": "...", "usuario": { ... } }`
    *   **Response (400 Bad Request):** `{ "error": "..." }`
*   `POST /api/v1/crowdfunding/usuarios/login/`
    *   Inicia sesión.
    *   **Request Body (JSON):** `{ "id_morelia_o_email": "...", "password": "..." }`
    *   **Response (200 OK):** `{ "mensaje": "...", "usuario": { ... } }` (Gestión de sesión/token no implementada)
    *   **Response (400/401/403):** `{ "error": "..." }`
*   `GET /api/v1/crowdfunding/casos/`
    *   Lista todos los casos de crowdfunding.
    *   **Response (200 OK):** `[ { ...datos_del_caso... }, ... ]`
*   `POST /api/v1/crowdfunding/casos/crear/`
    *   Crea un nuevo caso. Requiere autenticación (conceptual).
    *   **Request Body (Multipart/form-data):** Campos de texto (`creador_id_morelia` (temporal), `exposicion_titulo`, etc.) y archivos opcionales (`imagen_promocional`, `video_promocional`).
    *   **Response (201 Created):** `{ "mensaje": "...", "caso_id": ... }`
*   `GET /api/v1/crowdfunding/casos/<int:caso_id>/`
    *   Obtiene detalles de un caso específico.
    *   **Response (200 OK):** `{ ...datos_completos_del_caso... }`
    *   **Response (404 Not Found):** `{ "error": "Caso no encontrado." }`
*   `PUT/PATCH /api/v1/crowdfunding/casos/<int:caso_id>/actualizar/`
    *   Actualiza un caso existente. Requiere autenticación y permisos (conceptual).
    *   **Request Body (JSON o Multipart/form-data):** Campos a actualizar.
    *   **Response (200 OK):** `{ "mensaje": "...", "caso_id": ... }`
*   `DELETE /api/v1/crowdfunding/casos/<int:caso_id>/eliminar/`
    *   Elimina un caso. Requiere autenticación y permisos (conceptual).
    *   **Response (200 OK or 204 No Content):** `{ "mensaje": "..." }`

## Pruebas

*   **Backend:** Desde el directorio `proyecto_crowdfunding/`, ejecutar:
    ```bash
    python manage.py test nucleo_crowdfunding
    ```
    (Requiere que la base de datos configurada en `settings.py` sea accesible, o Django usará una base de datos de prueba en memoria si es SQLite, o intentará crear una BD de prueba para PostgreSQL si el usuario tiene permisos).
*   **Frontend:** (Conceptual) Las pruebas de componentes Vue se escribirían usando herramientas como Vue Test Utils con Jest o Vitest.

## Despliegue

Consultar la documentación conceptual de despliegue para estrategias. Implica:
*   Configurar un servidor WSGI (Gunicorn) para Django.
*   Construir la aplicación Vue (`npm run build`) y servir sus archivos estáticos.
*   Configurar un servidor de base de datos PostgreSQL de producción.
*   Usar un servidor web como Nginx como reverse proxy, para servir archivos estáticos/media y gestionar HTTPS.
---

Este README provee una guía básica. Detalles adicionales se pueden encontrar en comentarios dentro del código.

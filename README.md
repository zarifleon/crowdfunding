# Morelia Crowdfunding Platform (Backend Django + Frontend Vue.js)

A crowdfunding platform to promote economic development in the municipality of Morelia, enabling funding for municipal projects, SMEs, MSMEs, individuals, and the general citizenry.

## Overview

The system allows users (identified with an "ID Morelia") to register, submit "cases" (projects or needs), and seek funding. Other users can view these cases, interact with them, and make contributions (direct contributions are handled with manual confirmation and evidence). The municipality can also publish programs and allocate funds.

**Core Technologies:**
*   **Backend:** Python with Django Framework.
*   **Frontend:** Vue.js (basic structure created).
*   **Database:** PostgreSQL.

## Project Structure

The root directory for all project code related to this specific application is `proyecto_crowdfunding/`.

```
proyecto_crowdfunding/      # Main application directory
├── django_config/          # Django project configuration (settings.py, urls.py, etc.)
├── crowdfunding_core/      # Main Django app for crowdfunding logic
│   ├── migrations/
│   ├── models.py           # Database models (Spanish field names maintained)
│   ├── views.py            # View logic / API endpoints
│   ├── urls.py             # App-specific URLs
│   ├── tests.py            # App tests
│   └── ...
├── frontend/               # Directory for the Vue.js application
│   ├── public/             # Public assets for Vue (e.g., index.html)
│   │   └── index.html      # Main HTML for the Vue SPA
│   ├── src/
│   │   ├── components/     # Reusable Vue components (e.g., CaseCard.vue)
│   │   ├── views/          # Vue components for pages/routes (e.g., HomePage.vue)
│   │   ├── App.vue         # Root Vue component
│   │   ├── main.js         # Vue app entry point (simulated)
│   │   └── router.js       # Vue route definitions (simulated)
│   └── ...
├── mediafiles/             # (Will be created by Django) Directory for user-uploaded files (MEDIA_ROOT)
└── manage.py               # Django command-line utility
```

## Backend Setup (Django)

### Prerequisites
*   Python 3.8+
*   pip (Python package manager)
*   PostgreSQL (database server)

### Local Development Setup Steps

1.  **Clone Repository (if applicable):**
    ```bash
    # git clone <repository-url>
    # cd <project-root-directory>
    ```

2.  **Create and Activate a Virtual Environment:**
    (Assuming you are in the directory that *contains* `proyecto_crowdfunding`)
    ```bash
    python -m venv venv
    # Windows:
    # venv\Scripts\activate
    # macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install Python Dependencies:**
    Navigate into the `proyecto_crowdfunding` directory (where `manage.py` is located).
    ```bash
    pip install django psycopg2-binary Pillow
    ```
    *(In a shared project, these would be in a `requirements.txt` file. You can generate one using `pip freeze > requirements.txt`)*

4.  **Configure PostgreSQL Database:**
    *   Ensure PostgreSQL is installed and running.
    *   Create a database for the project (e.g., `morelia_crowdfunding_db`).
    *   Create a database user with permissions for this database.
    *   Update the `DATABASES` setting in `proyecto_crowdfunding/django_config/settings.py` with your PostgreSQL credentials:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_db_name',    # e.g., morelia_crowdfunding_db
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost',      # Or your DB server host/IP
                'PORT': '5432',           # Default PostgreSQL port
            }
        }
        ```

5.  **Apply Database Migrations:**
    From the `proyecto_crowdfunding` directory:
    ```bash
    python manage.py makemigrations crowdfunding_core
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional, for Django Admin):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Django Development Server:**
    ```bash
    python manage.py runserver
    ```
    The backend will typically be available at `http://127.0.0.1:8000/`.
    API endpoints will be under `http://127.0.0.1:8000/api/v1/crowdfunding/`.

## Frontend Setup (Vue.js) - Conceptual

The basic Vue.js structure is in `proyecto_crowdfunding/frontend/`. For full development:

1.  **Prerequisites:**
    *   Node.js and npm (or yarn).

2.  **Install Frontend Dependencies:**
    Navigate to `proyecto_crowdfunding/frontend/`. If a `package.json` existed:
    ```bash
    # npm install
    # or
    # yarn install
    ```
    *(This project's Vue files were created manually. A `package.json` with dependencies like `vue` and `vue-router` would be needed for a typical Vue CLI setup.)*

3.  **Run Vue Development Server (if using Vue CLI):**
    If structured as a Vue CLI project:
    ```bash
    # npm run serve
    # or
    # yarn serve
    ```
    The frontend would typically be at `http://localhost:8080/`.
    A proxy would need to be configured in `vue.config.js` to redirect API calls (e.g., to `/api/v1/`) to the Django backend (running on port 8000) to avoid CORS issues during development.
    Alternatively, opening `proyecto_crowdfunding/frontend/public/index.html` directly in a browser might show the basic structure but without full routing or Vue's dev server capabilities.

## Main API Endpoints (Backend)

Defined in `proyecto_crowdfunding/crowdfunding_core/urls.py` and logic in `views.py`.
User-facing URL segments like `usuarios` and `casos` remain in Spanish.

*   `POST /api/v1/crowdfunding/usuarios/registrar/` - Register a new user.
*   `POST /api/v1/crowdfunding/usuarios/login/` - User login.
*   `GET /api/v1/crowdfunding/casos/` - List all crowdfunding cases.
*   `POST /api/v1/crowdfunding/casos/crear/` - Create a new case.
*   `GET /api/v1/crowdfunding/casos/<int:caso_id>/` - Get details of a specific case.
*   `PUT/PATCH /api/v1/crowdfunding/casos/<int:caso_id>/actualizar/` - Update an existing case.
*   `DELETE /api/v1/crowdfunding/casos/<int:caso_id>/eliminar/` - Delete a case.

*(Refer to the source code or more detailed API documentation for request/response formats.)*

## Testing

*   **Backend:** From the `proyecto_crowdfunding/` directory, run:
    ```bash
    python manage.py test crowdfunding_core
    ```
    (Requires the database in `settings.py` to be accessible or for Django to be able to create a test database.)
*   **Frontend:** (Conceptual) Vue component tests would be written using tools like Vue Test Utils with Jest or Vitest.

## Deployment

Refer to conceptual deployment documentation. Involves setting up a WSGI server for Django, building and serving Vue static assets, a production PostgreSQL database, and a web server like Nginx.
---

This README provides a basic guide. More details can be found in code comments.

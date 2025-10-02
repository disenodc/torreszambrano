TuPrimeraPaginaDiaz
Blog básico en Django con MVT
Estructura del proyecto
mi_blog/
├── manage.py
├── mi_blog/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── migrations/
└── templates/
    ├── base.html
    ├── index.html
    ├── crear_post.html
    ├── crear_autor.html
    ├── crear_categoria.html
    └── buscar.html
Instalación y uso

Crear entorno virtual:

bashpython -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

Instalar Django:

bashpip install django

Crear proyecto:

bashdjango-admin startproject mi_blog
cd mi_blog
python manage.py startapp blog

Copiar archivos del código
Hacer migraciones:

bashpython manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Ejecutar servidor:

bashpython manage.py runserver
Funcionalidades

Página principal: Lista todos los posts del blog
Crear Post: Formulario para agregar nuevos posts
Crear Autor: Formulario para agregar autores
Crear Categoría: Formulario para agregar categorías
Buscar: Busca posts por título

Orden de prueba

Ir a http://127.0.0.1:8000/
Crear una categoría primero
Crear un autor
Crear un post
Probar la búsqueda
Ver la página principal con los posts

URLs disponibles

/ - Página principal
/crear_post/ - Crear nuevo post
/crear_autor/ - Crear nuevo autor
/crear_categoria/ - Crear nueva categoría
/buscar/ - Buscar posts

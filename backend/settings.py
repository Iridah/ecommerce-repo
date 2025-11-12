"""
settings.py para Mi Portafolio E-Commerce.
"""
import os
from pathlib import Path

# Construye rutas dentro del proyecto como: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================
# CONFIGURACIÓN DE SEGURIDAD
# =======================================================
# ATENCIÓN: Esta clave DEBE ser cambiada y mantenida en secreto en producción.
SECRET_KEY = 'tu_clave_secreta_aqui_para_desarrollo'

DEBUG = True # Mantener en True durante el desarrollo.

ALLOWED_HOSTS = []


# =======================================================
# APLICACIONES INSTALADAS
# =======================================================
INSTALLED_APPS = [
    # Las apps de Django por defecto (las de arriba)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aquí irán tus aplicaciones propias (ej. 'tienda' o 'productos')
]

MIDDLEWARE = [
    # ... (Middleware por defecto de Django)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls' # Apunta al archivo urls.py que crearemos

# =======================================================
# CONFIGURACIÓN DE PLANTILLAS (TEMPLATES)
# =======================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 1. Le dice a Django dónde buscar la carpeta 'templates'
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Agregado para que la función 'static' funcione en las plantillas
                'django.template.context_processors.static', 
            ],
        },
    },
]

# ... (Otros ajustes de Django: WSGI, Base de Datos, etc.)

# =======================================================
# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (STATIC FILES)
# =======================================================

# 1. La URL base que usará el navegador para acceder a estáticos (ej: /static/css/styles.css)
STATIC_URL = 'static/' 

# 2. Le dice a Django dónde buscar la carpeta 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]

# 3. Directorio para recoger estáticos en producción (importante para el deploy)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# =======================================================
# AJUSTES DE IDIOMA Y ZONA HORARIA
# =======================================================
LANGUAGE_CODE = 'es-cl' # Usaremos el código de Chile, como lo definiste en el HTML.
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True
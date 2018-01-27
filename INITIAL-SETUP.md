# Iniciar el proyecto

- Creamos un nuevo directorio del proyecto y accedemos al directorio creado

```sh
mkdir rest-api-basics & cd rest-api-basics
```

- creamos un nuevo entorno virtual con `python3` 

> **Nota:**  el entorno virtual se crea en la carpeta llamada *venv* por que así se lo indicamos.

> **Nota 2:**  el path a *python3* variará dependiendo la ubicación donde lo tengas.

```sh
# en Windows
virtualenv -p c:\Python3\python.exe venv

# en Linux
virtualenv -p python3 venv
```

- Activamos el entorno virtual para instalar los requerimientos del proyecto.

```sh
# en Windows
venv\Scripts\activate

# en Linux
source venv\bin\activate
```

- Instalamos los requerimientos del proyecto

```sh
pip install django==1.11.9 djangorestframework==3.7.7 djangorestframework-jwt==1.11.0
```

- Creamos el archivo `requirements.txt`

```sh
pip freeze > requirements.txt
```

- creamos la carpeta `src` donde irá el código de nuestro proyecto y accedemos a ella

```sh
mkdir src & cd src
```

- creamos nuestro nuevo proyecto de django en la carpera `src`
> **Nota:** el `.` al final es para indicarle que queremos que no cree una nueva carpeta si no que ponga todo en la carpeta raíz directamente

```sh
django-admin startproject apibasics .
```

- creamos nuestra app `postings`

```sh
django-admin startapp postings
```

- Agregamos las apps de `rest_frameworks` y `postings` a `INSTALLED_APPS` de nuestro `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    ...,
    'django.contrib.staticfiles',
    ### third apps
    'rest_framework',
    ### my apps
    'postings',
]
```

- Agregamos las configuraciones de `django rest framework` al final nuestro `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```

- Reemplazamos en `models.py` de `postings` con esto.

```python
from django.conf import settings
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=120, null=True, blank=True)
    content     = models.CharField(max_length=120, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
```

- Agregamos a `admin.py` de `postings` nuestro modelo para poder usarlo desde el admin de django.

```python
from .models import BlogPost

admin.site.register(BlogPost)
```

- Creamos los migrations, las aplicamos y creamos un super usuario.
> Ejecutamos linea por linea y en el `createsuperuser` llenamos la información que solicita

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**Listo el proyecto está en su fase inicial**

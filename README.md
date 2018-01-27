# REST API BASICS

### Cómo correr el proyecto 

- Clonamos el repositorio

```sh
git clone https://github.com/Cuahutli/rest-api-basics.git
```

- Accedemos a la carpeta creada

```sh
cd rest-api-basics
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
pip install -r requirements.txt
```

- Accedemos a la carpeta `src`

```sh
cd src
``` 

- Creamos la Base de Datos

```sh
python manage.py migrate
```

- Creamos un super usuario

```
python manage.py createsuperuser
```

- Corremos nuestro proyecto

```sh
python manage.py runserver
```

**A Disfrutar!!**
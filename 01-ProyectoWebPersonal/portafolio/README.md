#### Creacion de entornor virtuales

```
pip3 install pipenv
```

### Crear el entornor virtual

```
pipenv --python 3.8
```

pipenv --rm

### Instlar django y el resto de paquetes

pipenv isntall django django-ckeditor Pillow pylint pylint-django

### Para arrancar el servidor

pipenv run django-admin startproject nombr_proyecto

### Activar el entorno virtual

pipenv shell

### para correr el servidor

python manage.py runserver

--otra forma debe estar en curso django
pipenv run portafolio

#### Desarrollo del portafolio web inicio

### Creacion del core

```
python manage.py startapp core
```

### para crear los templates django

1.  se crea un directorio templates
2.  se crea un directorio con el nombre de la app
3.  en settings agrego el nombre del INSTALLED_APP

#### Parte para ahjcer dinamico la web

### Paquete para manipular iamgenes

pip install Pillow

#### Se crear otra app para las base de datos

python manage.py startapp portfolio

#### Crear las migraciones de las app creadas

python manage.py makemigrations portfolio

python manage.py migrate portfolio

### Crear un super usuario para el panel admin

python manage.py createsuperuser

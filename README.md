Comic Reader Online
====================


Proyecto experimental por el Hackerspace Monterrey
-------------------


### Como probar esto en desarrollo

(Opcional) Crear un entorno virtual, recomiendo usar [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.org/en/latest/).

Instalar las librerías necesarias `pip install -r requirements.txt`. Algunas librerías de python necesitan librerías de C/C++ así como de un compilador. Dichas librerías son:

  * [Pillow](http://pillow.readthedocs.org/installation.html#linux-installation)
  * (Opcional) [Psycopg2](http://initd.org/psycopg/docs/install.html#requirements)

Configurar las variables de entorno especificadas en `conf/env_var.sh`

  * `DATABASE_URL` puedes ver el [url schema aquí](https://github.com/kennethreitz/dj-database-url#url-schema)
  * `SECRET_KEY` una llave aleatoria

Una vez instalado todo puedes correr el servidor web con el comando

`python manage.py runserver`

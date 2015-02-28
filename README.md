Comic Reader Online
-------------------


Proyecto experimental por el Hackerspace Monterrey
====================


### Como probar esto en desarrollo

* (Opcional) Crear un entorno virtual
* Instalar las librerias necesarias `pip install -r requirements.txt`
    * Algunas librerias necesitan librerias de C/C++ así como un compilador.
    * (Pillow)[http://pillow.readthedocs.org/installation.html#linux-installation]
    * (Opcional) (Psycopg2)[http://initd.org/psycopg/docs/install.html#requirements]
* Configurar las variables de entorno especificadas en `conf/env_var.sh`
    * `DATABASE_URL` puedes ver el (url schema aqui)[https://github.com/kennethreitz/dj-database-url#url-schema]
* Una vez instalado todo puedes correr el servidor web con el comando `python manage.py runserver`

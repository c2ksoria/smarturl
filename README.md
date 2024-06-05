Este programa es un intento de hacer un software para utilizar para publicidad.

Básicamente permite crear campañas de publicidad para utilizar en pantallas con navegadores web.

Se elige primero el tipo de Paquete Contratado, que es el que define la cantidad de campañas diferentes (Campañas Disponibles) y la cantidad de Fotos Disponibles.
Luego accediendo al menú de campaña (/campana) se pueden crear nuevas campañas y ver el listado de las campanas actuales.
Desde esta misma pantalla (/campana) se accede listado de cada nueva campaña, y se pueden ejecutar acciones (CRUD) y copiar el link de enlace

Deploy:

petry shell
python manage.py runserver
or
python manage.py runserver 0.0.0.0:8000


ingresar desde:
127.0.0.1:8000/login

Verificar funcionamiento de puerto de escucha:
netstat -tulpn | grep LISTEN

Apertura de puerto 8000:
- sudo ufw allow 8000

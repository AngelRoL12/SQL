# SQL
This is my first proyect with GITHUB where i'll do a project with DJANGO and SQL.

Primero generas la clase o el modelo para realizar las migraciones a la base de datos en el archivo 'models.py', una vez hecho eso
ejecutar:
python manage.py makemigrations
Esto creará un documento que permitirá a Django hacer las migraciones de acuerdo a la estructura del modelo en 'models.py'.

Para realizar la migración:
python manage.py migrate

Forma de insertar datos a las tablas:
from flights.models import Flight
>>> f = Flight(origin='New York', destination='London', duration=415)
>>> f.save()
# SQL
This is my first proyect with GITHUB where i'll do a project with DJANGO and SQL.

Primero generas la clase o el modelo para realizar las migraciones a la base de datos en el archivo 'models.py', una vez hecho eso
ejecutar:

python manage.py makemigrations
Esto creará un documento que permitirá a Django hacer las migraciones de acuerdo a la estructura del modelo en 'models.py'.
Actualizar los cambios que se hayan hecho en 'models.py' para actualizar la base de datos.

Para realizar la migración:
python manage.py migrate
Realiza los cambios

Todo lo siguiente es desde SHELL DE PYTHON
Forma de insertar datos a las tablas:   
from flights.models import Flight

>>> f = Flight(origin='New York', destination='London', duration=415)
>>> f.save()
>>> Flight.objects.all()        Para poder acceder a todos los datos.
>>> Flight.objects.filter(origin='New York')            Para filtrar los datos
>>> Flight.objects.filter(origin='New York').first()    Para filtrar el primer valor
>>> Flight.objects.GET(origin='New York')               Si se sabe que solo te arrojara un valor

Foreign Keys: (Hace referencia a otras tablas)
models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="Departures")

on_delete=models.CASCADE -> para eliminar la fila en caso de que se elimine en la base de datos el objeto referenciado
          models.PROTECT -> para restringir eliminar en la base de datos si se esta utilizado en la tabla relacionada


sqlite3 db.sqlite3  ---> Para poder acceder a la base de datos.
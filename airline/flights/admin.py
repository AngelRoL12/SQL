from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")         #Quiero ver todo esto cuando cargas un vuelo

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)                                   #A la izquierda se muestran los vuelos disponibles, a la derecha los registrados 

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)

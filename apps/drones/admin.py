from django.contrib import admin

from .models import Drone, Medication

class DroneAdmin(admin.ModelAdmin):
    pass

class MedicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Drone)
admin.site.register(Medication)
# Register your models here.

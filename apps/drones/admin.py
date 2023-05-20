from django.contrib import admin

from .models import Drone, Medication, LogBattery

class DroneAdmin(admin.ModelAdmin):
    pass

class MedicationAdmin(admin.ModelAdmin):
    pass

class LogBatteryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Drone)
admin.site.register(Medication)
admin.site.register(LogBattery)
# Register your models here.

from django.contrib import admin

from .models import Drone

class DroneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Drone)
# Register your models here.

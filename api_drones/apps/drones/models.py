from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from  decimal import Decimal


class Medication(models.Model):
    name_validator = RegexValidator(r'^[A-Za-z0-9_-]*$', 'Allowed only letters, numbers, - and _')
    code_validator = RegexValidator(r'^[A-Z0-9_]*$', 'Allowed only upper case letters, underscore and numbers')
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    weight = models.IntegerField(default=1, blank=False, null=False)
    code = models.CharField(max_length=150, validators=[code_validator], blank=False)
    image = models.ImageField('PictureCase', upload_to='picturecase/', blank=True, null=True)
    

    class Meta:

        verbose_name_plural = "Medicationes"

    def __str__(self):
        return self.name

class Drone(models.Model):
    class DroneModelChoices(models.TextChoices):
        LIGHTWEIGHT = 'Lightweight', 'Lightweight'
        MIDDLEWEIGHT = 'Middleweight', 'Middleweight'
        CRUISERWRIGHT = 'Cruiserweight', 'Cruiserweight'
        HEAVYWEIGHT = 'Heavyweight', 'Heavyweight'
    
    class DroneStatusChoices(models.TextChoices):
        IDLE = 'IDLE', 'IDLE'
        LOADING = 'LOADING', 'LOADING'
        LOADED = 'LOADED', 'LOADED'
        DELIVERING = 'DELIVERING', 'DELIVERED'
        RETURNING = 'RETURNING', 'RETURNING'

       
    serial_number = models.CharField(max_length=100, unique=True, primary_key=True)
    model = models.CharField(choices=DroneModelChoices.choices, default=DroneModelChoices.LIGHTWEIGHT, blank=False, null=False)
    weight_limit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    battery_capacity = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=[MinValueValidator(1), MaxValueValidator(100)])
    status = models.CharField(choices=DroneStatusChoices.choices, default=DroneStatusChoices.IDLE, blank=False, null=False)

    class Meta:
       verbose_name_plural = "Drones"

    def __str__(self):
        return self.serial_number


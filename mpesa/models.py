from django.db import models

# Create your models here.
class MpesaExpress(models.Model):
    phone_number = models.PositiveBigIntegerField()
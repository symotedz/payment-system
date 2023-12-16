from django.db import models

# Create your models here.
class MpesaExpress(models.Model):
    phone_number = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.PositiveBigIntegerField()
    is_confirmed = models.BooleanField(default=True)
    ACCOUNT_REFERENCE = models.CharField(max_length = 255)
    Transcation_description = models.CharField(max_length=255)
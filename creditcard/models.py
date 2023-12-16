from django.db import models

# Create your models here.
class CreditCardDetails(models.Model):
    card_number = models.BigIntegerField()
    expirely_date = models.DateField()
    CVV = models.CharField(max_length=255)
from django.db import models

# Create your models here.
class MpesaExpress(models.Model):
    amount = models.DecimalField(verbose_name = "Amount", max_digits=5, decimal_places=2)
    receipt_no = models.CharField(verbose_name="Mpesa Receipt Number", max_length=100)
    transcation_date = models.DateTimeField(verbose_name="Transcation Date")
    phone = models.PositiveIntegerField(verbose_name="Phone Number")
    is_confirmed = models.BooleanField(verbose_name="confirmed", default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
def dict_instance():
    return ({'name' : 'simon'})
    
class ApiResponses(models.Model):
    responses = models.JSONField(verbose_name = "mpesa_result", default=dict_instance)
    
class LipaNaMpesa(models.Model):
    type = models.CharField(verbose_name = "Transcation Type", max_length=200)
    transcation_date = models.DateTimeField(verbose_name="Transcation date")
    receipt_no = models.CharField(verbose_name = "Mpesa Receipt Number", max_length=50)
    ref_no = models.CharField(verbose_name = "reference number", max_length=100, null=True, blank=True)
    invoice_no = models.CharField(verbose_name = "invoice number", max_length=15)
    acc_balance = models.DecimalField(verbose_name = "account balance", decimal_places = 2, max_digits=5)
    third_party = models.CharField(max_length=10, verbose_name = "Third party ID")
    phone = models.PositiveIntegerField(verbose_name = "mobile phone number")
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    time_stamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
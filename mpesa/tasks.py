
from mpesa.models import MpesaExpress



def get_express_payement(phone:int,amount:int):
    obj = MpesaExpress.objects.filter(phone = phone).filter(amount = amount).filter(is_confirmed = False).exits()
    return obj
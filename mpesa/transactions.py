import request

import datetime
import base64

from django.conf import settings

class ExpressException(Exception):
    pass

def mpesa_express(phone_no: int, amount: int, description="payment"):
    """Return a json object
    args:
      :phone_no:int
      :amount: int
      :description: string

    make a request to mpesa express api
    """
    pass_key = settings.PASS_KEY
    short_code = settings.BUSINESS_SHORT_CODE

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    password = str(short_code) + pass_key + timestamp
    byte_password = password.encode()
    new_password = base64.b64encode(byte_password)
    new_password = new_password.decode()
    payload = {
        "BusinessShortCode": settings.BUSINESS_SHORT_CODE,
        "Password": new_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_no,
        "PartyB": short_code,
        "PhoneNumber": phone_no,
        "CallBackURL": "https://squid-app-9xncj.ondigitalocean.app/mpesa/stk-callback/",
        "AccountReference": settings.ACCOUNT_REFERENCE[:12],
        "TransactionDesc": description[:13],
    }
    header = {"Authorization": "Bearer 5Fwz2gaTqE1XtJZSAB9AoORZ0yLm","Content-Type": "application/json"}
    response = requests.post(
        "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        headers=header,
        json= payload
    )
    print(response.json())
    
    if 'errorCode' in  response.json():
        raise ExpressExceptions("Invalid access token, use a valid access token")
    else:
        print(response.json()["ResponseDescription"])
        return "success"
    # return None
    # try:
    #     if 'errorCode' in  response.json():
    #         raise ExpressExceptions("Tranasaction failed, invalid access tokens")
    # except ExpressExceptions:
    #     pass
    # finally:
    #     return None


# mpesa_express(254114241129, 1)

def customer_to_business(type:str,phone:int,amount:int,account_number=None):
    if account_number == None:
        account_number = ""
    
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer A1pviNAIhlXSzBZJ6G1hADIAV66m'}

    payload = {
    "ShortCode": 600426,#change to use the settings in production
    "CommandID": type,
    "amount": amount,
    "MSISDN": phone,
    "BillRefNumber": account_number,}

    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers = headers, json = payload)
    print(response.text.encode('utf8'))
    if response.json()["ResponseCode"] == str(0):
        return "sucessful"
    else:
        return "failed"

    

import json
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse

from webapp.models import MpesaExpress, ApiResponses, LipaNaMpesa
from . forms import ExpressNumberForm
from . transactions import mpesa_express
from . tasks import get_express_payement

def mpesa_index(request):
    return HttpResponse('hello mpesa')


class ExpressNumber(View):
    def setup(self, request, *args, **kwargs):
        self.form = ExpressNumberForm()
        return super().setup(request, *args, **kwargs)
    
    def get(request):
        form = ExpressNumberForm()
        return render(request, "express.html", context={"form":form})
    
    def post(request):
        form = ExpressNumberForm(request.POST)
        if form.is_valid():
            phone_num = form.cleaned_data["phone"]
            amount = form.cleaned_data["amount"]
            status = MpesaExpress(phone_num, 1)
            if status == "success":
                result = get_express_payement.delay(phone_num, amount)
                result = result.get()
                result.is_confirmed = True
                result.save()
                return render(request, "express_success.html")
            else:
                #redirect(reverse("phone"))
                return render(request, "express.html", {"form" : form})
            
class MpesaExpressCallBack(View):
    """
    safaricom sandbox callback
    save api result in the database
    """
    def post(request):
        print(json.loads(request.body))
        stk_results = json.loads(request.body)
        ApiResponses.objects.create(stk_results)
        if not stk_results["Body"]["stkCallback"]["ResultCode"] == 0:
            pass
        else:
            MpesaExpress.objects.create(
                        amount = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"],
                        receipt_no = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"],
                        transaction_date = datetime.strptime(str(stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][2]["Value"]),"%Y%m%d%H%M%S"),
                        phone = stk_results["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
            )
            print(MpesaExpress.objects.last())
            return HttpResponse("")
        
class ValidationView(View):
    """ C2B validation view, return accepted """
    def post(request):
        print(json.loads)
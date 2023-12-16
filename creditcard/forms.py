from django import forms
from . models import CreditCardDetails

# forms and model forms
class CreditCardDetailsForm(forms.ModelForm):
    class Meta:
        model = CreditCardDetails
        fields = '__all__'
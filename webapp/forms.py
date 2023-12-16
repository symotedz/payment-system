from django import forms 
from .models import LipaNaMpesa, MpesaExpress 
from . models import  UserProfile, CardDetails

class LipaNaMpesaForm(forms.ModelForm):
    class Meta:
        models = LipaNaMpesa
        fields = '__all__'

class MpesaExpressForm(forms.ModelForm):
    class Meta:
        models = MpesaExpress
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username =forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

class CardDetailsForm(forms.ModelForm):
    class Meta:
        model = CardDetails
        fields = '__all__'
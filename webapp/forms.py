from django import forms 
from .models import LipaNaMpesa, MpesaExpress 
from . models import  UserProfile

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
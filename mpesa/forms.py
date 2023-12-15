from django import forms
from django.core.validators import RegexValidator


class ExpressNumberForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=12,
        min_length=10,
        widget = forms.TextInput(attrs={'name': 'phone'}),
        label = "Phone Number",
        initial = 254,
        help_text = "your mpesa registered number",
    )
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'name' : 'amount'}), label='Amount', initial=1)
    


class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(
        max_length=12,
        validators=[
            RegexValidator(r"^07((\d{7})|((\d{3})-(\d{3})-(\d{3})))$"),
        ],
        label="Phone Number",
        help_text="Enter your Mpesa phone number starting with 07.",
    )
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        min_value=0.01,
        label="Amount",
        help_text="Enter the amount you want to pay (minimum KSh 0.01).",
    )
    reference_number = forms.CharField(
        max_length=50,
        label="Reference Number (Optional)",
        help_text="Enter a reference number for your payment (optional).",
    )



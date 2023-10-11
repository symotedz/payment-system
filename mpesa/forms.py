from django import forms

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
    
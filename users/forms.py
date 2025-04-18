from django import forms
from .models import Order, OrderClosure, FilterData


class CustomLoginForm(forms.Form):
    login = forms.CharField(max_length=100, label="Login")
    password = forms.CharField(widget=forms.PasswordInput, label="Parol")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['qayerdan', 'qayerga', 'client', 'price', 'description']


class OrderClosureForm(forms.ModelForm):
    class Meta:
        model = OrderClosure
        fields = ['close_price', 'price_turi']


class FilterForm(forms.ModelForm):
    class Meta:
        model = FilterData
        fields = ['firma_nomi', 'firma_inn', 'boss_or_bugalter_number']
        widgets = {
            'firma_nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'firma_inn': forms.TextInput(attrs={'class': 'form-control'}),
            'boss_or_bugalter_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

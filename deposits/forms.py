from deposits.models import Deposits, select_confirm, select_auto_capitalization
from main.models import select_currency

from django.core.exceptions import ValidationError

# from main.models import deposit,loan,expenses   #шмпортуємо всі моделі таблиць щоб повязати їх з флормами і БД
from django.forms import ModelForm, TextInput, DateInput, Select


class add_depositForm(ModelForm):

    class Meta:
        model = Deposits
        fields = ['bank', 'name', 'sum', 'currency', 'rate', 'period', 'start_date', 'end_date', 'add_deposit', 'auto_capitalization', 'terminate_deposit']
        widgets = {
            "bank": TextInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Bank name'}),
            "name": TextInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Deposit name'
            }),
            "sum": TextInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Add deposit sum'
            }),
            "currency": Select(choices=select_currency, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
            "rate": TextInput(attrs={
                'class': 'form-control' ,         # Стиль від bootstrap
                'placeholder': 'Add deposit rate'
            }),
            "period": TextInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Add deposit period (in month)'
            }),
            "start_date": DateInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Deposit start date (YYYY-MM-DD format)'
            }),
            "end_date": DateInput(attrs={
                'class': 'form-control' , #стиль від bootstrap
                'placeholder': 'Deposit end date (YYYY-MM-DD format)'
            }),
            "add_deposit": Select(choices=select_confirm, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
            "auto_capitalization": Select(choices=select_auto_capitalization, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
            "terminate_deposit": Select(choices=select_confirm, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
        }


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['currency'].widget.attrs.update({'class':'form-control'})
        # self.fields['add_deposit'].widget.attrs.update({'class': 'form-control'})
        # self.fields['auto_capitalization'].widget.attrs.update({'class': 'form-control'})
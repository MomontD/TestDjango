# from deposits.models import Deposits, select_confirm, select_auto_capitalization
# from main.models import select_currency
# from main.models import deposit,loan,expenses   #шмпортуємо всі моделі таблиць щоб повязати їх з флормами і БД
# from django.forms import ModelForm, TextInput, DateInput, Select

from main.models import select_currency

from governments.models import Governments, select_type_gv, select_type_payment

from django.forms import ModelForm, TextInput, DateInput, Select


class add_governmentForm(ModelForm):

    class Meta:
        model = Governments
        fields = ['name', 'type_gv', 'sum', 'currency', 'coupons', 'rate', 'start_date', 'end_date',
                  'coupons_nominal_cost', 'coupons_current_cost', 'bonds_repayment_nominal', 'bonds_expenses']  # 'period'
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Code Government (UA400...90)'
            }),
            "type_gv": Select(choices=select_type_gv, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
            "sum": TextInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Government sum'
            }),
            "currency": Select(choices=select_currency, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
            "coupons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of coupons'
            }),
            "rate": TextInput(attrs={
                'class': 'form-control' ,         # Стиль від bootstrap
                'placeholder': 'Government rate'
            }),
            # "period": TextInput(attrs={
            #     'class': 'form-control',          # Стиль від bootstrap
            #     'placeholder': 'Optional field! Government period (in month)'
            # }),
            "start_date": DateInput(attrs={
                'class': 'form-control',          # Стиль від bootstrap
                'placeholder': 'Start date (YYYY-MM-DD format)'
            }),
            "end_date": DateInput(attrs={
                'class': 'form-control' , #стиль від bootstrap
                'placeholder': 'End date (YYYY-MM-DD format)'
            }),
            "coupons_nominal_cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nominal cost'
            }),
            "coupons_current_cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Current cost'
            }),
            "bonds_repayment_nominal": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nominal repayment'
            }),
            "bonds_expenses": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bonds expenses'
            })
        }
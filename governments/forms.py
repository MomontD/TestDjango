from main.models import select_currency

from governments.models import Governments, PaymentSchedule, select_type_gv, select_type_payment

from django.forms import ModelForm, TextInput, DateInput, Select


class AddPaymentSchedule(ModelForm):

    class Meta:
        model = PaymentSchedule
        fields = ['payment_type', 'payment_date', 'payment_sum']
        widgets = {
            "payment_type": Select(choices=select_type_payment, attrs={
                'class': 'form-control-sm',
                'placeholder': 'Enter your choice'
            }),
            "payment_date": DateInput(attrs={
                    'class': 'form-control-sm',          # Стиль від bootstrap
                    'placeholder': 'Payment date (YYYY-MM-DD)'
                }),
            "payment_sum": TextInput(attrs={
                'class': 'form-control-sm',  # Стиль від bootstrap
                'placeholder': 'Government sum'
            }),
    }


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
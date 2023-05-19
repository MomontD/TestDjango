from django.forms import ModelForm, TextInput, DateInput, Select

from main.models import select_currency

from loans.models import Loans


class add_loanForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['name', 'sum', 'currency', 'rate', 'period', 'start_date', 'end_date']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',  # стиль від bootstrap
                'placeholder': 'Loan name'
            }),
            "sum": TextInput(attrs={
                'class': 'form-control',  # стиль від bootstrap
                'placeholder': 'Add loan sum'
            }),
            "currency": Select(choices=select_currency, attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice'
            }),
            "rate": TextInput(attrs={
                'class': 'form-control',  # стиль від bootstrap
                'placeholder': 'Add loan rate'
            }),
            "period": TextInput(attrs={
                'class': 'form-control',  # стиль від bootstrap
                'placeholder': 'Add loan period (in month)'
            }),
            "start_date": DateInput(attrs={
                'class': 'form-control',  # стиль від bootstrap
                'placeholder': 'Loan start date (YYYY-MM-DD format)'
            }),
            "end_date": DateInput(attrs={
                'class': 'form-control',  # стиль від bootstrap
                'placeholder': 'Loan end date (YYYY-MM-DD format)'
            })
        }
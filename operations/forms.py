from main.models import *
# from main.models import deposit,loan,expenses   #шмпортуємо всі моделі таблиць щоб повязати їх з флормами і БД
from django.forms import ModelForm,TextInput,DateInput

class add_depositForm(ModelForm) :
    class Meta :
        model  = deposit
        fields = ['deposit_date','deposit_sum','deposit_rate','deposit_period','start_date','end_date']
        widgets = {
            "deposit_date" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Deposit name'
            }),
            "deposit_sum" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add deposit sum'
            }),
            "deposit_rate" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add deposit rate'
            }),
            "deposit_period" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add deposit period (in month)'
            }),
            "start_date" : DateInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Deposit start date (YYYY-MM-DD format)'
            }),
            "end_date" : DateInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Deposit end date (YYYY-MM-DD format)'
            })
        }


class add_loanForm(ModelForm) :
    class Meta :
        model  = loan
        fields = ['debt_date','debt_sum','debt_rate','debt_period','start_date','end_date']
        widgets = {
            "debt_date" : TextInput(attrs = {
                'class'           : 'form-control' , #стиль від bootstrap
                'placeholder'     : 'Loan name'
            }),
            "debt_sum" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add loan sum'
            }),
            "debt_rate" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add loan rate'
            }),
            "debt_period" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add loan period (in month)'
            }),
            "start_date" : DateInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Loan start date (YYYY-MM-DD format)'
            }),
            "end_date"   : DateInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Loan end date (YYYY-MM-DD format)'
            })
        }





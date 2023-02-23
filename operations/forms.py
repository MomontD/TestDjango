from main.models import *
# from main.models import deposit,loan,expenses   #шмпортуємо всі моделі таблиць щоб повязати їх з флормами і БД
from django.forms import ModelForm,TextInput,DateInput,ChoiceField

class add_depositForm(ModelForm) :

    class Meta :
        model  = deposit
        fields = ['bank','name','sum','currency','rate','period','start_date','end_date']
        widgets = {
            "bank" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Bank name'}),
            "name" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Deposit name'
            }),
            "sum" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add deposit sum'
            }),
            # "currency" : ChoiceField(choices=select_currency,attrs = {
            #     'class'       : 'form-control' , #стиль від bootstrap
            #     'placeholder' : 'Add deposit currency',
            #      }),
            "rate" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add deposit rate'
            }),
            "period" : TextInput(attrs = {
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['currency'].widget.attrs.update({'class':'form-control'})

class add_loanForm(ModelForm) :
    class Meta :
        model  = loan
        fields = ['name','sum','currency','rate','period','start_date','end_date']
        widgets = {
            "name" : TextInput(attrs = {
                'class'           : 'form-control' , #стиль від bootstrap
                'placeholder'     : 'Loan name'
            }),
            "sum" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add loan sum'
            }),
            "currency" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add loan currency'
            }),
            "rate" : TextInput(attrs = {
                'class'       : 'form-control' , #стиль від bootstrap
                'placeholder' : 'Add loan rate'
            }),
            "period" : TextInput(attrs = {
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





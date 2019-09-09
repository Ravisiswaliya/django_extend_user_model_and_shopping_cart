from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


# new account registration form
class AccountRegister(UserCreationForm):
    
    class Meta():
        model = Account
        fields = ['username', 'email']
    
    # method to remove help text
    def __init__(self, *args, **kwargs):
        super(AccountRegister, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



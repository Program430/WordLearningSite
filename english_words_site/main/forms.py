from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data['password1'] = self.data['password']
        self.data['password2'] =  self.data['password']
        del self.data['password']

        


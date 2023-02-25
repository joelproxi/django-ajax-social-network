from django import forms
from django.contrib.auth.models import User

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email')
        model = User
        
    def check_password(self):
        cd = self.changed_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Vos mot de passe sont incorrecte")
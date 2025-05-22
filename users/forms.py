from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    
    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'{email} not found')
        return email
    
    def clean_password(self):
        password = self.data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password\'s lenght must be greater than 8')
        return password
    
    
    
    
class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','password','confirm_password']
        
        
    
    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'{email.title()} already exist ')
        return email
    

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError('Password did not match')
        
        return confirm_password
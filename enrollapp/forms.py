from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget = forms.PasswordInput )
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'is_active']
        labels = {'email':'Email'}
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'disabled':True}),
        }

class UserLoginForm(AuthenticationForm):
    pass

class UserPasswordChangeForm(PasswordChangeForm):
    pass

class UserSetPasswordForm(SetPasswordForm):
    pass

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
        labels = {'email':'Email'}
        widgets = {
            'email': forms.EmailInput(attrs={'style': 'width:100px'}),
            'date_joined': forms.TextInput(attrs={'disabled':True}),
            'is_active': forms.CheckboxInput(attrs={'disabled':True}),
            'last_login': forms.TextInput(attrs={'disabled':True}),
         }

        
class EditManagerProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'last_login']
        labels = {'email':'Email'}
        widgets = {
            'email': forms.EmailInput(attrs={'style': 'width:250px','class':'form-control'}),
            'date_joined': forms.TextInput(attrs={'disabled':True}),
            'is_active': forms.CheckboxInput(attrs={'disabled':True}),
            'is_staff': forms.CheckboxInput(attrs={'disabled':True}),
            'is_superuser': forms.CheckboxInput(attrs={'disabled':True}),
            'last_login': forms.TextInput(attrs={'disabled':True}),
         }
        
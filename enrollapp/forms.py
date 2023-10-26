from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget = forms.PasswordInput )
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
        labels = {'email':'Email'}

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

class EditAdminUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields= '__all__'
        labels = {'email':'Email'}
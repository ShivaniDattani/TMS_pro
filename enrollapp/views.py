from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, UserLoginForm, UserPasswordChangeForm, UserSetPasswordForm, EditUserProfileForm, EditManagerProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from trainingapp.models import TrainingRecord

# Create your views here.
def sign_up(request):
    if request.method =="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Staff-Group')
            user.group.add(group)
            messages.success(request, 'Account Created Successfully!! Go to Login page')
    else:
        fm = SignUpForm()
    return render(request, 'enrollapp/signup.html', {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = UserLoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, 'Invalid Login details')
                    return HttpResponseRedirect('login/')
        else:
            fm = UserLoginForm()
        return render(request, 'enrollapp/userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')
        #return HttpResponseRedirect('profile.html')

   
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditManagerProfileForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance = request.user)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request, "Data updated successfully!!")
        else:
            if request.user.is_superuser == True:
                fm = EditManagerProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance = request.user)
                users = None
        return render(request, 'enrollapp/profile.html', {'name': request.user, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    # storage = messages.get_messages(request)
    # storage.used = True
    # messages.success(request, 'Thanks for using the app!!')
    return HttpResponseRedirect('/login/')

#change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = UserPasswordChangeForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Password Changed Successfully, Please login with your new password !!')
                return HttpResponseRedirect('/login/')
        else:
            fm = UserPasswordChangeForm(user = request.user)
        return render(request, 'enrollapp/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def user_set_pass(request):
    if request.method == "POST":
        fm = UserSetPasswordForm(user = request.user, data = request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Password Changed Successfully, Please login with your new password !!')
            return HttpResponseRedirect('/profile/')
    else:
        fm = UserSetPasswordForm(user = request.user)
    return render(request, 'enrollapp/setpass.html', {'form':fm})


def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditManagerProfileForm(instance=pi)
        return render(request, 'enrollapp/userdetails.html', {'form':fm})
    else:
       # return HttpResponseRedirect('/profile/')
        return HttpResponseRedirect('/profile/')

def home(request):
    if request.user.is_authenticated:
        training = TrainingRecord.objects.filter(employee_id=request.user)
        return render(request, 'enrollapp/home.html', {'training':training})
    else:
        return HttpResponseRedirect('/login/')
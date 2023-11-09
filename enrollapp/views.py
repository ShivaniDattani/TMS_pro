from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, UserLoginForm, UserPasswordChangeForm, UserSetPasswordForm, EditUserProfileForm, EditManagerProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from trainingapp.models import TrainingRecord
from courseapp.models import CourseGroupSyllabus, CourseDetails, CourseGroup
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method =="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            user.is_active = True
            group = Group.objects.get(name='Staff-Group')
            group.user_set.add(user)
            user.save()
            
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

@login_required
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_staff == True:
                fm = EditManagerProfileForm(request.POST, instance = request.user)
            else:
                fm = EditUserProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Data updated successfully!!")
        else:
            if request.user.is_staff == True:
                fm = EditManagerProfileForm(instance = request.user)
            else:
                fm = EditUserProfileForm(instance = request.user)
        return render(request, 'enrollapp/profile.html', {'name': request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    return HttpResponseRedirect('/login/')

#change password with old password
@login_required
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

@login_required
def user_detail(request):
    if request.user.is_staff:
        users = User.objects.all()
        return render(request, 'enrollapp/userdetails.html', {'users': users})
    else:
        return HttpResponseRedirect('/profile/')

@login_required
def showuser_detail(request,id):
    if request.user.is_staff:
        showuser = User.objects.get(pk = id)
        fm = EditManagerProfileForm(instance=showuser)
        users = User.objects.all()
        return render(request, 'enrollapp/userdetails.html', {'form':fm, 'users': users})
    else:
        return HttpResponseRedirect('/profile/')

# @login_required
# def user_detail(request, id):
#     if request.user.is_staff:
#         if id == None:
#             users = User.objects.all()
#             pi = User.object.get(pk=request.user)
#         else:
#             users = User.objects.all()
#             pi = User.objects.get(pk=id)
#         fm = EditManagerProfileForm(instance=pi)
#         return render(request, 'enrollapp/userdetails.html', {'form':fm, 'users':users})
#     else:
#         return HttpResponseRedirect('/profile/')


def home(request):
    if request.user.is_authenticated:
        # show their training record
        training = TrainingRecord.objects.filter(employee_id=request.user)

        #show suggested courses
        if not training:
            newstartergroup = CourseGroup.objects.filter(group_name__icontains='New starters').all()
            suggestedCourses = CourseGroupSyllabus.objects.filter(course_group_id__in=newstartergroup)
        else:
            training_grouplist = []
            training_recordlist = []
            for tr in training:
                traininggroups = tr.training_id.course_group_id
                if traininggroups not in training_grouplist:
                    training_grouplist.append(traininggroups)
                training_record = tr.training_id.course_id
                training_recordlist.append(training_record)
            print(training_recordlist)
            suggestedCourses = CourseGroupSyllabus.objects.filter(course_group_id__in=training_grouplist).exclude(course_id__in = training_recordlist)
        return render(request, 'enrollapp/home.html', {'training':training, 'courses':suggestedCourses})
    else:
        return HttpResponseRedirect('/login/')
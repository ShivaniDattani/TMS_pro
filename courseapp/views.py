from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from courseapp.models import CourseDetails,CourseGroup,CourseGroupSyllabus
from courseapp.forms import CourseDetailsForm, CourseGroupForm, CourseGroupSyllabusForm

from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def add_course(request):
    if request.method == 'POST':
        fm = CourseDetailsForm(request.POST)
        if fm.is_valid():  
            fm.save()
            fm = CourseDetailsForm()
            messages.success(request, 'Course Successfully Added!!')
    else:
        fm = CourseDetailsForm()
    courses = CourseDetails.objects.all()
    return render(request, 'courseapp/add_details.html', {'form':fm, 'courses':courses})

@user_passes_test(lambda user: user.is_superuser)
def delete_course(request, id):
    if request.method == 'POST':
        course = CourseDetails.objects.get(pk=id)
        course.delete()
        return HttpResponseRedirect('/add_details')

@user_passes_test(lambda user: user.is_superuser)
def update_course(request, id):
    if request.method == 'POST':
        course = CourseDetails.objects.get(pk=id)
        fm = CourseDetailsForm(request.POST, instance=course)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Course Successfully Updated!!')
    else:
        course = CourseDetails.objects.get(pk=id)
        fm = CourseDetailsForm(instance=course)
    return render(request, 'courseapp/update_details.html', {'form':fm})

@user_passes_test(lambda user: user.is_superuser)
def add_group(request):
    if request.method == 'POST':
        fm = CourseGroupForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = CourseGroupForm()
            messages.success(request, 'Group Successfully Added!!')
    else:
        fm = CourseGroupForm()
    groups = CourseGroup.objects.all()
    return render(request, 'courseapp/add_group.html', {'form':fm, 'groups':groups })

@user_passes_test(lambda user: user.is_superuser)
def update_group(request, id):
    if request.method == 'POST':
        group = CourseGroup.objects.get(pk=id)
        fm = CourseGroupForm(request.POST, instance=group)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Group Successfully Updated!!')
    else:
        group = CourseGroup.objects.get(pk=id)
        fm = CourseGroupForm(instance=group)
    return render(request, 'courseapp/update_group.html', {'form':fm})

@user_passes_test(lambda user: user.is_superuser)
def delete_group(request, id):
    if request.method == 'POST':
        group = CourseGroup.objects.get(pk=id)
        group.delete()
        return HttpResponseRedirect('/add_group')

@user_passes_test(lambda user: user.is_superuser)
def add_syllabus(request):
    if request.method == 'POST':
        fm = CourseGroupSyllabusForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = CourseGroupSyllabusForm()
            messages.success(request, 'Syllabus Successfully Added!!')
    else:
        fm = CourseGroupSyllabusForm()
    syllabus = CourseGroupSyllabus.objects.all()
    return render(request, 'courseapp/add_syllabus.html', {'form':fm, 'syllabus':syllabus })

@user_passes_test(lambda user: user.is_superuser)
def update_syllabus(request, id):
    if request.method == 'POST':
        syllabus = CourseGroupSyllabus.objects.get(pk=id)
        fm = CourseGroupSyllabusForm(request.POST, instance=syllabus)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Syllabus Successfully Updated!!')
    else:
        syllabus = CourseGroupSyllabus.objects.get(pk=id)
        fm = CourseGroupSyllabusForm(instance=syllabus)
    return render(request, 'courseapp/update_syllabus.html', {'form':fm})

@user_passes_test(lambda user: user.is_superuser)
def delete_syllabus(request, id):
    if request.method == 'POST':
        syllabus = CourseGroupSyllabus.objects.get(pk=id)
        syllabus.delete()
        return HttpResponseRedirect('/add_syllabus')
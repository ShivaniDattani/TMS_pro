
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from trainingapp.forms import StaffTrainingRecordForm
from trainingapp.models import TrainingRecord
from courseapp.models import CourseDetails, CourseGroupSyllabus
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_training(request, syllabus_id):
    if request.user.is_authenticated:
        syllabus = get_object_or_404(CourseGroupSyllabus, id=syllabus_id)
        if request.method == "POST":        
            form = StaffTrainingRecordForm(request.POST)
            if form.is_valid():
                new_record = form.save(commit=False)
                new_record.training_id = syllabus
                new_record.employee_id = request.user
                if TrainingRecord.objects.filter(training_id = new_record.training_id, employee_id = new_record.employee_id, completed_on = new_record.completed_on).exists():
                    messages.info(request, "Record already exists!")
                else:
                    new_record.save()
                    messages.success(request, "Record successfully Added!")
        else: 
            form = StaffTrainingRecordForm()
        training = TrainingRecord.objects.filter(employee_id=request.user)
        return render(request, 'trainingapp/add_training.html', {'syllabus': syllabus, 'form':form, 'training':training})
    else:
        return HttpResponseRedirect('/login/')

def show_training_record(request):
    if request.user.is_authenticated:
        training = TrainingRecord.objects.all()
        query = request.GET.get("q")
        if query == "":
            training = TrainingRecord.objects.all()
        else:
            user = User.objects.filter(username=query).all()
            training = TrainingRecord.objects.filter(employee_id__in = user)
        return render(request, 'trainingapp/show_trainingrecord.html', {'training': training})
    else:
        return HttpResponseRedirect('/login/')

def show_available_training(request):
    if request.user.is_authenticated:
        query = request.GET.get("q")
        if query == None:
            avail_training = CourseGroupSyllabus.objects.all()
        else:
            courses = CourseDetails.objects.filter(course_name__icontains=query).all()
            avail_training = CourseGroupSyllabus.objects.filter(course_id__in = courses)
        return render(request, 'trainingapp/show_availtraining.html', {'avail_training': avail_training})
    else:
        return HttpResponseRedirect('/login/')

@login_required
def delete_training(request, training_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            training = TrainingRecord.objects.filter(id=training_id)
            training.delete()
            return HttpResponseRedirect('/add_training')
    else:
        return HttpResponseRedirect('/login/')

@login_required   
def update_training(request, training_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            training = TrainingRecord.objects.get(pk=training_id)
            form = StaffTrainingRecordForm(request.POST, instance=training)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Successfully Updated!')
        else:
            training = TrainingRecord.objects.get(pk=training_id)
            form = StaffTrainingRecordForm(instance=training)
        return render(request, 'trainingapp/update_training.html', {'form':form, 'training':training})
    else:
        return HttpResponseRedirect('/login/')       
    # form = StaffTrainingRecordForm()
    # course = get_object_or_404(TrainingRecord, id=2)
    # form.training_id = course
    # form.employee_id = request.user
    # training = TrainingRecord.objects.all()
    # return render(request, 'trainingapp/update_training.html', {'form':form, 'training':training })



from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from trainingapp.forms import StaffTrainingRecordForm
from trainingapp.models import TrainingRecord
from courseapp.models import CourseDetails, CourseGroupSyllabus


# Create your views here.
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
                    messages.info(request, "Training already exists!")
                else:
                    new_record.save()
                    messages.success(request, "Record successfully Added!")
        else: 
            form = StaffTrainingRecordForm()
        return render(request, 'trainingapp/add_training.html', {'syllabus': syllabus, 'form':form})
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

def update_trainingrecord(request):
    form = StaffTrainingRecordForm()
    course = get_object_or_404(CourseGroupSyllabus, id=2)
    form.training_id = course
    form.employee_id = request.user
    training = TrainingRecord.objects.all()
    return render(request, 'trainingapp/update_traininigrecord.html', {'form':form, 'training':training })
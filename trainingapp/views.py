
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from trainingapp.forms import StaffTrainingRecordForm
from trainingapp.models import TrainingRecord
from courseapp.models import CourseDetails, CourseGroupSyllabus


# Create your views here.
def add_training(request, course_id):

    # print(course_id)
    # return render(request, 'trainingapp/add_training.html')

    course = get_object_or_404(CourseGroupSyllabus, id=course_id) 
    print(course)
    #form = StaffTrainingRecordForm()

    # if request.method == "POST":        
    #     form = StaffTrainingRecordForm(request.POST)
    #     if form.is_valid():
    #         new_record = form.save(commit=False)
    #         #print(new_record.type())
    #         new_record.training_id = course.course_id
    #         new_record.employee_id = request.user
    #         new_record.save()
    #         return redirect('trainingapp/add_training.html')
    # else: 
    #     form = StaffTrainingRecordForm()
    return render(request, 'trainingapp/add_training.html')


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
    
# def complete_training(request, id):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             fm = StaffTrainingRecordForm(request.POST)
#             fm["employee_id"] = user.username

def update_trainingrecord(request):
    form = StaffTrainingRecordForm()
    course = get_object_or_404(CourseGroupSyllabus, id=2)
    form.training_id = course
    form.employee_id = request.user
    return render(request, 'trainingapp/update_traininigrecord.html', {'form':form })
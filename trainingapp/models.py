
from django.db import models
from courseapp.models import CourseGroupSyllabus
from django.contrib.auth.models import User

# Create your models here.
class TrainingRecord(models.Model):
    training_id = models.ForeignKey(CourseGroupSyllabus, verbose_name="Course Syllabus Id", on_delete=models.CASCADE )
    employee_id = models.ForeignKey(User, verbose_name="User Id", on_delete= models.CASCADE)
    # completed_on = models.DateField(default=timezone.now)
    completed_on = models.DateField()
            
    
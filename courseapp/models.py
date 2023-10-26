from django.db import models
from django_enumfield import enum
from enum import IntEnum

# Create your models here.
class CourseDetails(models.Model):
    course_name = models.CharField(max_length=100, unique=True, blank=False)
    course_link = models.URLField(verbose_name="Course Link", max_length=1000, unique=True, blank=False)
    course_desc = models.TextField(blank=True)

    def __str__(self):
        return self.course_name

class CourseGroup(models.Model):
    group_name = models.CharField(max_length=25)
    group_desc = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.group_name

class CourseInterval(IntEnum):
    ONE_OFF = 0
    ANNUALLY = 12
    BI_ANNUALLY = 24
    TRI_ANNUALLY = 36

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace('_', ' ').lower().capitalize()) for key in cls]

class CourseGroupSyllabus(models.Model):
    course_id = models.ForeignKey("CourseDetails", verbose_name="Course Id", on_delete=models.CASCADE)
    
    # CourseGroupSyllabus y = ...
    ## CourseDetails x = y.course 

    course_group_id = models.ForeignKey("CourseGroup", verbose_name="Group Id", on_delete=models.CASCADE)
    course_interval = models.IntegerField(choices=CourseInterval.choices(), default = CourseInterval.ONE_OFF )
    course_mandatory = models.BooleanField(default=False)


    def __str__(self):
        return self.course_id.course_name
    
# CourseGroupSyllabus.course_id.id
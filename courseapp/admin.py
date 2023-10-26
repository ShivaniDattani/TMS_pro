from django.contrib import admin
from courseapp.models import CourseDetails, CourseGroup, CourseGroupSyllabus

# Register your models here.

admin.site.register(CourseDetails)
admin.site.register(CourseGroup)
admin.site.register(CourseGroupSyllabus)
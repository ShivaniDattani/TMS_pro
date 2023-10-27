from django.urls import path
from courseapp import views

appname='courseapp'

urlpatterns = [
    path('add_details/', views.add_course, name='add_details'),
    path('delete/<int:id>/', views.delete_course, name='delete_course'),
    path('update/<int:id>/', views.update_course, name='update_course'),
    path('add_group/', views.add_group, name='add_group'),
    path('delete_group/<int:id>/', views.delete_group, name='delete_group'),
    path('update_group/<int:id>/', views.update_group, name='update_group'),
    path('add_syllabus/', views.add_syllabus, name='add_syllabus'),
    path('delete_syllabus/<int:id>/', views.delete_syllabus, name='delete_syllabus'),
    path('update_syllabus/<int:id>/', views.update_syllabus, name='update_syllabus'),
]
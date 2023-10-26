from django.urls import path
from trainingapp import views

appname='trainingapp'

urlpatterns = [
    path('add_training/<int:syllabus_id>', views.add_training, name='add_training'),
    path('show_availtraining/', views.show_available_training, name='show_availtraining'),
    path('update_traininigrecord/', views.update_trainingrecord, name='update_traininigrecord')
]
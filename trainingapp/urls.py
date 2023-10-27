from django.urls import path
from trainingapp import views

appname='trainingapp'

urlpatterns = [
    path('add_training/<int:syllabus_id>', views.add_training, name='add_training'),
    path('show_availtraining/', views.show_available_training, name='show_availtraining'),
    path('delete_training/<int:training_id>', views.delete_training, name='delete_training'),
    path('update_training/<int:training_id>', views.update_training, name='update_training')
]
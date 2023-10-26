from datetime import date
from django import forms
from trainingapp import models
from django.contrib.auth.models import User
from enrollapp.forms import SignUpForm

class StaffTrainingRecordForm(forms.ModelForm):

    # training_id = forms.Select(attrs={'training_id':'Training Id'})
    # completed_on = forms.DateField()

    # class Meta:
    #     model = User
    #     fields = ['']
    completed_on = forms.DateField(label='Completed Date', widget=forms.SelectDateWidget(attrs={'type':'date'}))
    class Meta:
        model = models.TrainingRecord
        fields = ['completed_on']
        #labels = {'completed_on': 'Completed Date '}
       #widgets = { 'completed_on': forms.DateInput(format="%m/%d/%Y"), }
from datetime import datetime
from django import forms
from trainingapp import models
from django.contrib.auth.models import User
from enrollapp.forms import SignUpForm

class StaffTrainingRecordForm(forms.ModelForm):

    completed_on = forms.DateField(label='Completed Date', widget=forms.SelectDateWidget(attrs={'type':'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['completed_on'].initial = datetime.now()

    class Meta:
        model = models.TrainingRecord
        fields = ['completed_on']
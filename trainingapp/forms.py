from datetime import date, datetime
from django import forms
from trainingapp import models
from django.contrib.auth.models import User
from enrollapp.forms import SignUpForm

class StaffTrainingRecordForm(forms.ModelForm):

    # completed_on = forms.DateField(label='Completed Date', widget=forms.SelectDateWidget(attrs={'type':'date'}))
    today = date.today()
    
    completed_on = forms.DateField(label='Completed Date', 
                                   widget=forms.SelectDateWidget(years=range(today.year-2, today.year+1)),
                                   initial=today )
    
    # completed_on = forms.DateField(label='Completed Date', widget=forms.SelectDateWidget())
   
    # completed_on = forms.DateField(label='Completed Date', widget=forms.widgets.SelectDateWidget())

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     today = datetime.today().date()
    #     min_date = today.replace(year=today.year-2)
    #     max_date = today.replace(year=today.year+1)

    #     self.fields['completed_on'].initial = today
    #     self.fields['completed_on'].widget.attrs['min'] = min_date
    #     self.fields['completed_on'].widget.attrs['max'] = max_date

    class Meta:
        model = models.TrainingRecord
        fields = ['completed_on']
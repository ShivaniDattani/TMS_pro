from django import forms
from courseapp import models

class CourseDetailsForm(forms.ModelForm):
    class Meta:
        model = models.CourseDetails
        fields = "__all__"
        labels = { 'course_name': 'Course Name', 'course_link': 'Course Link', 'course_desc':'Course Description'}
        widgets = { 'course_name': forms.TextInput(attrs={'class':'form-control'}), 
                   'course_link': forms.Textarea(attrs={'rows':2, 'class':'form-control'}), 
                   'course_desc': forms.Textarea(attrs={'rows':3, 'class':'form-control'})}

class CourseGroupForm(forms.ModelForm):
    class Meta:
        model = models.CourseGroup
        fields="__all__"
        labels = {'group_name':'Group Name', 'group_desc':'Group Description'}
        widgets = { 'group_name': forms.TextInput(attrs={'class':'form-control'}),
            'group_desc': forms.Textarea(attrs={'rows':3, 'cols':25, 'class':'form-control'}) }

class CourseGroupSyllabusForm(forms.ModelForm):
    class Meta:
        model = models.CourseGroupSyllabus
        fields = "__all__"
        labels = {'course_id':'Course Name', 'course_group_id': 'Course Group', 'course_interval':'Interval Pace', 'course_mandatory':'Mandatory?'}
        widgets = { 'course_group_id': forms.Select(attrs={'class':'form-control'}),
                    'course_id': forms.Select(attrs={'class':'form-control'}),
                    'course_interval': forms.Select(attrs={'class':'form-control'}),
                   }
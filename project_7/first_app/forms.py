from django import forms
# from . import models
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = ['name', 'roll']
        # exclude = ['roll']
        label = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        fields = '__all__'
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class' : 'btn btn-primary'})
        # }
        help_texts = {
            'name' : "Write Your Full Name",
            'roll' : 'Enter Your Roll Number'
        }
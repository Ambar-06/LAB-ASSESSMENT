from django import forms
from .models import *

class Sample_Intake_Form(forms.ModelForm):
    
    class Meta:
        model = SampleIntake
        fields = '__all__'


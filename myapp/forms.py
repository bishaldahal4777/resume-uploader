from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = Resume
        fields = ("name","dob","gender","locality","city","pin","state","mobile","email","job_city","profile_image","my_file")
        labels = {'name':'Full Name', 'dob':'Date of Birth', 'pin':'pin code', 'mobile': 'Contact Number', 'email':'Email Address','profile_image':'Profile Image','my_file':'Document'}
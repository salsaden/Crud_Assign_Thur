from django import forms
from Student_Database.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name', 'admission', 'course']
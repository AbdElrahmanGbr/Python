from django import forms
from .models import Student,Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {'fname' ,'lname' ,'age' ,'student_track'}
        widgets ={
            'fname': forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'student_track': forms.TextInput(attrs={'class':'form-control'}),
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model= Track
        fields = {'track_name'}

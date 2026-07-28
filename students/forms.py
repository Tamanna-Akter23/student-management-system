from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "student_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. 1119068"}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Full name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "student@example.com"}),
            "department": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Computer Science"}),
        }

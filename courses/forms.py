from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            "code": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. CSE101"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Course title"}),
            "teacher": forms.TextInput(attrs={"class": "form-control", "placeholder": "Teacher name"}),
            "credits": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 10}),
        }

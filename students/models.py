from django.db import models
class Student(models.Model):
    student_id=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=100)
    def __str__(self): return f'{self.student_id} - {self.name}'

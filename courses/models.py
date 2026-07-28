from django.db import models
class Course(models.Model):
    code=models.CharField(max_length=20,unique=True)
    title=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)
    credits=models.PositiveIntegerField(default=3)
    def __str__(self): return f'{self.code} - {self.title}'

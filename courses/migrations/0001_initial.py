from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True; dependencies=[]
    operations=[migrations.CreateModel(name='Course',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('code',models.CharField(max_length=20,unique=True)),('title',models.CharField(max_length=100)),('teacher',models.CharField(max_length=100)),('credits',models.PositiveIntegerField(default=3))])]

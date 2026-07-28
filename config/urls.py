from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.shortcuts import render

from students.models import Student
from courses.models import Course
from notes.mongo import collection


@login_required
def home(request):
    recent_students = Student.objects.order_by('-id')[:5]
    recent_courses = Course.objects.order_by('-id')[:5]
    recent_notes = list(collection().find().sort('_id', -1).limit(5))
    for item in recent_notes:
        item['id'] = str(item.pop('_id'))
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'note_count': collection().count_documents({}),
        'recent_students': recent_students,
        'recent_courses': recent_courses,
        'recent_notes': recent_notes,
    }
    return render(request, 'home.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
    path('notes/', include('notes.urls')),
]

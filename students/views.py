from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student


@login_required
def student_list(request):
    query = request.GET.get('q', '').strip()
    students = Student.objects.all().order_by('student_id')
    if query:
        students = students.filter(
            Q(student_id__icontains=query)
            | Q(name__icontains=query)
            | Q(email__icontains=query)
            | Q(department__icontains=query)
        )
    page_obj = Paginator(students, 8).get_page(request.GET.get('page'))
    return render(request, 'students/list.html', {'items': page_obj, 'page_obj': page_obj, 'query': query})


@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student added successfully.')
        return redirect('student_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Student', 'back_url': 'student_list'})


@login_required
def student_update(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student updated successfully.')
        return redirect('student_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Student', 'back_url': 'student_list'})


@login_required
def student_delete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'object': obj, 'back_url': 'student_list'})

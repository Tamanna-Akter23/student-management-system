from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm
from .models import Course


@login_required
def course_list(request):
    query = request.GET.get('q', '').strip()
    courses = Course.objects.all().order_by('code')
    if query:
        courses = courses.filter(Q(code__icontains=query) | Q(title__icontains=query) | Q(teacher__icontains=query))
    page_obj = Paginator(courses, 8).get_page(request.GET.get('page'))
    return render(request, 'courses/list.html', {'items': page_obj, 'page_obj': page_obj, 'query': query})


@login_required
def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course added successfully.')
        return redirect('course_list')
    return render(request, 'form.html', {'form': form, 'title': 'Add Course', 'back_url': 'course_list'})


@login_required
def course_update(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course updated successfully.')
        return redirect('course_list')
    return render(request, 'form.html', {'form': form, 'title': 'Edit Course', 'back_url': 'course_list'})


@login_required
def course_delete(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('course_list')
    return render(request, 'confirm_delete.html', {'object': obj, 'back_url': 'course_list'})

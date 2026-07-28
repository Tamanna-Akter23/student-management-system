from datetime import datetime, timezone

from bson import ObjectId
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render

from .mongo import collection


def get_note(note_id):
    try:
        item = collection().find_one({'_id': ObjectId(note_id)})
    except Exception as exc:
        raise Http404('Invalid note ID') from exc
    if not item:
        raise Http404('Note not found')
    item['id'] = str(item.pop('_id'))
    return item


@login_required
def note_list(request):
    query = request.GET.get('q', '').strip()
    mongo_query = {}
    if query:
        mongo_query = {'$or': [
            {'student_id': {'$regex': query, '$options': 'i'}},
            {'note': {'$regex': query, '$options': 'i'}},
        ]}
    items = list(collection().find(mongo_query).sort('created_at', -1))
    for item in items:
        item['id'] = str(item.pop('_id'))
    page_obj = Paginator(items, 9).get_page(request.GET.get('page'))
    return render(request, 'notes/list.html', {'items': page_obj, 'page_obj': page_obj, 'query': query})


@login_required
def note_create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id', '').strip()
        note = request.POST.get('note', '').strip()
        if student_id and note:
            now = datetime.now(timezone.utc)
            collection().insert_one({'student_id': student_id, 'note': note, 'created_at': now, 'updated_at': now})
            messages.success(request, 'Student note added successfully.')
            return redirect('note_list')
        messages.error(request, 'Student ID and note are required.')
    return render(request, 'notes/form.html', {'title': 'Add Student Note'})


@login_required
def note_update(request, note_id):
    item = get_note(note_id)
    if request.method == 'POST':
        student_id = request.POST.get('student_id', '').strip()
        note = request.POST.get('note', '').strip()
        if student_id and note:
            collection().update_one(
                {'_id': ObjectId(note_id)},
                {'$set': {'student_id': student_id, 'note': note, 'updated_at': datetime.now(timezone.utc)}},
            )
            messages.success(request, 'Student note updated successfully.')
            return redirect('note_list')
        messages.error(request, 'Student ID and note are required.')
    return render(request, 'notes/form.html', {'title': 'Edit Student Note', 'item': item})


@login_required
def note_delete(request, note_id):
    item = get_note(note_id)
    if request.method == 'POST':
        collection().delete_one({'_id': ObjectId(note_id)})
        messages.success(request, 'Student note deleted successfully.')
        return redirect('note_list')
    return render(request, 'notes/confirm_delete.html', {'item': item})

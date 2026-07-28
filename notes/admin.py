from datetime import datetime, timezone

from bson import ObjectId
from django.contrib import admin, messages
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import path, reverse

from .models import MongoNote
from .mongo import collection


@admin.register(MongoNote)
class MongoNoteAdmin(admin.ModelAdmin):
    """MongoDB CRUD screens integrated into the Django administration site."""

    def get_urls(self):
        opts = self.model._meta
        custom_urls = [
            path('', self.admin_site.admin_view(self.changelist_view), name=f'{opts.app_label}_{opts.model_name}_changelist'),
            path('add/', self.admin_site.admin_view(self.add_view), name=f'{opts.app_label}_{opts.model_name}_add'),
            path('<str:note_id>/change/', self.admin_site.admin_view(self.change_view), name=f'{opts.app_label}_{opts.model_name}_change'),
            path('<str:note_id>/delete/', self.admin_site.admin_view(self.delete_view), name=f'{opts.app_label}_{opts.model_name}_delete'),
        ]
        return custom_urls

    def has_module_permission(self, request):
        return request.user.is_staff

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

    def _get_note(self, note_id):
        try:
            item = collection().find_one({'_id': ObjectId(note_id)})
        except Exception as exc:
            raise Http404('Invalid note ID') from exc
        if not item:
            raise Http404('Student note not found')
        item['id'] = str(item.pop('_id'))
        return item

    def changelist_view(self, request, extra_context=None):
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
        page_obj = Paginator(items, 25).get_page(request.GET.get('page'))
        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'title': 'Student Notes (MongoDB)',
            'items': page_obj,
            'page_obj': page_obj,
            'query': query,
            'add_url': reverse('admin:notes_mongonote_add'),
        }
        return TemplateResponse(request, 'admin/notes/mongonote/change_list.html', context)

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':
            student_id = request.POST.get('student_id', '').strip()
            note = request.POST.get('note', '').strip()
            if student_id and note:
                now = datetime.now(timezone.utc)
                collection().insert_one({
                    'student_id': student_id,
                    'note': note,
                    'created_at': now,
                    'updated_at': now,
                })
                self.message_user(request, 'Student note added successfully.', messages.SUCCESS)
                return redirect('admin:notes_mongonote_changelist')
            self.message_user(request, 'Student ID and note are required.', messages.ERROR)
        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'title': 'Add Student Note',
            'item': None,
            'is_popup': False,
            'save_as': False,
            'has_view_permission': True,
            'has_add_permission': True,
            'has_change_permission': True,
            'has_delete_permission': True,
        }
        return TemplateResponse(request, 'admin/notes/mongonote/change_form.html', context)

    def change_view(self, request, note_id, form_url='', extra_context=None):
        item = self._get_note(note_id)
        if request.method == 'POST':
            student_id = request.POST.get('student_id', '').strip()
            note = request.POST.get('note', '').strip()
            if student_id and note:
                collection().update_one(
                    {'_id': ObjectId(note_id)},
                    {'$set': {
                        'student_id': student_id,
                        'note': note,
                        'updated_at': datetime.now(timezone.utc),
                    }},
                )
                self.message_user(request, 'Student note updated successfully.', messages.SUCCESS)
                return redirect('admin:notes_mongonote_changelist')
            self.message_user(request, 'Student ID and note are required.', messages.ERROR)
        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'title': 'Edit Student Note',
            'item': item,
            'original': item,
            'is_popup': False,
            'save_as': False,
            'has_view_permission': True,
            'has_add_permission': True,
            'has_change_permission': True,
            'has_delete_permission': True,
            'delete_url': reverse('admin:notes_mongonote_delete', args=[note_id]),
        }
        return TemplateResponse(request, 'admin/notes/mongonote/change_form.html', context)

    def delete_view(self, request, note_id, extra_context=None):
        item = self._get_note(note_id)
        if request.method == 'POST':
            collection().delete_one({'_id': ObjectId(note_id)})
            self.message_user(request, 'Student note deleted successfully.', messages.SUCCESS)
            return redirect('admin:notes_mongonote_changelist')
        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'title': 'Delete Student Note',
            'item': item,
            'object': item,
        }
        return TemplateResponse(request, 'admin/notes/mongonote/delete_confirmation.html', context)


admin.site.site_header = 'Student Management Administration'
admin.site.site_title = 'StudentMS Admin'
admin.site.index_title = 'Manage Students, Courses, Notes and Users'

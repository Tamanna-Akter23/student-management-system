from django.urls import path
from . import views
urlpatterns=[path('',views.note_list,name='note_list'),path('add/',views.note_create,name='note_add'),path('<str:note_id>/edit/',views.note_update,name='note_edit'),path('<str:note_id>/delete/',views.note_delete,name='note_delete')]

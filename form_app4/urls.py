from django.urls import path

from form_app4 import views

app_name = 'form_app4'

urlpatterns = [
    path('create/', views.create_task_view, name='task_name'),
    path('list/', views.task_list_view, name='task_list_view')
]
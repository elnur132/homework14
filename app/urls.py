from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', show_task, name='show-tasks'),
    path('add-task', add_task, name='add-task'),
    path('update/<int:id>/', update_task, name='update-task'),
    path('delete/<int:id>/', delete_task, name='delete-task')
]

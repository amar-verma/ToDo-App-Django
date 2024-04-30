from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ToDo,name='ToDo'),
    path('home/', views.home,name='home'),
    path('complete/', views.complete,name='complete'),
    path('pending/', views.pending,name='pending'),
    path('create_a_list/', views.createToDo,name='create'),
    path('delete/<str:task_id>', views.delete,name='delete'), #it's not delete its details
    path('task_complete/<str:task_id>', views.task_complete,name='task_complete'),
    path('task_delete/<str:task_id>',views.task_delete,name='task_delete')
]
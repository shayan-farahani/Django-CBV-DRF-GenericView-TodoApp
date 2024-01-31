from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.TaskListApi.as_view(), name='task-list'),
    path('<int:pk>', views.TaskDetailApi.as_view(), name='task-detail')
    
]
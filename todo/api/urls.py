from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.TaskListCreateAPIView.as_view(), name='task-list'),
    path('<int:pk>', views.TaskDetailRetrieveUpdateDestroyAPIView.as_view(), name='task-detail')
    
]
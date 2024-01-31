from django.urls import path, include
from . import views
app_name = 'todo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api', include('todo.api.urls'))
]
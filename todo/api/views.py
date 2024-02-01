from rest_framework import generics
from ..models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status



class TaskListGenericsApiView(generics.GenericAPIView):
    '''
    create and retrieve model instance
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)# 1 < object == many=True
        return Response(serializer.data)


    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class TaskDetailGenericsApiView(generics.GenericAPIView):
    '''
    delete and retrieve  and update model instance
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({'detail':'Cleared successfully'})

        
# mixins

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


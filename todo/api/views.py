from rest_framework import generics
from ..models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status


class TaskListApi(generics.GenericAPIView):
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailApi(generics.GenericAPIView):
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
        serializer = self.serializer_class(data=request.data, status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object().delete()
        return Response({'detail':'Cleared successfully'}, status=status.HTTP_204_NO_CONTENT)

        

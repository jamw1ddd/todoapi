from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskViewSet(viewsets.ViewSet):
    def list(self,request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data,200)

    def create(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'error':serializer.errors},400)
        
        return Response(serializer.data,201)

    

class ListTodoView(APIView):
    def get(self,request,format=None):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data,200)
    
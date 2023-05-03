from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from base.models import Task, User, Mark
from .serializers import TaskSerializer, UserSerialaizer, MarkSerialaizer
from rest_framework import permissions


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/tasks',
        'GET /api/tasks/:id',
        'POST /api/create-task',
        'POST /api/update-task/:id',
        'DELETE /api/delete-task/:id',
        'GET /api/marks',
        'GET /api/marks/:id',
        'POST /api/create-mark',
        'POST /api/update-mark/:id',
        'DELETE /api/delete-mark/:id',
        'POST /api/api-auth',
        'POST /api/api/token',
        'POST /api/api/token/refresh',
        'GET /api/user',
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createTask(request):
    if request.user.creator:
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('This user not authorized to CRUD')

@api_view(['POST'])
@permission_classes((permissions.AllowAny))
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.user.creator:
        serializer = TaskSerializer(data = request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('This user not authorized to CRUD')


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.user.creator:
        task.delete()
        return Response('Task deleted')
    else:
        return Response('This user not authorized to CRUD')


class UserViews(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerialaizer
    queryset = User.objects.all()

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getMarks(request):
    marks = Mark.objects.all()
    serilizer = MarkSerialaizer(marks, many = True)
    return Response(serilizer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getMark(request, pk):
    mark = Mark.objects.get(id=pk)
    serilizer = MarkSerialaizer(mark, many = False)
    return Response(serilizer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createMark(request):
    if request.user.completer:
        # if request.data.get('task') == mark.task and request.data.get('user') == mark.user:
        #    return Response('Same task and user for a mark')
        serializer = MarkSerialaizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('This user not authorized to add Marks')
    

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def updateMark(request, pk): # only mark and user are changeable
    mark = Mark.objects.get(id=pk)
    if request.user.completer:
        serializer = MarkSerialaizer(data = request.data, instance=mark)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('This user not authorized to add Marks')
    

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def deleteMark(request, pk):
    mark = Mark.objects.get(id=pk)
    
    if request.user.completer:
        mark.delete()
        return Response('Task deleted')
    else:
        return Response('This user not authorized to CRUD')
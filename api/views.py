from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  TaskSerializer
from .models import  Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
        'Registration': '/auth/users/',
        'Login': '/auth-token/token/login/',
        'Logout': '/auth-token/token/logout/'

    }
    return Response(api_urls)
@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serielizer = TaskSerializer(task, many=True)
    return Response(serielizer.data)



@api_view(['POST'])
def TaskCreate(request):
    
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item was delete')


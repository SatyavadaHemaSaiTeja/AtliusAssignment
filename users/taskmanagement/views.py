from django.shortcuts import render
from rest_framework import viewsets, status
from .models import CustomUser, Task
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, TaskSerializer, UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    queryset= CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes= [IsAuthenticated]

class TaskViewSet(viewsets.ViewSet):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= [IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filter_class = TaskFilter

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def perform_update(self,serializer):
        serializer.save(updated_by=self.request.user)

@api_view(['POST'])
def user_registration(request):
    if request.method=='POST':
        serializer =UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def uplaod_profile_pic(request):
    if 'image' not in request.FILES:
        return Response({'error':'No Image'}, status=status.HTTP_400_BAD_REQUEST)
    image = request.FILES['image']
    userid= request.user
    try:
        s3_client.upload_fileobj(image,settings.AWS_S3_BUCKET_NAME,f"profilepics/{userid}/{image.name}.jpg")

    except:
        pass

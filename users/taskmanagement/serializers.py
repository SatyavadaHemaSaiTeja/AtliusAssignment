from rest_framework import serializers
from .models import CustomUser, Task, ProfilePicture

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ['id','username','email']
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        read_only=['created_by','created_on','updated_by','updated_on']
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model= CustomUser
        fields =['id','username','email','password']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ProfilePicSerializer(serializers.ModelSerializer):
    class meta:
        model=ProfilePicture
        read_only=['uploaded_at']
        fields='__all__'

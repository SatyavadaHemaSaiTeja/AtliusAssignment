from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass


class Task(models.Model):
    status_choices =[
        ('TODO','To Do'),
        ('IN_PROGRESS','IN Progress'),
        ('COMPLETED', 'Completed')
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser,related_name='tasks_assigned',null=True,blank=True, on_delete= models.CASCADE)
    created_by = models.ForeignKey(CustomUser,related_name='tasks_created', on_delete= models.CASCADE)
    status = models.CharField(max_length=20, choices=status_choices,default='TODO')
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on =models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser,related_name='tasks_updated',null=True,blank=True, on_delete= models.CASCADE)
    def __str__(self):
        return self.title
    

class ProfilePicture(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Profile Pic of {self.user.username}"
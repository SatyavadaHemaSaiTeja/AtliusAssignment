from django.contrib import admin
from .models import CustomUser,Task

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('username','email','is_staff','is_active')
    search_fields=('username','email')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter=('status','created_by','assigned_to','created_on')
    search_fields= ('title','description')
    date_hierarchy='created_on'

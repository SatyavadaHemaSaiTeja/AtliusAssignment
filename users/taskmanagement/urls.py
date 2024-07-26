from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet, user_registration, uplaod_profile_pic
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'tasks',TaskViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='taken_refresh'),
    path('register/',user_registration,name='user_registration'),
    path('uploadprofilepic/',uplaod_profile_pic, name =' upload')
]
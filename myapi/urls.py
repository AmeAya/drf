from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todo-api/', TodoListApiView.as_view(), name='todo'),
    path('api-auth/', include('rest_framework.urls')),
]

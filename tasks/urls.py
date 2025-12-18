from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls

urlpatterns = [
    path('', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
]

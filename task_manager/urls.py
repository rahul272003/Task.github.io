from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
def home(request):
    return HttpResponse("Task Manager API is running")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/auth/', include('accounts.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('api/tasks/', include('tasks.urls')),
]


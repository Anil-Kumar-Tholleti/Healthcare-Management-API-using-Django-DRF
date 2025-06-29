from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Healthcare API. Use /api/ to access the API endpoints."})

urlpatterns = [
    path('', home),  # This will catch the root URL
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

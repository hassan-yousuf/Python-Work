from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secondapp/',include('secondapp.urls')),
    path('admin/', admin.site.urls),
]

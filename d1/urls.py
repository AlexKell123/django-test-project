from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def show_index(request):
    return render(request, 'wall/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    path('wall/', include('wall.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

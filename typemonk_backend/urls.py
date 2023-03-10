"""typemonk_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('admin/', admin.site.urls),
    path('api/',include("typemonk.urls")),  
]
'''
curl -X POST -d "grant_type=password&username=Typemonk&password=Typemonk&client_id=TypeMonk&client_secret=pbkdf2_sha256$320000$7xvyYBJfFcQN8f1539D4JT$LsrNJbgfB6FJgtxADlhzEMEALDt0KHIFK3RUIedZo+k=" http://http://localhost:8000//o/token/

'''

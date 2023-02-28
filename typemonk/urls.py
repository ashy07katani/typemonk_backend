from django.urls import path,include
from . import views
urlpatterns = [
    
    path("tests",views.getAllTests),
    path("tests_specific_time",views.getSpecificTimeAllTests),
    path("users",views.getAllUser),
    path("user/tests",views.getUserTests),
    path("user/tests_specific_time",views.getUserSpecificTimeTests),
    path("auth/user",views.getOauth),
    path("register/user",views.registerUser)
]

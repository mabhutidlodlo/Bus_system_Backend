from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from . import views
urlpatterns = [
    path('signup/', views.Signup.as_view())

    ]

from django.urls import path,include
from . import views
urlpatterns =[
    path('',views.register),
    path('sign-in',views.login),
    path('sign-out',views.logout),
]
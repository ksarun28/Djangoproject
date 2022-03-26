from . import views
from django.urls import path

urlpatterns = [
    
    path('home',views.index,name='home'),
    path('',views.fun,name='index')
]

from django.urls import path
from . import views

#TEMPLATE URLS
app_name = 'app'

urlpatterns = [
    path('register/', views.register, name='register'),
]
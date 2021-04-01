from django.urls import path
from . import views

urlpatterns = [
    path('', views.teanews_home, name='teanews_home'),

]

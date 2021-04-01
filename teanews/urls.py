from django.urls import path
from . import views

urlpatterns = [
    path('', views.teanews_home, name='teanews_home'),
    path('create_text', views.create_text, name='create_text'),
    path('/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),

]

from this import d
from zlib import decompressobj
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
    path('create-post/',views.createPost,name='create-post'),
    path('<int:id>/', views.detail_view, name='photos')
    
]


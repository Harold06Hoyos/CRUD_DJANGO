from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('we', views.we, name="we"),
    path('libros', views.libros, name='libros'),
]
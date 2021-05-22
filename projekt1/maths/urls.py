from django.urls import path

from . import views

urlpatterns = [
    path('', views.div, name='div'),
    path('', views.mul, name='mul'),
    path('', views.add, name='add'),
    path('', views.sub, name='sub'),
]

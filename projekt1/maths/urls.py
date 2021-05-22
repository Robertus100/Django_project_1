from django.urls import path

from . import views

urlpatterns = [
    path('div/<int:x>/<int:y>', views.div, name='div'),
    path('', views.mul, name='mul'),
    path('<x>/<y>/', views.add, name='add'),
    path('', views.sub, name='sub'),
]

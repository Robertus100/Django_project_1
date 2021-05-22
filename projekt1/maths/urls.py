from django.urls import path

from . import views

urlpatterns = [
    path('div/<int:x>/<int:y>', views.div, name='div'),
    path('mul/<int:x>/<int:y>', views.mul, name='mul'),
    path('add/<int:x>/<int:y>', views.add, name='add'),
    path('sub/<int:x>/<int:y>', views.sub, name='sub'),
]

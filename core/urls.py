from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('carros', views.carros, name='carros'),
    path('agendar-servico', views.agendar_servico, name='agendar_servico'),
    path('carro/<int:id>', views.carro, name='carro'),
    path('contato', views.contato, name='contato'),
]


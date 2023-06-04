from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('rutinas/', views.rutinas, name = 'rutina'),
    path('iniciosesion/', views.iniciosesion, name = 'iniciosesion'),
    path('crearcuenta/', views.crearcuenta, name = 'crearcuenta'),
    path('quienessomos/', views.quienessomos, name = 'quienessomos')
]
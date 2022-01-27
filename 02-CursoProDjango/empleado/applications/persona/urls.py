from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

# permite llamar desde una vista mas rapido con el paquete lazy
app_name = "persona_app"

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<shorname>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/',
         views.EmpleadoUpdateView.as_view(),
         name='modificar_empleado'),
    path('delete-empleado/<pk>/',
         views.EmpleadoDeleteView.as_view(),
         name='modificar_empleado'),
]

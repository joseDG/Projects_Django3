
from django.contrib import admin
# inclucion de 2 paquetes re_path include
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluimos las urls de la app departamento
    re_path('', include('applications.departamento.urls')),
    # incluimos las urls de la app home
    re_path('', include('applications.home.urls')),
    # incluimos las urls de la app persona
    re_path('', include('applications.persona.urls')),
]

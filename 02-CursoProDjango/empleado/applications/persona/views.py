from dataclasses import fields
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import Empleado, Habilidades
# Create your views here.
# Trabajando con una lista generica ListView

# 1.- Lista todos los empelados de la empresa


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    model = Empleado

# 2.- Listar todos los empelados qeu pertenecen a una area de la empresa
# la peor forma de hacer filtros


class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        # el codigo que yo queria
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

# 3.- Listar empleados por trabajo

# 4.- Listar los empleados por palabra clave


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*******************')
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

# 5.- Listar habilidades de un empleado


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        return empleado.habilidades.all()

# Integracion de Vista generica DetailView
# Utilizacion de un pk es decir un ID


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"

# Vista generica CreateView para crear un nuevo registro de base de datos


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    # fields = ('__all__') muestra todos los datos
    # success_url = '.'  # redireccioana cunado todo se completa
    # success_url = '/success'  # redireccioana la pagina
    # redireccioana la pagina
    success_url = reverse_lazy('persona_app:correcto')

    # esta es la parte de instersectar antes de guardar un registro
    # Son procesos extras | permite validar datos
    def form_valid(self, form):
        # Logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

# Vista Generica UpdateView


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*********METHOD POST***********')
        print('==========================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('***********METHOD form calida*******')
        print('*********************************')
        return super(EmpleadoUpdateView, self).form_valid(form)

# Vista DeleteView Elimnar el Template


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')

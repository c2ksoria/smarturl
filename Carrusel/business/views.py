from queue import Empty
# from re import I
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, DeleteView
from django.shortcuts import render, HttpResponse, redirect
# from requests import request

from .models import Empresa, Campana, Multimedia, Paquete, Data
from .form import UpdateFormCampana, UpdateFormMultimedia, CreateFormCampana, CreateFormMultimedia
from urllib.parse import urlparse
from django.urls import resolve
from django.urls import reverse_lazy
from Carrusel.views import error_404
from django.http import Http404
from django.db.models import Q
# Create your views here.

def home1(request, id):
    try:
        campana=Campana.objects.get(url=id)
        temporizado= campana.Temporizado
    except:
        raise Http404()
    print(campana.estado)
    if (campana.estado_id==1):
        print("Campaña Activa!!")
        try:
            multimedia=Multimedia.objects.all().filter(capana_id = campana, estado_id=1)
            for item in multimedia:
                print(item)
            print("EXISTEEEEE")

        except:
            print("NO EXISTEEE")
            raise Http404()
    else:
        print("Campaña Suspendida!!!")
        data=Data.objects.all()
        multimedia=data    
    print("----------FIN!!!----------")
    return render(request, 'carrousel.html', {'multimedia': multimedia, 'temporizado': temporizado})


def home(request):
    return render(request,'home.html')

class EmpresaView(ListView):
    model=Empresa
    template_name: 'empresa.html'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)
        queryset=queryset.filter(Usuario=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Datos de la empresa'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print(context)
        return context

class CampanaView(ListView):
    model=Campana
    template_name: 'campana.html'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        queryset = queryset.filter(empresa=empresa_nombre.id)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Campañas Activas'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print("------------------")
        paqueteContratado=empresa_nombre.PaqueteContratado
        campanaContratadas=Campana.objects.filter(empresa=empresa_nombre).count()
        campanaDisponibles=paqueteContratado.CantCampana-campanaContratadas
        context['campanaDisponibles']= campanaDisponibles

        return context

class UpdateCampanaView(UpdateView):
    model=Campana
    form_class = UpdateFormCampana
    success_url ="/campana"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Datos de Campaña'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print(context)
        return context

def multimedia(request, pk):
        print("esto es un dato", pk)
        return HttpResponse(request, {'data': 'holas'})

class MultimediaView(ListView):
    model=Multimedia
    template_name: 'multimedia.html'
    success_url = reverse_lazy('createMultimedia')
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)
        get_id=Get_Id_Empresa(self.request)

        try:
            campana=Campana.objects.get(pk=get_id)
            multimedia=Multimedia.objects.all()
            multi=multimedia.filter(capana_id=get_id)
            return multi
        except:
            raise Http404()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Multimedia'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        paqueteContratado=empresa_nombre.PaqueteContratado
        get_id=Get_Id_Empresa(self.request)
        CantidadMultimedia=Multimedia.objects.filter(capana=get_id).count()
        # print(CantidadMultimedia)
        multimediaDisponible= paqueteContratado.CantFoto-CantidadMultimedia
        # print(multimediaDisponible)
        context['multimediaDisponibles']= multimediaDisponible
        return context

def Get_Id_Empresa(request):
        # print(request.user)
        current_url = request.path_info
        # print(current_url)
        # print(current_url.split('/'))
        all_path=current_url.split('/')
        get_id=all_path[2]
        # print(get_id)
        return get_id

class MultimediaUpdateView(UpdateView):
    model=Multimedia
    form_class = UpdateFormMultimedia
    success_url ="/campana"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Datos Multimedia'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print(context)
        return context

class CreateCampanaView(CreateView):
    model=Campana
    form_class= CreateFormCampana
    template_name= 'createCampana.html'
    success_url=reverse_lazy('campana')
    
    def form_valid(self, form):
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        form.instance.empresa = empresa_nombre
        form.save()
        current_url = self.request
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']= 'Creación de Nueva Campaña'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print(context)
        return context
    

class CreateMultimediaView(CreateView):
    model=Multimedia
    form_class= CreateFormMultimedia
    template_name= 'createMultimedia.html'
   
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('multimedia', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']= 'Creación de Multimedia'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print(context)
        return context
    
    def form_valid(self, form):
        id_Campana=self.kwargs['pk']
        campana=Campana.objects.get(id=id_Campana)
        form.instance.capana = campana
        form.save()
        current_url = self.request
        return super().form_valid(form)

class DeleteCampanaView(DeleteView):
    model = Campana
    success_url = reverse_lazy('campana')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        return context

class DeleteMultimediaView(DeleteView):
    model = Multimedia
    success_url = reverse_lazy('campana')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        return context

class PaqueteViewAdmin(ListView):
    model= Paquete
    template_name: 'paquete.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        planContratado=empresa_nombre.PaqueteContratado
        context['plan']=planContratado
        context['titulo']= "Planes Disponibles"
        print("Plan Contratado............",planContratado)
        return context



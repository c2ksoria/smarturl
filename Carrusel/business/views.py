from queue import Empty
# from re import I
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, DeleteView
from django.shortcuts import render, HttpResponse
# from requests import request

from .models import Empresa, Campana, Multimedia, Paquete
from .form import UpdateFormCampana, UpdateFormMultimedia, CreateFormCampana, CreateFormMultimedia
from urllib.parse import urlparse
from django.urls import resolve
from django.urls import reverse_lazy
# Create your views here.

def home1(request, id):
    print("++++++++++++++++")
    print(id)
    
    campana1=Campana.objects.all().get(url=id)
    print(campana1.Temporizado)
    campana=campana1
    temporizado= campana.Temporizado
    print("++++++++++++++++")
    # print(campana1)
    # print(campana.url)
    # print(campana.Temporizado)
    # print(campana.empresa)
    # for item in campana:
    #     print(item)
    multimedia=Multimedia.objects.filter(capana=campana1)
    # print(multimedia)
    # for item in multimedia:
    #     print(item)
    print("++++++++++++++++")
    # print(type(campana1))
    # print(temporizado)
    print("++++++++++++++++")
    return render(request, 'carrousel.html', {'multimedia':multimedia, 'temporizado': temporizado})

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
        # print(empresa_nombre.id)
        # print(type(empresa_nombre))
        # print("-------------")
        # Filtrado por empresa!
        queryset = queryset.filter(empresa=empresa_nombre.id)
        # print("-------------")

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Campañas Activas'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        print("------------------")
        paqueteContratado=empresa_nombre.PaqueteContratado
        # print(paqueteContratado.CantCampana)
        # print("------------------")
        campanaContratadas=Campana.objects.filter(empresa=empresa_nombre).count()
        # print(campanaContratadas)
        campanaDisponibles=paqueteContratado.CantCampana-campanaContratadas
        # print(campanaDisponibles)
        context['campanaDisponibles']= campanaDisponibles

        return context

class UpdateCampanaView(UpdateView):
    model=Campana
    form_class = UpdateFormCampana
    # template_name: 'campana.html'
    # fields = [
    #     "estado",
    #     "NombreCampana",
    #     "Temporizado",
    #     "url"
    # ]
    success_url ="/campana"
    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     empresa_usuario = Empresa.objects.filter(usuario=user)
    #     print(empresa_usuario)
    #     queryset = super().get_queryset(*args, **kwargs)
    #     # queryset=queryset.filter(empresa=Campana.empresa)
    #     return queryset
    
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
            print("si existe.......------")
            multimedia=Multimedia.objects.all()
            multi=multimedia.filter(capana_id=get_id)
            # for items in multi.iterator():
            #     print(items)
            return multi
            print("------------------")
        except:
            print("no existe..----------")
            multimedia1=Multimedia.objects.filter(pk=0)
            # context = super().get_context_data(**kwargs)
            # context['titulo1'] = 'eroorrrorro!!!'
            return multimedia1
        
        
        # user = self.request.user
        # if (empresa_nombre=Empresa.objects.get(Usuario=user.id)
        # print(type(queryset))
        # print("------------------")
        # print(queryset)

        # multimedia=multimedia.objects.filter(id=3)
        # ().filter(pk=get_id)
        # .filter(pk=get_id).filter(capana=campana)
        # print(campana[0].NombreCampana)
        

       
        # if (multimedia.exists()):
        #     print("hacer todo lo actual")
            
            
        #     # for items in queryset:
        #     #     print(items.capana)
        #     return multimedia
        # else:
        #     print("enviar un mensaje que no existe la campaña ")
        #     return queryset
        # print(empresa_nombre.id)
        # print(type(empresa_nombre))
        # print("-------------")
        # Filtrado por empresa!
        # queryset = queryset.filter(empresa=empresa_nombre.id)

        # print("-------------")
        # print(queryset)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Multimedia'
        user = self.request.user
        empresa_nombre=Empresa.objects.get(Usuario=user.id)
        context['empresa']= empresa_nombre.NombreEmpresa
        
        paqueteContratado=empresa_nombre.PaqueteContratado

        get_id=Get_Id_Empresa(self.request)
        CantidadMultimedia=Multimedia.objects.filter(capana=get_id).count()
        print(CantidadMultimedia)
        multimediaDisponible= paqueteContratado.CantFoto-CantidadMultimedia
        print(multimediaDisponible)
        context['multimediaDisponibles']= multimediaDisponible
        return context

def Get_Id_Empresa(request):
        print(request.user)
        current_url = request.path_info
        print(current_url)
        print(current_url.split('/'))
        all_path=current_url.split('/')
        get_id=all_path[2]
        print(get_id)
        return get_id

class MultimediaUpdateView(UpdateView):
    model=Multimedia
    form_class = UpdateFormMultimedia
    # template_name: 'campana.html'
    # fields = [
    #     "estado",
    #     "NombreCampana",
    #     "Temporizado",
    #     "url"
    # ]
    success_url ="/campana"
    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     empresa_usuario = Empresa.objects.filter(usuario=user)
    #     print(empresa_usuario)
    #     queryset = super().get_queryset(*args, **kwargs)
    #     # queryset=queryset.filter(empresa=Campana.empresa)
    #     return queryset
    
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

        # print("-------------current_url--------------")
        # print(id_Campana)
        # print(current_url)
        # print("---------------------------------------")
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
    # success_url=reverse_lazy('campana')

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
    
    # def get_form_kwargs(self):
    #     kwargs = super(CreateMultimediaView, self).get_form_kwargs()
    #     kwargs['capana']=2
    #     print("------get form kwargs------")
    #     print(kwargs)
    #     print("---------------------------")
    #     return kwargs

    def form_valid(self, form):
        id_Campana=self.kwargs['pk']
        # user = self.request.user
        # empresa_nombre=Empresa.objects.get(Usuario=user.id)
        # campana=Campana.objects.get(NombreCampana='Pantalla Av. Libertador1')
        campana=Campana.objects.get(id=id_Campana)
        form.instance.capana = campana
        form.save()

        current_url = self.request

        # print("-------------current_url--------------")
        # print(id_Campana)
        # print(current_url)
        # print("---------------------------------------")
        return super().form_valid(form)


    # def post(self,request,*args, **kwargs):
    #     form = self.get_form()
    #     print("---------FORM----------")
    #     print(form)
    #     print("---------------------------")
    #     return HttpResponseRedirect(self.get_success_url())

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
    
def error_404_view(request, exception):
    print("error 404-------")
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')
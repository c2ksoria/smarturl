from django.contrib import admin
from django.urls import path, include

from business.form import CreateFormMultimedia
from .views import CreateMultimediaView, PaqueteViewAdmin, UpdateCampanaView, CampanaView, EmpresaView, home, multimedia, MultimediaView, MultimediaUpdateView, CreateCampanaView, DeleteCampanaView, DeleteMultimediaView, home, error_404_view

urlpatterns = [
    # path('publi/<str:id>', home, name='home'),
    # path('carrousel/', CarrouselView.as_view(),name='carrouselView'),
    path('',home,name='home'),
    path('empresa/', EmpresaView.as_view(),name='empresa'),
    path('campana/', CampanaView.as_view(),name='campana'),
    path('campana/<slug:pk>/', UpdateCampanaView.as_view(),name='updateCampana'),
    path('campana/<slug:pk>/multimedia', MultimediaView.as_view(),name='multimedia'),
    path('campana/<slug:pk>/multimedia/add', CreateMultimediaView.as_view(), name='createMultimedia'),
    path('campana/add', CreateCampanaView.as_view(), name='createcampana'),
    path('campana/delete/<slug:pk>/', DeleteCampanaView.as_view(), name='deletecampana'),
    path('multimedia/<slug:pk>/', MultimediaUpdateView.as_view(),name='updateMultimedia'),
    path('multimedia/delete/<slug:pk>/', DeleteMultimediaView.as_view(),name='deleteMultimedia'),
    path('plan/', PaqueteViewAdmin.as_view(),name='paquete'),

]

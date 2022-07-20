from django.contrib import admin
from .models import *

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    list_display=('id','NombreEmpresa','DireccionEmpresa','CuitEmpresa', 'FechaIngreso', 'HoraIngreso','estado','Usuario')
    search_fields=('NombreEmpresa','CuitEmpresa')
    list_filter = ('NombreEmpresa','CuitEmpresa')
class CampanaAdmin(admin.ModelAdmin):
    # readonly_fields=('FechaCreacion', 'HoraCreacion')
    list_display=('id','NombreCampana', 'FechaCreacion','empresa','Temporizado', 'url')
    list_filter=('NombreCampana','empresa')
class MultimediaAdmin(admin.ModelAdmin):
    list_display=('id','NombreMultimedia','estado','capana')
    # list_filter=('NombreCampana','empresa')

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Campana, CampanaAdmin)
admin.site.register(Estado)
admin.site.register(Multimedia, MultimediaAdmin)
admin.site.register(Paquete)


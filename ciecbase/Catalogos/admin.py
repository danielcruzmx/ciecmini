import csv
from django.http import HttpResponse
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from Catalogos.models import TipoMovimiento, Situacion,     \
                             Banco, Condominio, Proveedore, \
                             PeriodoCorte, TipoDocumento

class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class SituacionAdmin(admin.ModelAdmin):
    list_display = ('situacion',)

class BancoAdmin(admin.ModelAdmin):
    list_display = ('clave','descripcion')

class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProveedoreAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'rfc', 'domicilio')

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('condominio', 'fecha_inicial', 'fecha_final')


admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(Banco, BancoAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Proveedore, ProveedoreAdmin)
admin.site.register(PeriodoCorte, PeriodoAdmin)



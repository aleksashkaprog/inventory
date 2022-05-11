from django.contrib import admin
from inventory_bd.models import Thing, Responsible, General


class ThingAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'inv', 'price', 'count', 'summ', 'note', 'resp']


admin.site.register(Thing, ThingAdmin)


class ResponsibleAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Responsible, ResponsibleAdmin)


class GeneralAdmin(admin.ModelAdmin):
    list_display = ['people', 'product']


admin.site.register(General, GeneralAdmin)

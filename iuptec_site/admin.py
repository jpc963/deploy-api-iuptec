from django.contrib import admin
from .models import Veiculos


class ListaVeiculos(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano', 'placa', 'cor', 'pessoa')
    list_display_links = ('modelo',)
    search_fields = ('modelo',)
    list_per_page = 10


admin.site.register(Veiculos, ListaVeiculos)
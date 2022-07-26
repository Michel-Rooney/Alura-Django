from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo')
    list_display_links = ('id', 'nome_receita')

    # Um campo de procura
    search_fields = ('nome_receita',)

    # Filtro
    list_filter = ('categoria',)

    # Quantas informações por página
    list_per_page = 10

admin.site.register(Receita, ListandoReceitas)
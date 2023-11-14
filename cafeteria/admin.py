from django.contrib import admin
from cafeteria.models import Produto

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "denominacao", "categoria", "legenda", "publicada")
    list_editable = ("publicada",)
    list_display_links = ("id", "denominacao")
    search_fields = ("id", "denominacao")
    list_filter = ("categoria", )
    list_per_page = 10

admin.site.register(Produto, ListandoProdutos)
from django.contrib import admin
from cafeteria.models import Produto

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "denominacao", "categoria", "legenda")
    list_display_links = ("id", "denominacao")
    search_fields = ("id", "denominacao")
    list_filter = ("categoria", )

admin.site.register(Produto, ListandoProdutos)
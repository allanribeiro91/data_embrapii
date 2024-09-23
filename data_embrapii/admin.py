from django.contrib import admin
from data_embrapii.models import Usuario, ProdutoInformacional

class ListandoUsuario(admin.ModelAdmin):
    list_display = ("cpf", "nome_completo", "usuario_is_ativo")
    list_display_links = ("cpf", "nome_completo")
    search_fields = ("cpf", "nome_completo")
    list_filter = ("usuario_is_ativo", )
    list_per_page = 100

class ListandoProdutoInformacional(admin.ModelAdmin):
    list_display = ("titulo", "tipo_produto", "data_criacao")
    list_display_links = ("titulo", "tipo_produto")
    search_fields = ("titulo",)
    list_filter = ("tipo_produto", )
    list_per_page = 100

admin.site.register(Usuario, ListandoUsuario)
admin.site.register(ProdutoInformacional, ListandoProdutoInformacional)
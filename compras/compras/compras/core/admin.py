from django.contrib import admin
from .models import ContatoFornecedor, Fornecedor

# Register your models here.
@admin.register(ContatoFornecedor)
class ContatoFornecedorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'contato', 'empresa', 'observacoes',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('forn_number', 'nome', 'observacoes',)
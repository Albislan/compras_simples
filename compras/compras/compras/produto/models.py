from django.db import models
from compras.core.models import Fornecedor
from django.urls import reverse

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca_produto = models.CharField("Marca:", max_length=30)
    forn_marca = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.marca_produto}"

    def get_absolute_url(self):
        return reverse("marca_update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("marca_delete", kwargs={"pk": self.id})

    class Meta:
        db_table = 'marca'
        ordering = ('marca_produto',)


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    estoq = models.IntegerField('estoque atual')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    observacoes = models.CharField(max_length=50)

    def __str__(self):
        return f"id({self.id}) {self.nome} {self.tipo} {self.marca} ({self.estoq} no estoque)"

    def get_absolute_url(self):
        return reverse("prod_update", kwargs={"pk": self.id})

    def get_delete_url(self):
        return reverse("prod_delete", kwargs={"pk": self.id})

    def to_dict_json(self):
        return {
            'pk': self.id,
            'produto': self.nome,
            'tipo': self.tipo,
            'marca': self.marca,
            'estoque': self.estoq,
            'preco': self.preco,
        }

    class Meta:
        db_table = 'produto'
        ordering = ('nome',)






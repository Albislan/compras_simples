from django.db import models
from django.urls import reverse

# Create your models here.
class Fornecedor(models.Model):
    forn_number = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    observacoes = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome}"

    def get_absolute_url(self):
        return reverse("forn_update", kwargs={"forn_number": self.forn_number})

    def get_delete_url(self):
        return reverse("forn_delete", kwargs={"forn_number": self.forn_number})

    class Meta:
        db_table = 'fornecedor'
        ordering = ('nome',)


class ContatoFornecedor(models.Model):
    contato = models.CharField('Nome do Contato', max_length=20)
    empresa = models.OneToOneField(Fornecedor, on_delete=models.CASCADE)
    observacoes = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.contato}"

    def get_absolute_url(self):
        return reverse("cont_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("cont_delete", kwargs={"pk": self.pk})

    class Meta:
        db_table = 'contatos'
        ordering = ('contato',)


class TimeStampedModel(models.Model):
    created = models.DateField('criado em', auto_now_add=True, auto_now=False)
    modified = models.DateField('modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True

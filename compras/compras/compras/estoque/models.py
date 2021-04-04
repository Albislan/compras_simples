from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from compras.core.models import Fornecedor, TimeStampedModel
from compras.produto.models import Produto

# Create your models here.
MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Código {} que {}ntrou na data de {}'.format(self.pk, self.movimento, self.created.strftime('%d-%m-%Y'))


class EstoqueEntradaManager(models.Manager):

    def get_queryset(self):
        return super(EstoqueEntradaManager, self).get_queryset().filter(movimento='e')


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)


class Compras(TimeStampedModel):
    cod_compra = models.AutoField(primary_key=True)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    forn = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    movimento = models.CharField(choices=MOVIMENTO, max_length=1, blank=True)
    valor = models.DecimalField('Valor R$:', decimal_places=2, max_digits=10)
    obs = models.CharField('Observações:', max_length=200)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.cod_compra, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} - {}'.format(self.cod_compra, self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'


    # def get_absolute_url(self):
    #     return reverse("compra_detail", kwargs={"pk": self.cod_compra})

    def get_delete_url(self):
        return reverse("compra_delete", kwargs={"pk": self.cod_compra})

    class Meta:
        db_table = 'compras'
        ordering = ('-created',)


class ComprasEntradaManager(models.Manager):
    def get_queryset(self):
        return super(ComprasEntradaManager, self).get_queryset().filter(movimento='e')


class ComprasEntrada(Compras):
    objects = ComprasEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'compra entrada'
        verbose_name_plural = 'compra entrada'


class ComprasItens(models.Model):
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE, related_name='comps')
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True)
    quant = models.PositiveIntegerField()
    sald = models.PositiveIntegerField('Saldo no Estoque', blank=True)
    preco_unit = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField('Valor Total dos Itens', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.pk, self.compra.pk, self.produtos, self.valor)


# class EstoqueSaidaManager(models.Manager):
#
#     def get_queryset(self):
#         return super(EstoqueSaidaManager, self).get_queryset().filter(movimento='s')

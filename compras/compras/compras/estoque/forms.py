from django import forms
from django.forms import inlineformset_factory

from .models import Compras, Estoque, EstoqueItens, ComprasItens


class EstoqueForm(forms.ModelForm):
    class Meta:

        model = Estoque
        fields = '__all__'


# class EstoqueEntradaForm(forms.ModelForm):
#     class Meta:
#
#         model = EstoqueEntrada
#         fields = '__all__'


class EstoqueItensForm(forms.ModelForm):
    class Meta:

        model = EstoqueItens
        fields = '__all__'

EstoqueItensFormSet = inlineformset_factory(Estoque, EstoqueItens, form=EstoqueItensForm)


class ComprasForm(forms.ModelForm):
    class Meta:

        model = Compras
        fields = ('nf', 'forn', 'valor', 'obs',)


class ComprasItensForm(forms.ModelForm):
    class Meta:

        model = ComprasItens
        fields = '__all__'

ComprasItensFormSet = inlineformset_factory(Compras, ComprasItens, form=ComprasItensForm)

PRODUCT_QUANTITY_CHOICES = [
    (i, str(i)) for i in range(1, 21)
]

class PedidoAddProdutoForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        label='Quantidade', choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
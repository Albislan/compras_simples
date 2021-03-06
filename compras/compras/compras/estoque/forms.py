from django import forms
from django.forms import inlineformset_factory
from .models import Compras, ComprasItens


# class EstoqueForm(forms.ModelForm):
#     class Meta:
#
#         model = Estoque
#         fields = '__all__'


# class EstoqueEntradaForm(forms.ModelForm):
#     class Meta:
#
#         model = EstoqueEntrada
#         fields = '__all__'

#
# class EstoqueItensForm(forms.ModelForm):
#     quantidade = forms.IntegerField(min_value=0, max_value=300)
#
#     class Meta:
#
#         model = EstoqueItens
#         fields = {
#             'estoque',
#             'produto',
#             'quantidade',
#             'saldo',
#         }
#
#
# EstoqueItensFormSet = inlineformset_factory(
#     Estoque, EstoqueItens, form=EstoqueItensForm,
#     can_delete=False, extra=0, min_num=1, validate_min=True
# )


class ComprasForm(forms.ModelForm):
    class Meta:

        model = Compras
        fields = ('nf', 'forn', 'valor', 'obs',)


class ComprasItensForm(forms.ModelForm):
    class Meta:

        model = ComprasItens
        fields = '__all__'


ComprasItensFormSet = inlineformset_factory(
    Compras, ComprasItens, form=ComprasItensForm,
    can_delete=False, extra=0, min_num=1, validate_min=True
)

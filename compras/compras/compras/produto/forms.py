from django import forms
from .models import Produto, Marca


class ProdutoForm(forms.ModelForm):
    class Meta:

        model = Produto
        exclude = ['data']


class MarcaForm(forms.ModelForm):
    class Meta:

        model = Marca
        fields = '__all__'

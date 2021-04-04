from django import forms
from .models import Fornecedor, ContatoFornecedor


class FornecForm(forms.ModelForm):
    class Meta:

        model = Fornecedor
        fields = '__all__'


class ContatoFornecedorForm(forms.ModelForm):
    class Meta:

        model = ContatoFornecedor
        fields = '__all__'


# class ArticleForm(ModelForm):
#     class Meta:
#         model = Article
#         fields = ['headline', 'content', 'reporter']
#
# class AuthorForm(ModelForm):
#     class Meta:
#
#         model = Author
#         fields = ['name', 'title', 'birth_date']
#
# class BookForm(ModelForm):
#     class Meta:
#
#         model = Book
#         fields = ['name', 'authors']
# ArticleFormSet = inlineformset_factory(Author, Article, form=ArticleForm)
# BookFormSet = inlineformset_factory(Author, Book, form=BookForm)

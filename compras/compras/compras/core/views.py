from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor, ContatoFornecedor
from .forms import FornecForm, ContatoFornecedorForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def pagina_inical(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou Senha Inválido. Tente Novamente. Persistindo o erro: Entre em contato com o suporte técnico pelo e-mail albislan@hotmail.com')
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')
0
class FornecedorListView(LoginRequiredMixin, ListView):
    template_name = 'fornecedor_list.html'
    paginate_by = 10
    model = Fornecedor
    login_url = '/login/'

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(Q(nome__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list


class FornecedorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'fornecedor.html'
    form_class = FornecForm
    login_url = '/login/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forn_list')


class FornecedorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'fornecedor.html'
    form_class = FornecForm
    login_url = '/login/'

    def get_object(self):
        forn_number = self.kwargs.get("forn_number")
        return get_object_or_404(Fornecedor, forn_number=forn_number)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forn_list')


class FornecedorDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    def get_object(self):
        forn_number = self.kwargs.get("forn_number")
        return get_object_or_404(Fornecedor, forn_number=forn_number)

    def get_success_url(self):
        return reverse("forn_list")


class ContatoListView(LoginRequiredMixin, ListView):
    template_name = 'contato_list.html'
    paginate_by = 10
    model = ContatoFornecedor
    login_url = '/login/'

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(Q(contato__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list


class ContatoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'contato.html'
    form_class = ContatoFornecedorForm
    login_url = '/login/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cont_list')

#Falta resolver o problema da atualização do contato
class ContatoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'contato.html'
    form_class = ContatoFornecedorForm
    login_url = '/login/'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(ContatoFornecedor, pk=pk)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cont_list')

#Falta resolver o problema de deletar o contato
class ContatoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(ContatoFornecedor, pk=pk)

    def get_success_url(self):
        return reverse("cont_list")

#teste article#

# class ArticleListView(ListView):
#     template_name = 'test_article_list.html'
#     model = Article
#
#
# class ArticleCreateView(CreateView):
#     template_name = 'test_article.html'
#     form_class = ArticleForm
#
#     def manage_books(self, request, author_id):
#         author = Author.objects.get(pk=author_id)
#         BookInLineFormSet = inlineformset_factory(Author, Article, fields=('reporter',))
#         if request.method == 'POST':
#             formset = BookInLineFormSet(request.POST, request.FILES, instance=author)
#             if formset.is_valid():
#                 formset.save()
#                 return HttpResponseRedirect(author.get_absolute_url())
#         else:
#             formset = BookInLineFormSet(instance=author)
#         return render(request, 'test_article.html', {'formset': formset})
#
# class AuthorListView(ListView):
#     template_name = 'test_author_list.html'
#     model = Author
#
#
# class AuthorCreateView(CreateView):
#     template_name = 'test_author.html'
#     form_class = AuthorForm
#
#     def get_context_data(self, **kwargs):
#         context = super(AuthorCreateView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             context['forms'] = AuthorForm(self.request.POST)
#             context['formset1'] = ArticleFormSet(self.request.POST)
#             context['formset2'] = BookFormSet(self.request.POST)
#         else:
#             context['forms'] = AuthorForm()
#             context['formset1'] = ArticleFormSet()
#             context['formset2'] = BookFormSet()
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         forms = context['forms']
#         formset1 = context['formset1']
#         formset2 = context['formset2']
#         if forms.is_valid() and formset1.is_valid() and formset2.is_valid():
#             self.object = form.save()
#             forms.instance = self.object
#             formset1.instance = self.object
#             formset2.instance = self.object
#             forms.save()
#             formset1.save()
#             formset2.save()
#             return redirect("author_list")
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
#
#     def get_success_url(self):
#         return reverse("author_list")
#
#
# class BookListView(ListView):
#     template_name = 'test_book_list.html'
#     model = Book
#
#
# class BookCreateView(CreateView):
#     template_name = 'test_book.html'
#     form_class = BookForm
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('book_list')

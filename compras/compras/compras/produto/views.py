from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Marca
from .forms import ProdutoForm, MarcaForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProdutoListView(LoginRequiredMixin, ListView):
    template_name = 'prod_list.html'
    paginate_by = 10
    model = Produto
    login_url = '/login/'

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(Q(nome__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'prod.html'
    form_class = ProdutoForm
    login_url = '/login/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('prod_list')


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'prod.html'
    form_class = ProdutoForm
    login_url = '/login/'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Produto, pk=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('prod_list')


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Produto, pk=id)

    def get_success_url(self):
        return reverse("prod_list")


def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})


class MarcaListView(LoginRequiredMixin, ListView):
    template_name = 'marca_list.html'
    paginate_by = 10
    model = Marca
    login_url = '/login/'

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(Q(nome__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list


class MarcaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'marca.html'
    form_class = MarcaForm
    login_url = '/login/'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marca_list')


class MarcaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'marca.html'
    form_class = MarcaForm
    login_url = '/login/'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Marca, pk=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marca_list')


class MarcaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Marca, pk=id)

    def get_success_url(self):
        return reverse("marca_list")

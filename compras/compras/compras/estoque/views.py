from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Estoque, EstoqueEntrada, Compras
from compras.produto.models import Produto
from .forms import ComprasForm, ComprasItensForm, EstoqueForm, EstoqueItensForm, EstoqueItensFormSet, ComprasItensFormSet
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ComprasListView(LoginRequiredMixin, ListView):
    template_name = 'compras_list.html'
    paginate_by = 10
    model = Compras
    login_url = '/login/'

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(Q(cliente__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super(ComprasListView, self).get_context_data(**kwargs)
        context['titulo'] = 'Entrada'
        context['url_add'] = 'compras_create'
        return context


def atualizar_estoque_compra(form):

    produtos = form.comps.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produtos.pk)
        produto.estoq = item.sald
        produto.save()
    print("Estoque atualizado com sucesso")

def compras_estoque_add(request, form_inline, template_name, movimento, url):
    compras_form = Compras()
    if request.method == 'POST':
        form = ComprasForm(request.POST, instance=compras_form, prefix='comp')
        formset = ComprasItensFormSet(request.POST, instance=compras_form, prefix='compras')
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.save()
            formset.save()
            atualizar_estoque_compra(form)
            return {'pk': form.pk}
    else:
        form = ComprasForm(instance=compras_form, prefix='comp')
        formset = ComprasItensFormSet(instance=compras_form, prefix='compras')
    context = {'form': form, 'formset': formset}
    return context

@login_required(login_url='/login/')
def compras_create(request):
    form_inline = ComprasItensForm
    template_name = 'compras.html'
    movimento = 'e'
    url = 'compra_detail'
    context = compras_estoque_add(request, form_inline, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)

class ComprasCreateView(LoginRequiredMixin, CreateView):
    template_name = 'compras.html'
    form_class = ComprasForm

    def get_context_data(self, **kwargs):
        context = super(ComprasCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['forms'] = ComprasForm(self.request.POST)
            context['formset'] = ComprasItensFormSet(self.request.POST)
        else:
            context['forms'] = ComprasForm()
            context['formset'] = ComprasItensFormSet()
        return context

    def atualizar_estoque_compra(self, form):

        produtos = form.comps.all()
        for item in produtos:
            produto = Produto.objects.get(pk=self.item.produtos.pk)
            produto.estoq = self.item.sald
            produto.save()
        print("Estoque atualizado com sucesso")

    def form_valid(self, form):
        context = self.get_context_data()
        forms = context['forms']
        formset = context['formset']
        if forms.is_valid() and formset.is_valid():
            self.object = form.save()
            forms.instance = self.object
            formset.instance = self.object
            forms.save()
            formset.save()
            self.atualizar_estoque_compra(forms)
            return {'pk': forms.pk}
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('compra_detail')


class ComprasDetailView(LoginRequiredMixin, DetailView):
    model = Compras
    template_name = 'compra_detail.html'
    login_url = '/login/'


def compras_detail(request, pk):
    template_name = 'compra_detail.html'
    obj = Compras.objects.get(pk=pk)
    context = {
        'object': obj,
        'url_list': 'compras_list'
    }
    return render(request, template_name, context)


class ComprasUpdateView(UpdateView):
    template_name = 'compras.html'
    form_class = ComprasForm

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Compras, pk=pk)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('compras_list')


class ComprasDeleteView(DeleteView):

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Compras, pk=pk)

    def get_success_url(self):
        return reverse("compras_list")


class EstoqueListView(LoginRequiredMixin, ListView):
    template_name = 'estoque_list.html'
    paginate_by = 10
    model = Estoque
    login_url = '/login/'

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            object_list = self.model.objects.filter(Q(item__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super(EstoqueListView, self).get_context_data(**kwargs)
        context['titulo'] = 'Entrada'
        context['url_add'] = 'estoque_create'
        return context


def atualizar_estoque(form):
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoq = item.saldo
        produto.save()
    print("Estoque atualizado com sucesso")

def estoque_add(request, form_inline, template_name, movimento, url):
    estoque_form = Estoque()
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = EstoqueItensFormSet(request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.save()
            formset.save()
            atualizar_estoque(form)
            return {'pk': form.pk}
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = EstoqueItensFormSet(instance=estoque_form, prefix='estoque')
    context = {'form': form, 'formset': formset}
    return context

@login_required(login_url='/login/')
def estoque_create(request):
    form_inline = EstoqueItensForm
    template_name = 'estoque.html'
    movimento = 'e'
    url = 'estoque_detail'
    context = estoque_add(request, form_inline, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)

class EstoqueDetailView(LoginRequiredMixin, DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'
    login_url = '/login/'

@login_required(login_url='/login/')
def estoque_entrada_detail(request, pk):
    template_name = 'estoque_detail.html'
    obj = EstoqueEntrada.objects.get(pk=pk)
    context = {
        'object': obj,
        'url_list': 'estoque_list'
    }
    return render(request, template_name, context)



# class EstoqueUpdateView(UpdateView):
#     template_name = 'estoque.html'
#     form_class = EstoqueForm
#
#     def get_object(self):
#         pk = self.kwargs.get("pk")
#         return get_object_or_404(Estoque, pk=pk)
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('estoque_list')


class EstoqueDeleteView(DeleteView):

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Estoque, pk=pk)

    def get_success_url(self):
        return reverse("estoque_list")


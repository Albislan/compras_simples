"""compras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
import debug_toolbar
from .core import views as v
from .estoque import views
from .produto import views as vi
from .core.views import FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView, \
    ContatoCreateView, ContatoListView, ContatoUpdateView, ContatoDeleteView
from .produto.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    MarcaCreateView, MarcaListView, MarcaUpdateView, MarcaDeleteView
from .estoque.views import EstoqueListView, EstoqueDeleteView, \
    ComprasCreateView, ComprasListView, ComprasUpdateView, ComprasDeleteView, ComprasDetailView, EstoqueDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(TemplateView.as_view(template_name='index.html')), name='index'),
    path('login/', v.login_user),
    path('login/submit', v.submit_login),
    path('logout/', v.logout_user),
    path('fornecedor/list', FornecedorListView.as_view(), name='forn_list'),
    path('fornecedor', FornecedorCreateView.as_view(), name='forn_create'),
    path('fornecedor/<int:forn_number>/', FornecedorUpdateView.as_view(), name='forn_update'),
    path('fornecedor/<int:forn_number>/delete/', FornecedorDeleteView.as_view(), name='forn_delete'),
    path('contato/list', ContatoListView.as_view(), name='cont_list'),
    path('contato', ContatoCreateView.as_view(), name='cont_create'),
    path('contato/<int:pk>/', ContatoUpdateView.as_view(), name='cont_update'),
    path('contato/<int:pk>/delete/', ContatoDeleteView.as_view(), name='cont_delete'),
    path('produto/list', ProdutoListView.as_view(), name='prod_list'),
    path('produto', ProdutoCreateView.as_view(), name='prod_create'),
    path('produto/<int:pk>/', ProdutoUpdateView.as_view(), name='prod_update'),
    path('produto/<int:pk>/json/', vi.produto_json, name='produto_json'),
    path('produto/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='prod_delete'),
    path('marca/produto/list', MarcaListView.as_view(), name='marca_list'),
    path('marca/produto', MarcaCreateView.as_view(), name='marca_create'),
    path('marca/produto/<int:pk>/', MarcaUpdateView.as_view(), name='marca_update'),
    path('marca/protduto/<int:pk>/delete/', MarcaDeleteView.as_view(), name='marca_delete'),
    path('compras/list', ComprasListView.as_view(), name='compras_list'),
    path('compra', views.compras_create, name='compras_create'),
    path('compra/<int:pk>/', ComprasDetailView.as_view(), name='compra_detail'),
    # path('compra/<int:pk>/', ComprasUpdateView.as_view(), name='compras_update'),
    path('compra/<int:pk>/delete/', ComprasDeleteView.as_view(), name='compras_delete'),
    path('estoque/list', EstoqueListView.as_view(), name='estoque_list'),
    path('estoque', views.estoque_create, name='estoque_create'),
    path('estoque/<int:pk>/', EstoqueDetailView.as_view(), name='estoque_detail'),
    path('estoque/<int:pk>/delete/', EstoqueDeleteView.as_view(), name='estoque_delete'),
    # path('artigo/list', ArticleListView.as_view(), name='article_list'),
    # path('artigo', ArticleCreateView.as_view(), name='article_create'),
    # path('author/list', AuthorListView.as_view(), name='author_list'),
    # path('author', AuthorCreateView.as_view(), name='author_create'),
    # path('book/list', BookListView.as_view(), name='book_list'),
    # path('book', BookCreateView.as_view(), name='book_create'),
    path('__debug__/', include(debug_toolbar.urls)),
]

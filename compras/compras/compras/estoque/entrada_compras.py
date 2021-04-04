import copy
from decimal import Decimal
from .forms import PedidoAddProdutoForm
from compras.compras.produto.models import Produto

class Pedido:

    def __iter__(self):
        pedido = copy.deepcopy(self.pedido)

        produtos = Produto.objects.filter(id_in=pedido)
        for produto in produtos:
            pedido[str(produto.id)]['produto'] = produto

        for item in pedido.values():
            item['preco'] = Decimal(item['preco'])
            item['valor'] = item['quantidade'] * item['preco']
            item['update_quantidade_form'] = PedidoAddProdutoForm(
                initial={'quantidade': item['quantidade'], 'override':True}
            )

            yield item

    def __len__(self):
        return sum(item['quantidade'] for item in self.pedido.values())

    def add(self, produto, quantidade=1, override_quantidade=False):
        produto_id = str(produto.id)

        if produto_id not in self.pedido:
            self.pedido[produto_id] = {
                'quantidade': 0,
                'preco': str(produto.preco)
            }

        if override_quantidade:
            self.pedido[produto_id]['quantidade'] = quantidade
        else:
            self.pedido[produto_id]['quantidade'] += quantidade

        self.pedido[produto_id]['quantidade'] = min(20, self.pedido[produto_id]['quantidade'])

        self.save()

    def remove(self, produto):
        prouto_id = str(produto.id)

        if prouto_id in self.pedido:
            del self.pedido[prouto_id]
            self.save()

    def get_preco_total_pedido(self):
        return sum(
            Decimal(item['preco']) * item['quantidade'] for item in self.pedido.values()
        )

    def clear(self):
        del self.session['pedido']

    def save(self):
        self.session.modified = True
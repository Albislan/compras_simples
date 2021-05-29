var count = $('#compras').children().length;
var listaSoma = []
$(document).ready(function() {
    $('#id_compras-0-produtos').addClass('clProduto');
    $('#id_compras-0-quant').addClass('clQuantidade');
    $('#id_compras-0-preco_unit').addClass('clPreco');
    $('#id_compras-0-sald').prop('type', 'hidden');
    $('#id_compras-0-valor').prop('type', 'hidden');
    $('label[for="id_compras-0-sald"]').append('<span id="id_compras-0-sald-span" class= "lead" style="padding-left: 10px;"></span>');
    $('label[for="id_compras-0-sald"]').append('<input id="id_compras-0-inicial" class= "form-control" type="hidden" />');
    $('label[for="id_compras-0-valor"]').append('<span id="id_compras-0-valor-span" class= "lead" style="padding-left: 10px;"></span>');
    $('label[for="id_compras-0-valor"]').append('<input id="id_compras-0-vr" class= "form-control" type="hidden" />');
    $('.clProduto').select2();
});
    $('#add-item').click(function(ev) {
        ev.preventDefault();
        var tmplMarkup = $('#item-compras').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#compras').append(compiledTmpl);
        $('#id_compras-TOTAL_FORMS').attr('value', count + 1);
        $('#id_compras-' + (count) + '-sald').prop('type', 'hidden')
        $('#id_compras-' + (count) + '-valor').prop('type', 'hidden')
        $('html', 'body').animate({
            scrollTop: $('#add-item').position().top - 200
        }, 800);
        $('#id_compras-' + (count) + '-produtos').addClass('clProduto');
        $('#id_compras-' + (count) + '-quant').addClass('clQuantidade');
        $('#id_compras-' + (count) + '-preco_unit').addClass('clPreco')
        $('label[for="id_compras-' + (count) + '-sald"]').append('<span id="id_compras-' + (count) + '-sald-span" class="lead" style="padding-left: 10px;"></span>')
        $('label[for="id_compras-' + (count) + '-sald"]').append('<input id="id_compras-' + (count) + '-inicial" class="form-control" type="hidden" />')
        $('label[for="id_compras-' + (count) + '-valor"]').append('<span id="id_compras-' + (count) + '-valor-span" class="lead" style="padding-left: 10px;"></span>')
        $('label[for="id_compras-' + (count) + '-valor"]').append('<input id="id_compras-' + (count) + '-vr" class="form-control" type="hidden" />')
        $('.clProduto').select2()
        count++
    });

let estoque
let estoqueAtual
let campoQuantidade
let campoEstoqueAtual
let campoValorUnitario
let campoValorTotal
let valorUnitario
let quantidade
let valorTotal
let somaTotalFinal
const valorNf = document.getElementById('id_comp-valor')

$(document).on('change', '.clProduto', function() {
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'

    $.ajax({
    url: url,
    type: 'GET',
    success: function(response) {
        estoque = response.data[0].estoque
        campoQuantidade = self.attr('id').replace('produtos', 'quant')
        estoque_inicial = self.attr('id').replace('produtos', 'inicial')
        $('#' + estoque_inicial).val(estoque)
        $('#' + campoQuantidade).val('')
    },
    error: function(xhr) {
        // body...
    }
    })
});

$(document).on('change', '.clQuantidade', function() {
    quantidade = $(this).val();
    campoQuantidade = $(this).attr('id').replace('quant', 'sald')
    campo_estoque_inicial = $(this).attr('id').replace('quant', 'inicial')
    estoque_inicial = $('#' + campo_estoque_inicial).val()
    estoqueAtual = Number(quantidade) + Number(estoque_inicial)
    $('#' + campoQuantidade).prop('type', 'hidden')
    $('#' + campoQuantidade).val(estoqueAtual)
    campoEstoqueAtual = $(this).attr('id').replace('quant', 'sald-span')
    $('#' + campoEstoqueAtual).text(estoqueAtual)
});

$(document).on('change', '.clPreco', function() {
    let somaValorTotal = 0
    var ind = ''
    valorUnitario = $(this).val();
    campoValorUnitario = $(this).attr('id').replace('preco_unit', 'valor')
    valorTotal = valorUnitario * quantidade
    if (campoValorUnitario[12] === '-') {
        ind += campoValorUnitario[11]
        listaSoma[ind] = valorTotal
        for(j=0; j< listaSoma.length; j++) {
            somaValorTotal += listaSoma[j]
            somaTotalFinal = somaValorTotal.toFixed(2)
        }
    }else {
        ind += campoValorUnitario[11] + campoValorUnitario[12]
        listaSoma[ind] = valorTotal
        for(j=0; j< listaSoma.length; j++) {
            somaValorTotal += listaSoma[j]
            somaTotalFinal = somaValorTotal.toFixed(2)
        }
    }
    $("input[name*='compras-valor']")
    somaValorTotalFormatado = somaValorTotal.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL'})
    document.getElementById('geral').setAttribute('value', somaValorTotalFormatado)
    $('#' + campoValorUnitario).prop('type', 'hidden')
    $('#' + campoValorUnitario).val(valorTotal)
    campoValorTotal = $(this).attr('id').replace('preco_unit', 'valor-span')
    $('#'+ campoValorTotal).text(valorTotal.toFixed(2))
});

var form = document.getElementById('formulario');

form.addEventListener('submit', function(e) {
    nfValor = parseFloat(valorNf.value)
    if (nfValor != somaTotalFinal) {
        alert('ops! \n A soma dos valores dos itens lançados não batem com o valor da NF \n Favor verificar e corrigir!')
        e.preventDefault();
    }
})

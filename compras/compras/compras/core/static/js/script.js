$(document).ready(function() {
    $('#id_estoque-0-produto').addClass('clProduto');
    $('#id_estoque-0-quantidade').addClass('clQuantidade');
    $('#id_estoque-0-saldo').prop('type', 'hidden');
    $('label[for="id_estoque-0-saldo"]').append('<span id="id_estoque-0-saldo-span" class= "lead" style="padding-left: 10px;"></span>')
    $('label[for="id_estoque-0-saldo"]').append('<input id="id_estoque-0-inicial" class= "form-control" type="hidden" />')
    $('.clProduto').select2()
});
$('#add-item').click(function(ev) {
    ev.preventDefault();
    var count = $('#estoques').children();length;
    var tmplMarkup = $('#item-estoque').html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $('div#estoques').append(compiledTmpl);
    $('#id_estoques-TOTAL_FORMS').attr('value', count + 1);
    $('#id_estoques-' + (count) + '-saldo').prop('type', 'hidden')
    $('html', 'body').animate({
        scrollTop: $('#add-item').position().top - 200
    }, 800);
    $('#id_estoques-' + (count) + '-produto').addClass('clProduto');
    $('#id_estoques-' + (count) + '-quantidade').addClass('clQuantidade');
    $('label[for="id_estoques-' + (count) + '-saldo"]').append('<span id="id_estoques-' + (count) + '-saldo-span" class="lead" style="padding-left: 10px;"></span>')
    $('label[for="id_estoques-' + (count) + '-saldo"]').append('<input id="id_estoques-' + (count) + '-inicial" class="form-control" type="hidden" />')
    $('.clProduto').select2()
});

let estoque
let saldo
let campo
let campo2
let quantidade

$(document).on('change', '.clProduto', function() {
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'

    $.ajax({
    url: url,
    type: 'GET',
    success: function(response) {
        estoque = response.data[0].estoque
        campo = self.attr('id').replace('produto', 'quantidade')
        estoque_inicial = self.attr('id').replace('produto', 'inicial')
        $('#' + estoque_inicial).val(estoque)
        $('#' + campo).val('')
    },
    error: function(xhr) {
        // body...
    }
    })
});

$(document).on('change', '.clQuantidade', function() {
    quantidade = $(this).val();
    campo = $(this).attr('id').replace('quantidade', 'saldo')
    campo_estoque_inicial = $(this).attr('id').replace('quantidade', 'inicial')
    estoque_inicial = $('#' + campo_estoque_inicial).val()
    saldo = Number(quantidade) + Number(estoque_inicial)
    $('#' + campo).prop('type', 'hidden')
    $('#' + campo).val(saldo)
    campo2 = $(this).attr('id').replace('quantidade', 'saldo-span')
    $('#' + campo2).text(saldo)
});
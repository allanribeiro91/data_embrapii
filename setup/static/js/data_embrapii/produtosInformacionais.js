document.addEventListener('DOMContentLoaded', function() {

    const botao_inserir_produtoInformacional = document.getElementById('btnInserirProdutoInformacional')
    const modal_produtoInformacional = new bootstrap.Modal(document.getElementById('modalProdutosInformacionais'))
    botao_inserir_produtoInformacional.addEventListener('click', function(){
        modal_produtoInformacional.show()
    })

});
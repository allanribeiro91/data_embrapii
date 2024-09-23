document.addEventListener('DOMContentLoaded', function() {

    const botao_inserir_produtoInformacional = document.getElementById('btnInserirProdutoInformacional')
    const modal_produtoInformacional = new bootstrap.Modal(document.getElementById('modalProdutosInformacionais'))
    botao_inserir_produtoInformacional.addEventListener('click', function(){
        modal_produtoInformacional.show()
    })


    
    const statusFilter = document.getElementById('filtroStatusPrivacidade');
    const ferramentaFilter = document.getElementById('filtroFerramenta');
    const donoFilter = document.getElementById('filtroDonoProduto');
    const fonteFilter = document.getElementById('filtroFontesDados');
    const cards = document.querySelectorAll('.box_dataviz');

    function filterCards() {
        const status = statusFilter.value.toLowerCase();
        const ferramenta = ferramentaFilter.value.toLowerCase();
        const dono = donoFilter.value.toLowerCase();
        const fonte = fonteFilter.value.toLowerCase();

        cards.forEach(card => {
            const cardStatus = card.getAttribute('data-status').toLowerCase();
            const cardFerramenta = card.getAttribute('data-ferramenta').toLowerCase();
            const cardDono = card.getAttribute('data-dono').toLowerCase();
            const cardFonte = card.getAttribute('data-fonte').toLowerCase();

            if (
                (status === "" || cardStatus === status) &&
                (ferramenta === "" || cardFerramenta === ferramenta) &&
                (dono === "" || cardDono === dono) &&
                (fonte === "" || cardFonte === fonte)
            ) {
                card.style.visibility = "visible";
            } else {
                card.style.visibility = "hidden";
            }
        });
    }

    // Adicionar evento nos filtros
    statusFilter.addEventListener('change', filterCards);
    ferramentaFilter.addEventListener('change', filterCards);
    donoFilter.addEventListener('change', filterCards);
    fonteFilter.addEventListener('change', filterCards);


    const limparFiltros = this.documentElement.querySelector('#limparFiltros')
    limparFiltros.addEventListener('click', function(){
        statusFilter.value = "";
        ferramentaFilter.value = "";  
        donoFilter.value = "";
        fonteFilter.value = "";

        filterCards();
    })
    

});
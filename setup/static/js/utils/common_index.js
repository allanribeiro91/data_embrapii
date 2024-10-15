document.addEventListener('DOMContentLoaded', function() {
    
    const botao_inserir = document.getElementById('Inserir')
    botao_inserir.addEventListener('click', function(){
        const novaUrl = `${window.location.origin}${window.location.pathname}/novo`;
        window.location.href = novaUrl;
    })

});
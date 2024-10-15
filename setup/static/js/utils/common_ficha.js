document.addEventListener('DOMContentLoaded', function() {

    const botao_cancelar = document.getElementById('Cancelar')
    botao_cancelar.addEventListener('click', function() {
        const pathAtual = window.location.pathname;
    
        // Remove '/novo' do final do caminho, se presente
        const novaUrl = pathAtual.endsWith('/novo') 
            ? pathAtual.slice(0, -5)  // Remove os últimos 5 caracteres ('/novo')
            : pathAtual;
    
        // Redireciona para a nova URL
        window.location.href = `${window.location.origin}${novaUrl}`;
    })

});
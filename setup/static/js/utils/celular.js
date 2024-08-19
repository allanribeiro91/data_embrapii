function celularFormato(numero) {
    // Remove tudo que não for dígito
    let numeroLimpo = numero.replace(/\D/g, '');

    // Limita a 11 dígitos (2 para o DDD e 9 para o número)
    numeroLimpo = numeroLimpo.substring(0, 11);

    // Formata no padrão (##) #####-####
    // Primeiro verifica se o número tem o comprimento total
    if (numeroLimpo.length === 11) {
        return numeroLimpo.replace(/^(\d{2})(\d{5})(\d{4})$/, '($1) $2-$3');
    } else {
        // Se o número é mais curto, formata conforme o comprimento
        if (numeroLimpo.length > 7) {
            return numeroLimpo.replace(/^(\d{2})(\d{0,5})(\d{0,4})$/, '($1) $2-$3');
        } else if (numeroLimpo.length > 2) {
            return numeroLimpo.replace(/^(\d{2})(\d{0,5})$/, '($1) $2');
        } else {
            return numeroLimpo.replace(/^(\d*)$/, '($1');
        }
    }
}
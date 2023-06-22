
function acaoBotao(){
    var valor1, valor2, resultado, operacao;

    valor1 = parseInt(prompt("Digite o primeiro valor: "))
    operacao = prompt("Digite a operacao: Ex: +, -, *, /")
    valor2 = parseInt(prompt("Digite o segundo valor: "))
    
    if (operacao == "+"){
        resultado = valor1 + valor2
    }
    else if (operacao == "-"){
        resultado = valor1 - valor2
    }
    else if (operacao == "*"){
        resultado = valor1 * valor2
    }
    else if (operacao == "/"){
        resultado = valor1 / valor2
    }    
    document.getElementById("paragrafo").innerText = resultado

}

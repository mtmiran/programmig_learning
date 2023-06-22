function acaoBotao(){
    var valor1, valor2, resultado, operacao;

    valor1 = parseInt(prompt("Digite o primeiro valor: "))
    operacao = prompt("Digite a operacao: Ex: +, -, *, /")
    valor2 = parseInt(prompt("Digite o segundo valor: "))
    
    switch (operacao){
        case "+":
            resultado = valor1 + valor2
            break;
        case "-":
            resultado = valor1 - valor2
            break;
        case "*":
            resultado = valor1 * valor2
            break;
        case "/":
            resultado = valor1 / valor2
            break;

    }
    document.getElementById("paragrafo").innerText = resultado

}

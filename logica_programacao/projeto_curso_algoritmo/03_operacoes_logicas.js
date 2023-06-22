var nome, nota1, nota2, media, passou;

nome = prompt("Digite o nome do aluno: ")
nota1 = prompt("Digitie nota 1: ")
nota2 = prompt("Digitie nota 2: ")
passou = false;
media = (parseInt(nota1) + parseInt(nota2)) / 2;

if (media >= 5){
    passou = true;
}
if (passou && (media >= 7 && media <= 90)){
    alert("Aprovado! "+ nome)
}
else{
    alert("Reprovado! " + nome)
}

var nome, nota1, nota2, media;

nome = prompt("Digite o nome do aluno: ")
nota1 = prompt("Digitie nota 1: ")
nota2 = prompt("Digitie nota 2: ")

media = (parseInt(nota1) + parseInt(nota2)) / 2;

if (media >= 5){
    alert("Aprovado! " + nome)
}
else{
    alert("Reprovado! " + nome)
}

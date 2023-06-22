// ### Variaveis###

// definicao da bolinha
let xBolinha = 100;
let yBolinha = 200;
let diametro = 20;
// bolinha entra nas bordas pq o x é o centro do circulo
// pare reconhecer a colisão precisa do raio
let raio = diametro / 2;

//velocidade da bolinha
let velocidadeXBolinha = 6;
let velocidadeYBolinha = 6;

// raquete
let xRaquete = 5;
let yRaquete = 150;
let raqueteComprimento = 10;
let raqueteAltura = 90;

// raquete oponente
let xRaqueteOponente = 585;
let yRaqueteOponente = 150;
let velocidadeYOponente;

// placar pontos
let meusPontos = 0;
let pontosOponente = 0;

// biblioteca collider
let colidiu = false;

// sons do jogo
let raquetada;
let ponto;
let trilha

// =============================================

// ### Funcoes ###

// carregar os sons
function preload(){
  trilha = loadSound("trilha.mp3");
  ponto = loadSound("ponto.mp3");
  raquetada = loadSound("raquetada.mp3");

}

// criar o plano de fundo
function setup() {
  createCanvas(600, 400);
  trilha.loop(); // tocar son da trilha
}

// desenhar os elementos do jogo
function draw() {
  background(0);
  mostraBolinha();
  movimentaBolinha();
  verificaColisaoBorda();
  mostraRaquete(xRaquete, yRaquete);
  mostraRaquete(xRaqueteOponente, yRaqueteOponente);
  movimentaRaquete();
  movimentaRaqueteOponente();
  // verificaColisaoRaquete();
  colisaoRaqueteBiblioteca(xRaquete, yRaquete);
  colisaoRaqueteBiblioteca(xRaqueteOponente, yRaqueteOponente);
  incluiPlacar();
  marcaPonto();
}


// Funcoes Bolinha

// criar a bolinha
function mostraBolinha(){
  circle(xBolinha, yBolinha, diametro);
}

// movimentar a bolinha
function movimentaBolinha(){
    xBolinha += velocidadeXBolinha;
  yBolinha += velocidadeYBolinha;
}

// função para verificar a colisão nas bordas
function verificaColisaoBorda(){
    // se tocar na borda - voltar - horizontal
  // width - largura maxima da tela, borda direita
  // xBolinha < 0 -> borda esquerda
  if (xBolinha + raio > width || xBolinha -raio < 0){
    velocidadeXBolinha *= -1 //inverter a velocidade
  }
  
  // se tocar no teto ou chao
  if (yBolinha + raio > height || yBolinha - raio < 0){
    velocidadeYBolinha *= -1
  }
}

// Funcoes raquete
// criar raquete
function mostraRaquete(x,y){
  rect(x, y, raqueteComprimento, raqueteAltura)
}


//movimentar a raquete
function movimentaRaquete() {
    if (keyIsDown(UP_ARROW)) {
        yRaquete -= 10;
    }
    if (keyIsDown(DOWN_ARROW)) {
        yRaquete += 10;
    }
}


// movimentar a raquete oponente
function movimentaRaqueteOponente(){
  // 87 == tecla w
   if (keyIsDown(87)) {
        yRaqueteOponente -= 10;
    }
  // 83 == tecla s
    if (keyIsDown(83)) {
        yRaqueteOponente += 10;
    }
}

// colisao com a bolinha - mudar direcao
// function verificaColisaoRaquete(){
//   if (xBolinha - raio < xRaquete + raqueteComprimento && yBolinha - raio < yRaquete + raqueteAltura && yBolinha + raio > yRaquete){
//     velocidadeXBolinha *= -1
//     raquetada.play();
//   }
// }

// funcao de colisao usando a biblioteca collider2d
function colisaoRaqueteBiblioteca(x, y){
  colidiu = collideRectCircle(x, y, raqueteComprimento, raqueteAltura, xBolinha, yBolinha, raio);
  if (colidiu){
    velocidadeXBolinha *= -1
    raquetada.play();
  }
}


// Funcao Placar
function incluiPlacar(){
  stroke(255); // contorno na cor branca
  textAlign(CENTER);
  textSize(16);
  
  // criar quadrados do placar
  fill(color(255, 140, 0)) // pintar o quadrado de laranja
  rect(130, 10, 40, 20)
  fill(255); // pintar o texto de branco
  //              x  e  y
  text(meusPontos, 150, 26);
  fill(color(255, 140, 0)); // pintar o quadrado de laranja
  rect(430, 10, 40, 20);
  fill(255); // pintar o texto de branco
  text(pontosOponente, 450, 26);
}

function marcaPonto(){
  if (xBolinha > 590){
    meusPontos += 1;
    ponto.play();
  }
  if (xBolinha < 10){
    pontosOponente += 1;
    ponto.play();
  }
}








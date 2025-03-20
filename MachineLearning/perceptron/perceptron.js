class Perceptron {
  weights = [0, 0];
  constructor() {
    // Inicializando com valores random
    for (let i = 0; i < this.weights.length; i++) {
      this.weights[i] = random(-1, 1);
    }
  }

  //inputs --> entrada array de duas posiçoes (X1 e X2)
  guess(inputs) {
    let sum = 0;
    // aplicando a formula (Y = X1 * W1 + X2 * W2)
    for (let i = 0; i < this.weights.length; i++) {
      sum += inputs[i] * this.weights[i];
    }
    const output = sign(sum);
    return output;
  }
}

//Função de aticação
function sign(num) {
  return num >= 0 ? 1 : -1;
}

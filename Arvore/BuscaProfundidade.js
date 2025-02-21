import NoB from "./NoB.js";

class BuscaProfundidade {
  static preOrdem(no) {
    if (!no) {
      return;
    }
    console.log(no.valor);
    this.preOrdem(no.filhoEsquerda);
    this.preOrdem(no.filhoDireita);
  }

  static inOrdem(no) {
    if (!no) {
      return;
    }
    this.inOrdem(no.filhoEsquerda);
    console.log(no.valor);
    this.inOrdem(no.filhoDireita);
  }

  static posOrdem(no) {
    if (!no) {
      return;
    }
    this.posOrdem(no.filhoEsquerda);
    this.posOrdem(no.filhoDireita);
    console.log(no.valor);
  }

  static porLargura(no, fila) {
    if (!fila || fila.length == 0) {
      return;
    }

    if (!no) {
      return;
    }

    if (no.filhoEsquerda) {
      fila.push(no.filhoEsquerda);
    }

    if (no.filhoDireita) {
      fila.push(no.filhoDireita);
    }

    console.log(no);
    fila.shift();
    this.porLargura(fila[0], fila);
  }
}

export default BuscaProfundidade;

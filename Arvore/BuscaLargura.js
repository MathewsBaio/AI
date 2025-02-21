export default class BuscaLargura {
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

  static buscaLargura(raiz) {
    if (!raiz) {
      return;
    }

    let fila = [raiz];
    atual = null;
    while (fila.length > 0) {
      atual = fila.shift();

      console.log(atual);

      if (atual.filhoEsquerda) {
        fila.push(atual.filhoEsquerda);
      }

      if (atual.filhoDireita) {
        fila.push(atual.filhoDireita);
      }
    }
  }
}

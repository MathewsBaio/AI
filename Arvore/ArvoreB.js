import NoB from "./NoB.js";
import BuscaProfundidade from "./BuscaProfundidade.js";

class ArvoreB {
  raiz = null;
  constructor(no) {
    if (no instanceof NoB) {
      this.raiz = no;
    } else {
      throw new Error("A raiz deve ser um nó!");
    }
  }

  buscaPreOrdem() {
    BuscaProfundidade.preOrdem(this.raiz);
  }
}

export default ArvoreB;

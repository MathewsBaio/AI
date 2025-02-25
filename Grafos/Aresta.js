import Vertice from "./Vertice";

class Aresta {
  vertices = [];
  nome = "";
  constructor(nome, vertice1 = null, vertice2 = null) {
    this.nome = nome;
    if (
      vertice1 &&
      vertice2 &&
      vertice1 instanceof Vertice &&
      vertice2 instanceof Vertice
    ) {
      this.vertices = [vertice1, vertice2];
      vertice1.arestas.push(this);
      vertice2.arestas.push(this);
    }
  }
}

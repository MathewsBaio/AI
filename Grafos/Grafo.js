class Grafo {
  vertices = [];
  arestas = [];
  constructor() {}

  addVertice(valor) {
    const vertice = new Vertice(valor);
    this.vertices.push(vertice);
    return vertice;
  }

  addAresta(nome, vertice1, vertice2) {
    const aresta = new Aresta(nome, vertice1, vertice2);
    this.arestas.push(aresta);
    return aresta;
  }
}

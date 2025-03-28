import Vertice from "./Vertice";

class Aresta{
    vertices = [];
    nome = "";
    custo = 0;

    constructor(nome,vertice1 = null, vertice2 = null, custo = 0){
        this.nome = nome;
        this.custo = custo;

        if(vertice1 && vertice2
            && vertice1 instanceof Vertice
            && vertice2 instanceof Vertice){
            this.vertices = [vertice1,vertice2];
            vertice1.aresta.push(this);
            vertice2.aresta.push(this);
        }      
    }
}

export default Aresta;

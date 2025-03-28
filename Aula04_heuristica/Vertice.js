class Vertice{
    valor = "";
    aretas = [];
    heuristica = 0;

    constructor(valor,heuristica){
        this.valor = valor;
        this.heuristica = heuristica;
    }
}

export default Vertice
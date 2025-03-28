class Rastreador
{
    custo = 0;
    vertice = null;
    anterior = null;

    constructor(vertice,anterior,custoAtual) {
        this.vertice = vertice;
        this.anterior = anterior;
        this.custo = anterior.custo + custoAtual;
    }

    funcaoAvaliacao(){
        return this.custo+this.vertice.heuristica;
    }
}

export default Rastreador;
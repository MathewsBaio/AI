import random 

class Perceptron:

    def __init__(self, num_weights):
        self.weights = [random.uniform(-1,1),random.uniform(-1,1) for _ in range(num_weights)]
        self.lr = 0.1 #learning rate

    # inputs tbm é uma lista com dois valores (pois weights tbm é uma lista com dois)
    def guess(self, inputs):
        total = sum(inputs[i] * self.weights[i] for i in range(len(self.weights)))
        return self._sign(total)
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = guess - target 

        # ajustar os pesos
        for i in range(len(self.weights)):
            self.weights[i] += error * input[i] * self.lt
    
    def _sign(self,num):
        return 1 if num >= 0 else -1


    # A ideia é classificar pontos num plano cartesiano entre sendo pertencentes 
    # a um de dois grupos, definidos pelo corte da linha onde eixo y é igual ao eixo x
    # ex: (1,1), (2,2), (3,3)... Os pontos acima dessa linha classificamos como 1
    # e os pontos abaixo dessa linha nós classificamos como -1


    # Ao pegar o guess para descobrir o grupo do ponto (3,10)
    # considerando pesos aleatorios definidos como w1 = 0.5 e w2 = -0.8
    # net = w1*x1 + w2*x2
    # net = 0.5*3 + -0.8*10
    # net = 1.5 + (-8)
    # net = -6.5
    # após chamar a função de ativação (1 if num >= 0 else -1) -> seria classificado como -1
    # apesar do ponto ser de facto do grupo definido como 1, nesse exemplo da execução
    # o perceptron teria errado o palpite, com os pesos utilizados.
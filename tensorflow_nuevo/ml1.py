import tensorflow as tf

#1 Conjunto de dados de treinamento - entrada e saída 
xs = tf.constant([0,1,2,3,4], dtype=tf.float32)
ys = xs * 1.2 + 5

#2 Modelo de aprendizado de máquina
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units = 1, input_shape = [1])
])

#3 Compilar modelo - com otimizador e função de perda
model.compile(optimizer = "sgd", loss = "mean_squared_error")


#4 Treinar modelo - dados de treinamento e quantidade de vezes
print("O modelo está treinando")

model.fit(xs, ys, epochs = 500)


def linear_reg():
    x_max = 20 # máximo de pontos
    x_arr = [] # coord x
    y_arr = [] # cood y encontrada
    correct_arr = [] # cood y que deveria ter sido encontrada

    for x in range(10, x_max + 1):
        x_tensor = tf.constant([float(x)],dtype = tf.float32)
        y_pred = model.predict(x_tensor, verbose = 0)
        x_arr.append(x)
        y_arr.append(float(y_pred[0][0]))
        correct_arr.append(float(x * 1.2 + 5))

    display(x_arr, y_arr, correct_arr)

def display(x_arr, y_arr, correct_arr):
    text = "Correct\tPredict \n"
    for i in range(len(x_arr)):
        correct = correct_arr[i]
        predicted = y_arr[i]
        text += f"{correct:.4f}\t{predicted:.4f}"
    print(text)

linear_reg()
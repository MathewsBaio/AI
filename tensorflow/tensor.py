import tensorflow as tf

xs = tf.constant([0,1,2,3,4], dtype = tf.float32)
ys = xs * 1.2 + 5

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(loss='mean_squared_error', optimizer='sdg')

print("Model is training!")

model.fit(xs,ys,epochs=500)

def linear_red():
    x_max = 20
    x_arr = []
    y_arr = []
    correct_arr = []
    
    for x in range(10, x_max+1):
        x_tensor = tf.constant([float(x)], dtype=tf.float32)
        y_pread = model.predict(x_tensor, verbose=0)
        x_arr.append(x)
        y_arr.append(float(y_pread[0][0]))
        correct_arr.append(float(x * 1.2 + 5))
    
    display(x_arr,y_arr,correct_arr)
    
def display(x_arr,y_arr,correct_arr):
    
    text = "Correct Predicted \n"
    
    for i in range(0, len(x_arr)):
        corret = correct_arr[i]
        predicted = y_arr[i]
        text += f"{correct:.4f} {predicted:.4f}"
    
    print(text)
    
linear_red()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

url = "https://storage.googleapis.com/tfjs-tutorials/carsData.json"
column_names = [
    'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
    'Acceleration', 'Model Year', 'Origin'
]

raw_dataset = pd.read_csv(
    url,
    names = column_names,
)

dataset = raw_dataset.copy()

dataset = dataset.dropna()
dataset = dataset.pop("Origin")

dataset["USA"] = (origin == 1) * 1.0
dataset["Europe"] = (origin == 2) * 1.0
dataset["Japan"] = (origin == 3) * 1.0

print(dataset.tail())

train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

train_stats = train_dataset.describe()
train_stats = train_stats.transpose()

train_labels = train_dataset.pop("MPG")
test_labels = train_dataset.pop("MPG")

# Normaliza os dados (entre 0 e 1)
def norm(x):
    return (x - train_stats["mean"]) / train_stats["std"]

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

def build_model():
    model = keras.Sequential([
        layers.Dense(64, activation="relu", input_shape=[len(train_dataset.keys())]),
        layers.Dense(64, activation="relu"),
        layers.Dense(1)
    ])
    
    optmizer = tf.keras.optimizers.RMSprop(0.001)
    
    model.compile(loss="mse",
                  optmizer=optimizer,
                  metrics=["mae, mse"]
    )

    return model

model = build_model()

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf

from tensorflow import keras 
from tensorflow.keras import layers

url = "./auto-mpg/auto-mgp.data"

columns = ["MPG", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration",
           "Model Year", "Origin"]

raw_dataset = pd.read_csv(url, names = columns, na_values = '?', comment = '\t', sep = " ", skipinitialspace = True)

print(raw_dataset.info())

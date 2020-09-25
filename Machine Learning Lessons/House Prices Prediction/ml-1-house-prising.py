import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([1.0,  5.0, 16.0, 2.0, 3.0, 13.0], dtype=float)
ys = np.array([1.0, 3.0, 8.5, 1.5, 2.0, 7.0], dtype=float)
model.fit(xs, ys, epochs=1500)
print(model.predict([7.0]))

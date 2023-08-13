import os
from django.db import models
import tensorflow as tf

class HandwrittenDigitModel(models.Model):
    model = None

    @staticmethod
    def load_or_train_model():
        if HandwrittenDigitModel.model is None:
            # Loading the model if available, or creating and training a new one
            if os.path.exists('ImageApp/models/handwritten_digits.model'):
                HandwrittenDigitModel.model = tf.keras.models.load_model('ImageApp/models/handwritten_digits.model')
            else:
                mnist = tf.keras.datasets.mnist
                (X_train, y_train), (_, _) = mnist.load_data()

                X_train = tf.keras.utils.normalize(X_train, axis=1)

                model = tf.keras.models.Sequential()
                model.add(tf.keras.layers.Flatten())
                model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
                model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
                model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

                model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
                model.fit(X_train, y_train, epochs=7)

                HandwrittenDigitModel.model = model
                model.save('ImageApp/models/handwritten_digits.model')

        return HandwrittenDigitModel.model


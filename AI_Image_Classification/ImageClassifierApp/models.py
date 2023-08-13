from django.db import models
from tensorflow import keras
import numpy as np
import cv2 as cv
from keras import datasets, layers, models
import matplotlib.pyplot as plt
import os

class ImageClassificationModel(models.Model):
    model = None

    @staticmethod
    def load_or_train_model():
        if ImageClassificationModel.model is None:
            # Loading the model if available, or creating and training a new one
            if os.path.exists('ImageClassifierApp/models/image_classifier.model'):
                ImageClassificationModel.model = keras.models.load_model('ImageClassifierApp/models/image_classifier.model')
            else:
                (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
                training_images, testing_images = training_images / 255, testing_images / 255

                class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

                for i in range(16):
                    plt.subplot(4, 4, i + 1)
                    plt.xticks([])
                    plt.yticks([])
                    plt.imshow(training_images[i], cmap=plt.cm.binary)
                    plt.xlabel(class_names[training_labels[i][0]])

                model = models.Sequential()
                model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
                model.add(layers.MaxPooling2D((2, 2)))
                model.add(layers.Conv2D(64, (3, 3), activation='relu'))
                model.add(layers.MaxPooling2D(2, 2))
                model.add(layers.Conv2D(64, (3, 3), activation='relu'))
                model.add(layers.Flatten())
                model.add(layers.Dense(64, activation='relu'))
                model.add(layers.Dense(10, activation='softmax'))

                model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
                model.fit(training_images, training_labels, epochs=10, validation_data=(testing_images, testing_labels))

                ImageClassificationModel.model = model
                model.save('ImageClassifierApp/models/image_classifier.model')

        return ImageClassificationModel.model

    @staticmethod
    def predict_image(img):
        model = ImageClassificationModel.load_or_train_model()

        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.resize(img, (32, 32)) / 255.0
        prediction = model.predict(np.array([img]))
        index = np.argmax(prediction)
        class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
        predicted_class = class_names[index]

        return predicted_class

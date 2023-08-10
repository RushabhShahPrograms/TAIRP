from tensorflow import keras
from keras import datasets,layers,models
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

(training_images,training_lables),(testing_images,testing_labels) = datasets.cifar10.load_data()
training_images,testing_images = training_images/255, testing_images/255

class_names = ['Plane','Car','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']

# for i in range(16):
#     plt.subplot(4,4,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.imshow(training_images[i],cmap=plt.cm.binary)
#     plt.xlabel(class_names[training_lables[i][0]])

# plt.show()
# training_images = training_images[:20000]
# training_lables = training_lables[:20000]
# testing_images = testing_images[:4000]
# testing_labels = testing_labels[:4000]

# model = models.Sequential()
# model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)))
# model.add(layers.MaxPooling2D((2,2)))
# model.add(layers.Conv2D(64,(3,3),activation='relu'))
# model.add(layers.MaxPooling2D(2,2))
# model.add(layers.Conv2D(64,(3,3),activation='relu'))
# model.add(layers.Flatten())
# model.add(layers.Dense(64,activation='relu'))
# model.add(layers.Dense(10,activation='softmax'))

# model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# model.fit(training_images,training_lables,epochs=10,validation_data=(testing_images,testing_labels))

# loss,accuracy = model.evaluate(testing_images,testing_labels)
# print(f"loss: {loss}")
# print(f"Accuracy: {accuracy}")


# model.save('image_classifier.model')

model = models.load_model('image_classifier.model')

img = cv.imread('img/deer.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img,cmap=plt.cm.binary)
prediction = model.predict(np.array([img])/255)
index = np.argmax(prediction)
print(f"Prediction is {class_names[index]}")
plt.show()
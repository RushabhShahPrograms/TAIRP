from django.shortcuts import render
from .models import ImageClassificationModel
import os
import cv2
import numpy as np

def index(request):
    return render(request, 'index.html')

def image_classification(request):
    results = []

    for image in request.FILES.getlist('image'):
        try:
            image_path = os.path.join('ImageClassifierApp', 'images', image.name)
            with open(image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            prediction = ImageClassificationModel.predict_image(img)
            results.append(prediction)
            print(f"Processed image {image.name}, result: {prediction}")
        except:
            results.append("Error")
            print(f"Error processing image {image.name}")

    context = {'results': results}
    return render(request, 'result.html', context)

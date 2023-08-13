from django.shortcuts import render
from .models import HandwrittenDigitModel
import os
import cv2
import numpy as np

def index(request):
    return render(request, 'index.html')

def digit_recognition(request):
    model = HandwrittenDigitModel.load_or_train_model()

    results = []

    for image in request.FILES.getlist('image'):
        try:
            image_path = os.path.join('ImageApp', 'digits', image.name)
            with open(image_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            img = cv2.imread(image_path)[:, :, 0]
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            result = np.argmax(prediction)
            results.append(result)
            print(f"Processed image {image.name}, result: {result}")
        except:
            results.append("Error")
            print(f"Error processing image {image.name}")

    context = {'results': results}
    return render(request, 'result.html', context)


<<<<<<< HEAD
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from tensorflow import keras
import cv2 as cv
import numpy as np
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View
from django.views.generic.edit import FormView,CreateView

class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
model = keras.models.load_model('image_classifier.model')

class IndexView(TemplateView):
    template_name = "index.html"

class PredictView(View):
    def post(self, request, *args, **kwargs):
        if request.FILES.get('image'):
            image = request.FILES['image']
            img = cv.imdecode(np.fromstring(image.read(), np.uint8), cv.IMREAD_COLOR)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            img = cv.resize(img, (32, 32))
            img = img / 255.0
            prediction = model.predict(np.array([img]))
            index = np.argmax(prediction)
            class_name = class_names[index]
            return render(request, 'index.html', {'prediction': class_name})
        return JsonResponse({'error': 'No file found'})
=======
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from tensorflow import keras
import cv2 as cv
import numpy as np
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View
from django.views.generic.edit import FormView,CreateView

class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
model = keras.models.load_model('image_classifier.model')

class IndexView(TemplateView):
    template_name = "index.html"

class PredictView(View):
    def post(self, request, *args, **kwargs):
        if request.FILES.get('image'):
            image = request.FILES['image']
            img = cv.imdecode(np.fromstring(image.read(), np.uint8), cv.IMREAD_COLOR)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            img = cv.resize(img, (32, 32))
            img = img / 255.0
            prediction = model.predict(np.array([img]))
            index = np.argmax(prediction)
            class_name = class_names[index]
            return render(request, 'index.html', {'prediction': class_name})
        return JsonResponse({'error': 'No file found'})
>>>>>>> 0fb0c66000e07c1d11087329b62690269a8180e7

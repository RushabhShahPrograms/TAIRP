from django.shortcuts import render
import spacy

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Chat

nlp = spacy.load("en_core_web_sm")

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input", "")

        # Process user input using SpaCy
        doc = nlp(user_input)

        # Your NLP chatbot logic here - generate bot_response based on user_input

        bot_response = "Hello, I am a simple AI chatbot! You said: " + user_input

        # Save the user query and bot response to the database
        Chat.objects.create(user_input=user_input, bot_response=bot_response)

        return JsonResponse({"response": bot_response})

    return JsonResponse({"error": "Invalid Request"})

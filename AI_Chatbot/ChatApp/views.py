from django.shortcuts import render
import spacy
import random
import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Chat

# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Construct the full file path to intents.json using the STATICFILES_DIRS setting
intents_file_path = os.path.join(settings.STATICFILES_DIRS[0], 'intents.json')

# Load the intents data from intents.json
with open(intents_file_path) as f:
    intents_data = json.load(f)

# Create a PhraseMatcher with separate patterns for each intent
from spacy.matcher import PhraseMatcher

intent_matchers = {}  # Dictionary to store PhraseMatchers for each intent

for intent in intents_data['intents']:
    patterns = [nlp(pattern.lower()) for pattern in intent['patterns']]
    matcher = PhraseMatcher(nlp.vocab)
    matcher.add(intent['tag'], None, *patterns)
    intent_matchers[intent['tag']] = matcher


def generate_response(user_input):
    """Generate a bot response based on the user input and the intents data"""
    doc = nlp(user_input.lower())

    # Initialize the best match values
    best_match_score = 0
    best_match_intent = None

    for intent_tag, matcher in intent_matchers.items():
        
        # Check if the user wants to calculate something
        if "calculate" in user_input.lower() or "math" in user_input.lower():
            # Extract the mathematical expression to calculate
            expression = user_input.replace("calculate", "").strip()
            # Evaluate the mathematical expression and return the result
            try:
                result = eval(expression)
                return f"The result of {expression} is: {result}"
            except Exception as e:
                return f"Sorry, I couldn't calculate that. Error: {e}"
        
        # Use the PhraseMatcher to find matches in the user input for each intent

        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            match_score = len(span)  # Calculate the match score as the length of the matched span

            # Update the best match if the current match has a higher score
            if match_score > best_match_score:
                best_match_score = match_score
                best_match_intent = intent_tag

    if best_match_intent:
        # If a match is found, return a random response from the matched intent
        for intent in intents_data['intents']:
            if intent['tag'] == best_match_intent:
                bot_response = random.choice(intent['responses'])
                return bot_response

    # Default response if no intent is matched
    return "Sorry, I don't understand that. Please try again."

@csrf_exempt
def chatbot(request):
    """Handle the chatbot requests and render the chatbot template"""
    if request.method == "POST":
        # Get the user input from the POST request
        user_input = request.POST.get("user_input", "").lower()
        try:
            # Generate a bot response using the generate_response function
            bot_response = generate_response(user_input)
            # Save the user input and bot response in the Chat model
            Chat.objects.create(user_input=user_input, bot_response=bot_response)
        except Exception as e:
            # Handle any exceptions and return an error message
            bot_response = f"Something went wrong: {e}"
            Chat.objects.create(user_input=user_input, bot_response=bot_response)

    # Get all the chats from the Chat model
    chats = Chat.objects.all()
    # Render the chatbot template with the chats context
    return render(request, "chatbot.html", {"chats": chats})


@csrf_exempt
def clear_responses(request):
    """Clear the chatbot responses"""
    try:
        # Delete all the chat entries from the database
        Chat.objects.all().delete()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
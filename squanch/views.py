import json

from django.shortcuts import render
from django.http import JsonResponse

import nltk

# Create your views here.
def squanch(request):
    return render(request, 'index.html')


def squanchitize(request):
    json_request = json.loads(request.read())


    def squanch_text(text):
        text = text.lower()
        tokens = nltk.word_tokenize(text)
        nltk_text = nltk.Text(tokens)

        verbs = [tag[0] for tag in nltk.pos_tag(nltk_text) if tag[1].startswith('VB')]
        for verb in verbs:
            text = text.replace(verb, "<b>squanch</b>")

        return text

    return JsonResponse({'squanchitized_text': squanch_text(json_request['text'])})

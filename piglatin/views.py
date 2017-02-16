from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def translate(request):

    original = request.GET['originaltext'].lower()

    #to modify user input to create pig latin translation
    translation = ''
    for word in original.split():
        #check if first letter in each word is vowel
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translation += word
            translation += 'yay '
        #if the first letter is a consonant
        else:
            translation += word[1:]
            translation += word[0]
            translation += 'ay '
    #calls function on translate page to perform the translation
    return render(request, 'translate.html',
                  {'original':original, 'translation':translation})


def about(request):
    return render(request, 'about.html')
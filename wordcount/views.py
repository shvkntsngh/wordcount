from django.http import HttpResponse
from django.shortcuts import render


def home(request):  # anytime someone is coming looking for a URL on a website, it sends this request obj which
    # basically says, what's the url that you're looking for, some cookies, what browser you're on,
    # all of this information that comes through is this request object.

    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    words_list = fulltext.split()
    worddict = {}
    for word in words_list:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    return render(request, 'count.html', {'worddict': worddict.items()})

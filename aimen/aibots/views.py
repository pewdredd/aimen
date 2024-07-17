from django.shortcuts import render

def index(request):
    return render(request, 'aibots/index.html', {})


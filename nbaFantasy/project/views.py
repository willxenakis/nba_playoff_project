from django.shortcuts import render
from .forms import playoffGamePredictEast
from .forms import playoffGamePredictWest

# Create your views here.

def predictions(request):
    formEast = playoffGamePredictEast()
    formWest = playoffGamePredictWest()
    return render(request, "predictions.html", {'formEast': formEast, 'formWest': formWest})

def stats(request):
    response = list(request.POST.values()) [1:]
    print(response)
    return render(request, "stats.html")

def defaultStats(request):
    return render(request, "stats.html")
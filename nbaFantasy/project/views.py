from django.shortcuts import render
from .forms import playoffGamePredictEast
from .forms import playoffGamePredictWest
from .forms import whichStat
from backend import getStats
from backend import getSpecificStat

# Create your views here.

def predictions(request):
    formEast = playoffGamePredictEast()
    formWest = playoffGamePredictWest()
    return render(request, "predictions.html", {'formEast': formEast, 'formWest': formWest})

def stats(request):
    response = list(request.POST.values()) [1:]
    stats = whichStat()
    print(response)
    return render(request, "stats.html", {'statsDataframeHTML': getStats.getStats(), 'whichStat': stats})

def specificStats(request):
    response = list(request.POST.values()) [1:][0]
    stats = whichStat(response)
    print(response)
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats(response), 'whichStat': stats})

def defaultStats(request):
    return render(request, "stats.html")
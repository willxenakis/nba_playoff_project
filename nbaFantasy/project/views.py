from django.shortcuts import render
from .forms import playoffGamePredict

# Create your views here.

def predictions(request):
    form = playoffGamePredict()
    return render(request, "predictions.html", {'form': form})

def stats(request):
    response = list(request.POST.values()) [1:]
    print(response)
    return render(request, "stats.html")

def defaultStats(request):
    return render(request, "stats.html")
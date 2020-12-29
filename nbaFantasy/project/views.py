from django.shortcuts import render
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "nbaFantasy.settings")
import django
django.setup()
from .forms import playoffGamePredictEast, playoffGamePredictWest, whichStat
from .models import TeamDict
from backend import getStats
from backend import getSpecificStat

# Create your views here.

def predictions(request):
    formEast = playoffGamePredictEast()
    formWest = playoffGamePredictWest()
    return render(request, "predictions.html", {'formEast': formEast, 'formWest': formWest})

def stats(request):
    teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BKN', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR']
    response = list(request.POST.values()) [1:]
    predicted = ';'.join(response)
    teams = ';'.join(teams)
    t = TeamDict(teamNames=teams, predictions=predicted)
    t.save()
    stats = whichStat()
    return render(request, "stats.html", {'statsDataframeHTML': getStats.getStats(), 'whichStat': stats})

def specificStats(request):
    response = list(request.POST.values()) [1:][0]
    teamPredicts = TeamDict.objects.all()[len(TeamDict.objects.all())-1]
    teams = teamPredicts.teamNames.split(';')
    predictions = [int (x) for x in teamPredicts.predictions.split(';')]
    allTeams = dict(zip(teams, predictions))
    print(allTeams)
    stats = whichStat(response)
    print(response)
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats(response, allTeams), 'whichStat': stats})

def defaultStats(request):
    return render(request, "stats.html")

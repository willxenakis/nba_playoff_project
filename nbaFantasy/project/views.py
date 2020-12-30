from django.shortcuts import render
from django.http import HttpResponse
from .forms import playoffGamePredictEast, playoffGamePredictWest, whichStat
from backend import getStats, getSpecificStat

# Create your views here.

#home view
def predictions(request):
    formEast = playoffGamePredictEast() #initialize form for eastern conference teams
    formWest = playoffGamePredictWest() #intialize form for western conference teams
    return render(request, "predictions.html", {'formEast': formEast, 'formWest': formWest})

#called when submit button clicked from predictions page
def stats(request):
    teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BKN', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR']
    response = list(request.POST.values()) [1:] #get predictions (list of integers)
    try:
        response = [int(x) for x in response]
    except ValueError:
        return HttpResponse(status=204) #if there is a non-integer in the predictions form, then don't submit
    allTeams = dict(zip(teams, response)) #create dictionary matching each team to their number of predicted games
    request.session['predictions'] = allTeams #save the dictionary in the request session
    stats = whichStat() #initialize the drop down menu 
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats('allStats', allTeams), 'whichStat': stats})

#called when submit button clicked on drop down
def specificStats(request):
    allTeams = request.session.get('predictions', None) #get the dictionary that matches each team to their predicted games from request.session
    response = list(request.POST.values()) [1:][0] #get option chosen from drop down menu
    stats = whichStat(response) #initialize drop down menu
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats(response, allTeams), 'whichStat': stats})

#called when stats link is clicked on nav bar, this causes the stats page to be multiplied by default values
def defaultStats(request):
    #default values from each team taken from starter2.py. 
    defaultPredictions = {'MIL': 14, 'TOR': 7, 'BOS': 21, 'IND': 7, 'MIA': 14, 'PHI': 7, 'BKN': 28, 'ORL': 1, 'LAL': 28, 'LAC': 14, 'DEN': 21, 'HOU': 14, 'OKC': 1, 'UTA': 7, 'DAL': 7, 'POR': 1}
    stats = whichStat()
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats('allStats', defaultPredictions), 'whichStat': stats})

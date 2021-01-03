from django.shortcuts import render
from django.http import HttpResponse
from .forms import playoffGamePredictEast, playoffGamePredictWest, whichStat
from backend import getStats, getSpecificStat

# Create your views here.

teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BKN', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR']
#home view
def predictions(request):
    formEast = playoffGamePredictEast() #initialize form for eastern conference teams
    formWest = playoffGamePredictWest() #intialize form for western conference teams
    return render(request, "predictions.html", {'formEast': formEast, 'formWest': formWest})

#called when submit button clicked from predictions page
def stats(request):
    response = list(request.POST.values()) [1:] #get predictions (list of integers)
    try:
        response = [int(x) for x in response]
    except ValueError:
        return HttpResponse(status=204) #if there is a non-integer in the predictions form, then don't submit
    allTeams = dict(zip(teams, response)) #create dictionary matching each team to their number of predicted games
    print(allTeams)
    request.session['predictions'] = allTeams #save the dictionary in the request session
    stats = whichStat() #initialize the drop down menu 
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats('allStats', allTeams), 'whichStat': stats})

def statsWithoutPredictions(request):
    stats = whichStat()
    return render(request, "statsWithoutPredictions.html", {'statsDataframeHTML': getStats.getStats(teams, "points"), 'whichStat': stats},)


#called when submit button clicked on drop down
def specificStats(request):
    allTeams = request.session.get('predictions', None) #get the dictionary that matches each team to their predicted games from request.session 
    response = list(request.POST.values()) [1:][0] #get option chosen from drop down menu
    stats = whichStat(response) #initialize drop down menu
    if allTeams is None:
        predictedGames = [28,21,14,14,7,7,7,7] * 2
        default = dict(zip(teams, predictedGames))
        return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats(response, default), 'whichStat': stats})   
    else:
        return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats(response, allTeams), 'whichStat': stats})

#called when stats link is clicked on nav bar, this causes the stats page to be multiplied by default values
def defaultStats(request):
    #default values from each team taken from starter2.py. 
    request.session.flush()
    predictedGames = [28,21,14,14,7,7,7,7] * 2
    defaultPredictions = dict(zip(teams, predictedGames))
    stats = whichStat()
    return render(request, "stats.html", {'statsDataframeHTML': getSpecificStat.getSpecificStats('allStats', defaultPredictions), 'whichStat': stats})

def specificUnStats(request):
    response = list(request.POST.values()) [1:][0]
    stats = whichStat(response)
    return render(request, "statsWithoutPredictions.html", {'statsDataframeHTML': getStats.getStats(teams, response), 'whichStat': stats},)
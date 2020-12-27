from django import forms

class playoffGamePredict(forms.Form):
    teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BKN', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR']
    team1 = forms.CharField(label=teams[0], max_length=3)
    team2 = forms.CharField(label=teams[1], max_length=3)
    team3 = forms.CharField(label=teams[2], max_length=3)
    team4 = forms.CharField(label=teams[3], max_length=3)
    team5 = forms.CharField(label=teams[4], max_length=3)
    team6 = forms.CharField(label=teams[5], max_length=3)
    team7 = forms.CharField(label=teams[6], max_length=3)
    team8 = forms.CharField(label=teams[7], max_length=3)
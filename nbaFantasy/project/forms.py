from django import forms

class playoffGamePredictEast(forms.Form):
    teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BKN', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR']
    team1 = forms.CharField(label=teams[0], max_length=3)
    team2 = forms.CharField(label=teams[1], max_length=3)
    team3 = forms.CharField(label=teams[2], max_length=3)
    team4 = forms.CharField(label=teams[3], max_length=3)
    team5 = forms.CharField(label=teams[4], max_length=3)
    team6 = forms.CharField(label=teams[5], max_length=3)
    team7 = forms.CharField(label=teams[6], max_length=3)
    team8 = forms.CharField(label=teams[7], max_length=3)

class playoffGamePredictWest(forms.Form):
    teams = ['MIL', 'TOR', 'BOS', 'IND', 'MIA', 'PHI', 'BKN', 'ORL', 'LAL', 'LAC', 'DEN', 'HOU', 'OKC', 'UTA', 'DAL', 'POR']
    team9 = forms.CharField(label=teams[8], max_length=3)
    team10 = forms.CharField(label=teams[9], max_length=3)
    team11 = forms.CharField(label=teams[10], max_length=3)
    team12 = forms.CharField(label=teams[11], max_length=3)
    team13 = forms.CharField(label=teams[12], max_length=3)
    team14 = forms.CharField(label=teams[13], max_length=3)
    team15 = forms.CharField(label=teams[14], max_length=3)
    team16 = forms.CharField(label=teams[15], max_length=3)

STATS = [
    ('allStats', 'All Stats'),
    ('points', 'Points'),
    ('freeThrowsMade', 'Free Throws'),
    ('threePointsMade', '3 Pointers'),
    ('totalRebounds', 'Rebounds'),
    ('blocks', 'Blocks'),
    ('assists', 'Assists'),
    ('fouls', 'Fouls')
]

class whichStat(forms.Form):
    def __init__(self, currentField=None):
        super().__init__()
        #extend __init__
        self.currentField = currentField
        if(currentField==None):
            self.fields['whichStat'] =forms.CharField(label='Which Stat do you Want to see the Top 50 Players for?', widget=forms.Select(choices=STATS))
        else:
            self.fields['whichStat'] =forms.CharField(label='Which Stat do you Want to see the Top 50 Players for?', widget=forms.Select(choices=STATS), initial=currentField)
        
    whichStat = forms.CharField()
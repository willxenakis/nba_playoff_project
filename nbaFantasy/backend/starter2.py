import requests
import lxml.html as lh
import pandas as pd
import numpy

url='https://www.nba.com/stats/leaders/?Season=2019-20&SeasonType=Regular%20Season&StatCategory=REB'
url2 = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"
#Create a handle, page, to handle the contents of the website
page = requests.get(url2)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)
# file = open("sample.html","w")
# file.write((lh.tostring(doc).decode('utf-8')))
# file.close()

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

print(len(tr_elements))

# All per game stats
# These columns go with the table at this link: https://www.basketball-reference.com/leagues/NBA_2020_per_game.html
mapStatToColumnIndex = {
    "name": 1,
    "position": 2,
    "age": 3,
    "team": 4,
    "gamesPlayed": 5,
    "gamesStarted": 6,
    "minutesPlayed": 7,
    "fieldGoals": 8,
    "fieldGoalsAttempted": 9,
    "fieldGoalPercentage": 10,
    "threePointsMade": 11,
    "threePointsAttempted": 12,
    "threePointPercentage": 13,
    "twoPointsMade": 14,
    "twoPointsAttempted": 15,
    "twoPointPercentage": 16,
    "effectiveFieldGoalPercentage": 17,
    "freeThrowsMade": 18,
    "freeThrowsAttempted": 19,
    "freeThrowPercentage": 20,
    "offensiveRebounds": 21,
    "defensiveRebounds": 22,
    "totalRebounds": 23,
    "assists": 24,
    "steals": 25,
    "blocks": 26,
    "turnovers": 27,
    "fouls": 28,
    "points": 29
}

dataSet = []

for T in tr_elements[1:]:
    validRow = True
    row = []
    for i, t in enumerate(T.iterchildren()):
        if(str(t.text_content())=='Rk'):
            validRow = False
            break
        elif(str(t.text_content())==''):
            row.append(0.0)
        else:
            if(i==1 or i==2 or i==4):
                row.append(str(t.text_content()))
            else:
                row.append(float(t.text_content()))
    if validRow:
        dataSet.append(row)

def getColumn(col, data):
    column = [row[col] for row in data]
    return column

d = {
    "name": getColumn(1, dataSet),
    "position": getColumn(2, dataSet),
    "age": getColumn(3, dataSet),
    "team": getColumn(4, dataSet),
    "gamesPlayed": getColumn(5, dataSet),
    "gamesStarted": getColumn(6, dataSet),
    "minutesPlayed": getColumn(7, dataSet),
    "fieldGoals": getColumn(8, dataSet),
    "fieldGoalsAttempted": getColumn(9, dataSet),
    "fieldGoalPercentage": getColumn(10, dataSet),
    "threePointsMade": getColumn(11, dataSet),
    "threePointsAttempted": getColumn(12, dataSet),
    "threePointPercentage": getColumn(13, dataSet),
    "twoPointsMade": getColumn(14, dataSet),
    "twoPointsAttempted": getColumn(15, dataSet),
    "twoPointPercentage": getColumn(16, dataSet),
    "effectiveFieldGoalPercentage": getColumn(17, dataSet),
    "freeThrowsMade": getColumn(18, dataSet),
    "freeThrowsAttempted": getColumn(19, dataSet),
    "freeThrowPercentage": getColumn(20, dataSet),
    "offensiveRebounds": getColumn(21, dataSet),
    "defensiveRebounds": getColumn(22, dataSet),
    "totalRebounds": getColumn(23, dataSet),
    "assists": getColumn(24, dataSet),
    "steals": getColumn(25, dataSet),
    "blocks": getColumn(26, dataSet),
    "turnovers": getColumn(27, dataSet),
    "fouls": getColumn(28, dataSet),
    "points": getColumn(29, dataSet)
}

df = pd.DataFrame(data=d)

# df.sort_values(by=["team", "points"], inplace = True, ascending = False)

sortedTeams = df.sort_values(by=["team"], ascending = False)

consoleIn = 'name' #input()

sortedByInputColumn = df.sort_values(by=[consoleIn], ascending = False)

print(sortedByInputColumn)

predictedGamesWestern = {
    "DAL": 7,
    "DEN": 21,
    "GSW": 0,
    "HOU": 14,
    "LAC": 14,
    "LAL": 28,
    "MEM": 0,
    "MIN": 0,
    "NOP": 7, 
    "OKC": 0, 
    "PHX": 7,
    "POR": 0,
    "SAC": 0,
    "SAS": 0,
    "UTA": 7,
}

predictedGamesEastern = {
    "ATL": 0,
    "BKN": 28,
    "BOS": 21,
    "CHA": 7,
    "CHI": 0,
    "CLE": 0,
    "DET": 0,
    "IND": 7,
    "MIA": 14,
    "MIL": 14,
    "NYK": 0,
    "ORL": 0,
    "PHI": 7,
    "TOR": 7,
    "WAS": 0
}

# df.loc[df['team']=="BOS", 'points'] = df.loc[df['team']=="BOS", 'points']*10

statList = list(df.columns)
popList = [0, 1, 2, 3, 4, 5, 9, 12, 15, 16, 19]
for i in range(len(popList)):
    popList[i] = popList[i] - i

for i in popList:
    statList.pop(i)
print(statList)


for team in predictedGamesWestern:
    for i in statList:
        df.loc[df['team']==team, i] = df.loc[df['team']==team, i]*predictedGamesWestern[team]

print(df.loc[df['team']=="NOP"])


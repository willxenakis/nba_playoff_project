import requests
import lxml.html as lh
import pandas as pd
import numpy
import re

url = "https://www.basketball-reference.com/leagues/NBA_2020_standings.html"
#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)
# file = open("sample.html","w")
# file.write((lh.tostring(doc).decode('utf-8')))
# file.close()

#Parse data that are stored between <tr>..</tr> of HTML
easternTable = doc.xpath('//table[@id="confs_standings_E"]/tbody/tr')
westernTable = doc.xpath('//table[@id="confs_standings_W"]/tbody/tr')

playoffTeams = []

teamNametoTicker = {
    "Atlanta Hawks":"ATL",
    "Brooklyn Nets":"BKN",
    "Boston Celtics":"BOS",
    "Charlotte Hornets":"CHA",
    "Chicago Bulls":"CHI",
    "Cleveland Caveliers":"CLE",
    "Detroit Pistons":"DET",
    "Indiana Pacers":"IND",
    "Miami Heat":"MIA",
    "Milwaukee Bucks": "MIL",
    "New York Knicks":"NYK",
    "Orlando Magic":"ORL",
    "Philadelphia ers":"PHI",
    "Toronto Raptors":"TOR",
    "Washington Wizards":"WAS",
    "Dallas Mavericks":"DAL",
    "Denver Nuggets":"DEN",
    "Golden State Warriors":"GSW",
    "Houston Rockets":"HOU",
    "Los Angeles Clippers":"LAC",
    "Los Angeles Lakers":"LAL",
    "Memphis Grizzlies":"MEM",
    "Minnesota Timberwolves":"MIN",
    "New Orleans Pelicans":"NOP",
    "Oklahoma City Thunder":"OKC",
    "Phoenix Suns":"PHX",
    "Portland Trail Blazers":"POR",
    "Sacramento Kings":"SAC",
    "San Antonio Spurs":"SAS",
    "Utah Jazz":"UTA"
}

for i, T in enumerate(easternTable):
    for j, t in enumerate(T.iterchildren()):
        if(i<=7 and j==0):
            playoffTeams.append(str(t.text_content()))

for i, T in enumerate(westernTable):
    for j, t in enumerate(T.iterchildren()):
        if(i<=7 and j==0):
            playoffTeams.append(str(t.text_content()))

regex = re.compile('[^a-zA-Z ]')

for i, team in enumerate(playoffTeams):
    playoffTeams[i] = teamNametoTicker[regex.sub('', team)]

# At this point, playoffTeams is an array of the top 8 team tickers in each conference,
# With the first eight being the eastern teams in order and then last eight being the 
# Western teams in order

print(playoffTeams)
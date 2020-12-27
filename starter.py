from nba_api.stats.endpoints import commonplayerinfo
import requests
import json

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)

numPlayers = 6
minPlayersPerCategory = numPlayers*4*2

# print(player_info.available_seasons.get_json())

urlPlayers = "https://www.balldontlie.io/api/v1/players/"
urlStats = "https://www.balldontlie.io/api/v1/stats"
urlSeasonAverage = "https://www.balldontlie.io/api/v1/season_averages"

test = "https://www.nba.com/stats/leaders/?Season=2020-21&SeasonType=Pre%20Season&StatCategory=REB"

params1= {
    "seasons[]": 2019,
    "player_ids[]": 237,
    "postseason": True,
    "start_date": "2020-09-30"
}

params2 = {
    "season": 2019,
    "player_ids[]": 237
}

params3  = {
    "season": 2019,
    "per_page": 100
}

r = requests.get(url = test, params=None) 
print(r.content)

# data = r.json()

# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)
import requests
import pandas as pd
from pandas.io.json import json_normalize
from pandas import DataFrame
import numpy as np
import itertools
import requests
import json
import pandas
import csv
from itertools import zip_longest

##NHL RG PULL
url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-21/4/base/nhl-skater.json?timestamp=1576929300000'
page = requests.get(url)
page_json = json.loads(page.text)['data']['results']

lines = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-21/nhl/fixtures.json?timestamp=1576929300000'
EV = requests.get(lines)
line = json.loads(EV.text)["gameLineups"]

skater = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NHL/Dec21.csv",'w'))
skater.writerow(["Name", "FD Points","Player ID","Lineup ID","Even Strength","Power Play"])

# for x in page_json:


for x, i in zip(page_json, line):
    skater.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
                     page_json[x]["fpts"]["2"],
                     page_json[x]["player"]["id"],
                     [i][0],
                     line[i]['even_strength'],
                     line[i].get("power_play", 0)])

# skater = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NHL/Dec11.csv", 'a+'))
#
# for i in line:
#       skater.writerow([[i][0],
#        line[i]['even_strength'],
#        line[i].get("power_play", 0),])
url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-21/4/base/nhl-goalie.json?timestamp=1576929300000'
page = requests.get(url)
page_json = json.loads(page.text)['data']['results']
goalie = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NHL/Dec21.csv",'a'))
for x in page_json:
    goalie.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
                page_json[x]["fpts"]["2"],
    ])


##PGA PULL
# url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-11-20/6/base/pga-golfer.json'
# page = requests.get(url)
# page_json = json.loads(page.text)['data']['results']
#
# golfer = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/PGA/Nov20.csv",'w'))
# golfer.writerow(["Name", "FD Points","pOWN","Win Prob","Top 5", "Top 10", "Top 20", "Make Cut", "RG Ranking"])
# for x in page_json:
#     golfer.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 page_json[x]["ownership"]["2"],
#                 page_json[x]["stats"]["last-two"]["Win Prob"],
#                 page_json[x]["stats"]["last-two"]["Top 5 Prob"],
#                 page_json[x]["stats"]["last-two"]["Top 10 Prob"],
#                 page_json[x]["stats"]["last-two"]["Top 20 Prob"],
#                 page_json[x]["stats"]["last-two"]["Make Cut Prob"],
#                 page_json[x]["stats"]["last-two"]["Noto Rating"],
#     ])

##NBA PULL
url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-21/3/base/nba-player.json?timestamp=1576929300000'
page = requests.get(url)
page_json = json.loads(page.text)['data']['results']

tags = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-21/nba/fixtures.json?timestamp=1576929300000'
T = requests.get(tags)
tag = json.loads(T.text)['playerTags']


baller = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NBA/Dec21.csv",'w'))
baller.writerow(["Name", "FD Points","pOWN","Minutes","Archetype","DVP Rank","Usage Rate","Player ID", "Total Minutes", "Season FPTS", "Minutes/Game","Lineup ID","Player Tag 1","Player Tag 2"])
for x in page_json:
    baller.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
                page_json[x]["fpts"]["2"],
                # page_json[x].get("ownership",0).get("2",0),
                page_json[x]["minutes"],
                page_json[x]['player']['position'],
                page_json[x]["dvp"]["2"]["rank"],
                page_json[x]["stats"]["season"]["usg"],
                page_json[x]["player_id"],
                # page_json[x]["stats"]["season"]["min"],
                # page_json[x]["stats"]["season"]["fpts"]["2"],
                # page_json[x]["stats"]["season"]["mpg"],

    ])
for i in tag:
    print([i][0],tag[i].get("tags", 0).get("2", 0))
##NFL PULL
# qb = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-08/1/base/nfl-qb.json'
# page = requests.get(qb)
# page_json = json.loads(page.text)['data']['results']
#
# quarter = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NFL/Week14.csv",'w'))
# quarter.writerow(["Name", "FD Points","pOWN"])
# for x in page_json:
#     quarter.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 page_json[x]["ownership"]["2"],
#     ])
#
# #
# wr = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-08/1/base/nfl-wr.json'
# WR = requests.get(wr)
# page_json = json.loads(WR.text)['data']['results']
# wide = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NFL/Week14.csv",'a'))
#
# for x in page_json:
#     wide.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 # page_json[x].get("ownership","None").get("2",'0'),
#     ])
# #
# te = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-08/1/base/nfl-te.json'
# TE = requests.get(te)
# page_json = json.loads(TE.text)['data']['results']
# tight = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NFL/Week14.csv",'a'))
#
# for x in page_json:
#     tight.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 # page_json[x].get("ownership","None").get("2",'0'),
#     ])
# #
# rb = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-08/1/base/nfl-rb.json'
# RB = requests.get(rb)
# page_json = json.loads(RB.text)['data']['results']
# running = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NFL/Week14.csv",'a'))
#
# for x in page_json:
#     running.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 page_json[x].get("ownership","None").get("2",'0'),
#     ])
# #
# defense = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-12-08/1/base/nfl-defense.json'
# DEFENSE = requests.get(defense)
# page_json = json.loads(DEFENSE.text)['data']['results']
# Defender = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/NFL/Week14.csv",'a'))
#
# for x in page_json:
#     Defender.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#     ])

##MLB Pull
# url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-03-30/2/base/mlb-hitter.json'
# page = requests.get(url)
# page_json = json.loads(page.text)['data']['results']
#
# batter = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/MLB/March30.csv",'w'))
# batter.writerow(["Name", "FD Points", "pOWN","Batting Order", "Confrimed"])
# for x in page_json:
#     batter.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 page_json[x].get("ownership", 0).get("2", 0),
#                 page_json[x]['batting_order']["order"],
#                 page_json[x]['batting_order']["confirmed"],
#
#     ])
#
# #
# url = 'https://d1qacz8ndd7avl.cloudfront.net/lineuphq/v1.00/2019-03-30/2/base/mlb-pitcher.json'
# page = requests.get(url)
# page_json = json.loads(page.text)['data']['results']
# pitcher = csv.writer(open("/Users/adamsardinha/Desktop/DFS Files/Projections/Rotogrinders/MLB/March30.csv",'a'))
# # pitcher.writerow(["Name", "FD Points","pOWN"])
# for x in page_json:
#     pitcher.writerow([page_json[x]['player']["first_name"] + " " + page_json[x]['player']["last_name"],
#                 page_json[x]["fpts"]["2"],
#                 page_json[x].get("ownership", 0).get("2", 0),
#     ])
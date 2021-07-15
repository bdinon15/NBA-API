import random
from nba_api.stats.static import teams
from sportsreference.nba.roster import Roster
team_name = teams.find_teams_by_full_name('')
print('Welcome to the 82-0 Challenge. Here are your 5 random teams: ')
for elem in random.sample(team_name, 5):
    res = elem['abbreviation'] + ": " + elem['full_name']
    print(res)
    var = res[:3]
    test = Roster(f'{var}', year='2021')
    if team_name == 'CHA':
        team_name = 'CHO'
    if team_name == 'PHX':
        team_name = 'PHO'
    for i in random.sample(test.players, 1):
        print("Assigned Player: " + i.name)

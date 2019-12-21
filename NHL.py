import pulp
from pulp import *
from pulp.solvers import CPLEX_PY
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter
from pydfs_lineup_optimizer.solvers.pulp_solver import PuLPSolver
class CustomPuLPSolver(PuLPSolver):
    LP_SOLVER = pulp.CPLEX_PY(msg=0)

optimizer = get_optimizer(Site.FANDUEL, Sport.HOCKEY, solver=CustomPuLPSolver)

optimizer.load_players_from_csv("NHL.csv")
for player in optimizer.players:
    if player.efficiency == 0:
        optimizer.remove_player(player)


optimizer.set_spacing_for_positions(['C', 'W', 'W'], 1)

# optimizer.set_teams_max_exposure({team: .1250 for team in optimizer.available_teams})
optimizer.set_team_stacking([4, 3], for_positions=['C', 'W', 'G'])
optimizer.set_max_repeating_players(7)
optimizer.restrict_positions_for_opposing_team(['G'], ['C', 'W', 'D','DD'])

lineups = []

# Display the lineups
for lineup in optimizer.optimize(n=150):
    lineups.append(lineup)
    print(lineup.players)

#   Export the lineups
exporter = CSVLineupExporter(lineups)
exporter.export('/Users/adamsardinha/Desktop/NHL_MME.csv')

#
optimizer.load_players_from_csv("NHL_SS.csv")
for player in optimizer.players:
    if player.efficiency == 0:
        optimizer.remove_player(player)
optimizer.set_spacing_for_positions(['C', 'W', 'W'], 1)

optimizer.set_team_stacking([4, 3], for_positions=['C', 'W', 'G'])
optimizer.set_max_repeating_players(7)
optimizer.restrict_positions_for_opposing_team(['G'], ['C', 'W', 'D','DD'])

lineups = []

# Display the lineups
for lineup in optimizer.optimize(n=150):
    lineups.append(lineup)
    print(lineup.players)

#   Export the lineups
exporter = CSVLineupExporter(lineups)
exporter.export('/Users/adamsardinha/Desktop/NHL_MME1.csv')
#
# ###5-Max
# # optimizer.load_players_from_csv("NHL.csv")
# # for player in optimizer.players:
# #     if player.efficiency == 0:
# #         optimizer.remove_player(player)
# #
# #
# # optimizer.set_spacing_for_positions(['C', 'W', 'W'], 1)
# #
# #
# # optimizer.set_team_stacking([4, 3], for_positions=['C', 'W', 'G'])
# # optimizer.restrict_positions_for_opposing_team(['G'], ['C', 'W', 'D','DD'])
# #
# # lineups = []
# #
# # # Display the lineups
# # for lineup in optimizer.optimize(n=10):
# #     lineups.append(lineup)
# #     print(lineup.players)
# #
# # #   Export the lineups
# # exporter = CSVLineupExporter(lineups)
# # exporter.export('/Users/adamsardinha/Desktop/NHL_5Max.csv')
#
#
# #Merge
with open('/Users/adamsardinha/Desktop/NHL_MME1.csv', 'r') as f1:
    next(f1)
    original = f1.read()

with open('/Users/adamsardinha/Desktop/NHL_MME.csv', 'a') as f2:
    f2.write('\n')
    f2.write(original)
#
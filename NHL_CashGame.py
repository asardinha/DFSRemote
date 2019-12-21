import pulp
from pulp import *
from pulp.solvers import CPLEX_PY
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter
from pydfs_lineup_optimizer.solvers.pulp_solver import PuLPSolver
class CustomPuLPSolver(PuLPSolver):
    LP_SOLVER = pulp.CPLEX_PY(msg=0)

optimizer = get_optimizer(Site.FANDUEL, Sport.HOCKEY, solver=CustomPuLPSolver)

#Cash Game
optimizer.load_players_from_csv("NHL_cash.csv")
for player in optimizer.players:
    if player.efficiency == 0:
        optimizer.remove_player(player)

optimizer.restrict_positions_for_opposing_team(['G'], ['C', 'W', 'D','DD'])

lineups = []

# Display the lineups
for lineup in optimizer.optimize(n=150):
    lineups.append(lineup)
    print(lineup.players)

#   Export the lineups
exporter = CSVLineupExporter(lineups)
exporter.export('/Users/adamsardinha/Desktop/NHLCash.csv')
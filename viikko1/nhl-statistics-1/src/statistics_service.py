from enum import Enum
from player_reader import PlayerReader

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def player_projection(criterion: SortBy):
    match criterion:
        case SortBy.POINTS: return lambda player: player.points
        case SortBy.GOALS: return lambda player: player.goals
        case SortBy.ASSISTS: return lambda player: player.assists

class StatisticsService:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player
        return None

    def team(self, team_name):
        return list(filter(lambda player: player.team == team_name, self._players))

    def top(self, how_many, criterion: SortBy = SortBy.POINTS):
        players = sorted(self._players, reverse=True, key=player_projection(criterion))
        result = []
        i = 0
        while i <= how_many:
            result.append(players[i])
            i += 1
        return result

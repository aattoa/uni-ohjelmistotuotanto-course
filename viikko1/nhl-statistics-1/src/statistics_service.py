from player_reader import PlayerReader

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

    def top(self, how_many):
        players = sorted(self._players, reverse=True, key=lambda player: player.points)
        result = []
        i = 0
        while i <= how_many:
            result.append(players[i])
            i += 1
        return result

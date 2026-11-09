import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self) -> list[Player]:
        return list(map(Player, requests.get(self.url).json()))

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def players_by_nationality(self, nationality: str) -> list[Player]:
        return list(filter(lambda player: player.nationality == nationality, self.reader.get_players()))

    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        return sorted(self.players_by_nationality(nationality), reverse=True, key=lambda player: player.goals + player.assists)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
            print(f"{player.name}: {player.goals} goals + {player.assists} assists")

if __name__ == "__main__":
    main()

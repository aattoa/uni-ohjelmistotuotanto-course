import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player import Player

class PlayerReader:
    def __init__(self, url: str):
        self.players = list(map(Player, requests.get(url).json()))

    def get_nationalities(self) -> list[str]:
        return list(set(map(lambda player: player.nationality, self.players)))

    def get_players(self) -> list[Player]:
        return self.players

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def players_by_nationality(self, nationality: str) -> list[Player]:
        return list(filter(lambda player: player.nationality == nationality, self.reader.get_players()))

    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        return sorted(self.players_by_nationality(nationality), reverse=True, key=lambda player: player.points())

def player_table(title: str, players: list[Player]) -> Table:
    table = Table(title=title)

    for column in ("Player", "Teams", "Goals", "Assists", "Points"):
        table.add_column(column)
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points()))

    return table

def season_name(year: int) -> str:
    return f"20{year}-{year+1}"

def main():
    seasons = list(map(season_name, range(18, 27)))

    season = Prompt.ask('Season', choices=seasons, default=season_name(24))
    reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")

    while True:
        nationality = Prompt.ask('Nationality', choices=reader.get_nationalities())
        players = PlayerStats(reader).top_scorers_by_nationality(nationality)
        Console().print(player_table(f"Season {season} players from {nationality}", players))

if __name__ == "__main__":
    main()

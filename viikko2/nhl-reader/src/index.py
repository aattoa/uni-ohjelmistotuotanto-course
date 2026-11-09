import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    print("Suomalaiset pelaajat:")

    finns = filter(lambda player: player.nationality == "FIN", map(Player, response))

    for player in sorted(finns, reverse=True, key=lambda player: player.goals + player.assists):
            print(f"{player.name}: {player.goals} goals + {player.assists} assists")

if __name__ == "__main__":
    main()

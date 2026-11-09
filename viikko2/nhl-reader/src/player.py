class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']

    def __str__(self):
        return self.name

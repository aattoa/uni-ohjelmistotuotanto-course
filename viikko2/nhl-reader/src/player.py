class Player:
    def __init__(self, fields: dict):
        self.name = fields['name']
        self.team = fields['team']
        self.goals = fields['goals']
        self.assists = fields['assists']
        self.nationality = fields['nationality']

    def points(self) -> int:
        return self.goals + self.assists

    def __str__(self):
        return self.name

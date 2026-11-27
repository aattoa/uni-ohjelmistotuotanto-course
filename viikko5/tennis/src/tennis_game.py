class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                return "Love-All"
            elif self.player1_score == 1:
                return "Fifteen-All"
            elif self.player1_score == 2:
                return "Thirty-All"
            else:
                return "Deuce"
        elif self.player1_score >= 4 or self.player2_score >= 4:
            difference = self.player1_score - self.player2_score

            if difference == 1:
                return f"Advantage {self.player1_name}"
            elif difference == -1:
                return f"Advantage {self.player2_name}"
            elif difference >= 2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"
        else:
            score = ""
            temp_score = 0

            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score += "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score += "Love"
                elif temp_score == 1:
                    score += "Fifteen"
                elif temp_score == 2:
                    score += "Thirty"
                elif temp_score == 3:
                    score += "Forty"

            return score

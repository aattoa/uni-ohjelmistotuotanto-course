def _describe_score(score: int) -> str:
    match score:
        case 0:
            return "Love"
        case 1:
            return "Fifteen"
        case 2:
            return "Thirty"
        case 3:
            return "Forty"


class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str):
        match player_name:
            case self.player1_name:
                self.player1_score += 1
            case self.player2_name:
                self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            match self.player1_score:
                case 0:
                    return "Love-All"
                case 1:
                    return "Fifteen-All"
                case 2:
                    return "Thirty-All"
                case _:
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
            score1 = _describe_score(self.player1_score)
            score2 = _describe_score(self.player2_score)
            return f"{score1}-{score2}"

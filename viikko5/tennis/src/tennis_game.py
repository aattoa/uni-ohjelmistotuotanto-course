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

def _potential_win(score: int) -> bool:
    return score >= 4

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

    def _score_equal(self) -> str:
        match self.player1_score:
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
            case _:
                return "Deuce"

    def _score_potential_win(self) -> str:
        difference = self.player1_score - self.player2_score
        if difference == 1:
            return f"Advantage {self.player1_name}"
        elif difference == -1:
            return f"Advantage {self.player2_name}"
        elif difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _score_default(self) -> str:
        score1 = _describe_score(self.player1_score)
        score2 = _describe_score(self.player2_score)
        return f"{score1}-{score2}"

    def _potential_win(self) -> bool:
        return _potential_win(self.player1_score) or _potential_win(self.player2_score)

    def get_score(self) -> str:
        if self.player1_score == self.player2_score:
            return self._score_equal()
        elif self._potential_win():
            return self._score_potential_win()
        else:
            return self._score_default()

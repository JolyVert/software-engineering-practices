class TennisGame2:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name: str, player2_name: str):
        """Inicjalizuje gracze i ich punkty"""
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name: str):
        """Dodaje punkt wskazanemu graczowi"""
        if player_name == self.player1_name:
            self.__p1_score()
        elif player_name == self.player2_name:
            self.__p2_score()

    def score(self):
        """Zwraca aktualny wynik"""
        if self.__is_draw():
            return self.__draw_score()
        if self.__is_endgame():
            return self.__endgame_score()
        return self.__regular_score()

    def __is_draw(self):
        """Sprawdza czy gracze mają równą liczbę punktów"""
        return self.p1_points == self.p2_points

    def __is_endgame(self):
        """Sprawdza czy gra weszła w fazę koncową"""
        return self.p1_points >= 4 or self.p2_points >= 4

    def __draw_score(self):
        """Zwraca wynik w przypadku remisu"""
        if self.p1_points < 3:
            return f"{self.SCORE_NAMES[self.p1_points]}-All"
        return "Deuce"

    def __endgame_score(self):
        """Zwraca wynik w przypadku Advantage i Win"""
        diff = self.p1_points - self.p2_points

        if diff == 1:
            return f"Advantage {self.player1_name}"
        if diff == -1:
            return f"Advantage {self.player2_name}"
        if diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def __regular_score(self):
        return f"{self.SCORE_NAMES[self.p1_points]}-{self.SCORE_NAMES[self.p2_points]}"

    def __p1_score(self):
        self.p1_points += 1

    def __p2_score(self):
        self.p2_points += 1


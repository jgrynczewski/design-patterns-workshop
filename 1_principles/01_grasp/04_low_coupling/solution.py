"""
GRASP Low Coupling - Game System

>>> # Test ScoreService
>>> service = ScoreService()
>>> service.save_score("player1", 100)
'Saved score 100 for player1'

>>> # Test Game with ScoreService (low coupling)
>>> game = Game(service)
>>> game.finish_game("Alice", 150)
'Game finished. Saved score 150 for Alice'
"""


class Database:
    """Konkretna implementacja bazy danych"""

    def connect(self) -> str:
        return "Connected to database"

    def save(self, player: str, score: int) -> str:
        return f"Saved score {score} for {player}"


# TODO: Zaimplementuj ScoreService
# Klasa pośrednicząca między Game a bazą danych (redukuje sprzężenie)
# Metoda save_score(player, score) zwraca: "Saved score {score} for {player}"

class ScoreService:
    def __init__(self):
        self.database = Database()

    def save_score(self, player: str, score: int) -> str:
        """Pośrednik - izoluje Game od Database"""
        self.database.connect()
        return self.database.save(player, score)


# TODO: Zaimplementuj Game
# Przyjmuje score_service: ScoreService w konstruktorze (dependency injection)
# Metoda finish_game(player, score):
#   - Wywołuje score_service.save_score(player, score)
#   - Zwraca "Game finished. {wynik z save_score}"
#
# Low Coupling: Game nie zna Database, tylko ScoreService (pośrednik)

class Game:
    def __init__(self, score_service: ScoreService):
        """Dependency Injection - redukuje sprzężenie"""
        self.score_service = score_service

    def finish_game(self, player: str, score: int) -> str:
        """Game używa tylko ScoreService, nie zna Database"""
        result = self.score_service.save_score(player, score)
        return f"Game finished. {result}"


# GRASP Low Coupling:
# Minimalizuj zależności między klasami
#
# Silne sprzężenie ❌:
# Game → Database (bezpośrednia zależność)
#
# Luźne sprzężenie ✅:
# Game → ScoreService → Database (pośrednik)
#
# Korzyść: Zmiana Database nie wpływa na Game


# Przykład użycia
if __name__ == "__main__":
    service = ScoreService()
    game = Game(service)
    print(game.finish_game("Alice", 150))

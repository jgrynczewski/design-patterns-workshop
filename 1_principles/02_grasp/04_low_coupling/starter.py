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


class ScoreService:
    """
    Serwis do zapisywania wyników

    Pośrednik między Game a bazą danych - redukuje sprzężenie
    """

    def save_score(self, player: str, score: int) -> str:
        """
        Zapisuje wynik gracza

        W rzeczywistości: łączy się z bazą, obsługuje błędy, itp.
        Tutaj: symulacja
        """
        return f"Saved score {score} for {player}"


# TODO: Zaimplementuj Game
# Hint: W konstruktorze przyjmij score_service: ScoreService
# Hint: finish_game(player, score) wywołuje score_service.save_score()
# Hint: Low Coupling - Game nie zna Database, tylko ScoreService

class Game:
    """
    Gra - LOW COUPLING dzięki ScoreService

    GRASP Low Coupling: Game nie zależy bezpośrednio od Database,
    tylko od ScoreService (pośrednik)
    """

    def __init__(self, score_service: ScoreService):
        """
        TODO: Zapisz score_service
        """
        pass

    def finish_game(self, player: str, score: int) -> str:
        """
        Kończy grę i zapisuje wynik

        TODO:
        - Wywołaj score_service.save_score()
        - Zwróć "Game finished. {result from save_score}"
        """
        pass


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

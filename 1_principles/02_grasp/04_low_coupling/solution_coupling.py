"""
GRASP Low Coupling - Game System - SOLUTION

>>> service = ScoreService()
>>> game = Game(service)
>>> game.finish_game("Alice", 150)
'Game finished. Saved score 150 for Alice'
"""


class ScoreService:
    """Pośrednik między Game a bazą danych"""

    def save_score(self, player: str, score: int) -> str:
        return f"Saved score {score} for {player}"


class Game:
    """Gra - LOW COUPLING dzięki ScoreService"""

    def __init__(self, score_service: ScoreService):
        self.score_service = score_service

    def finish_game(self, player: str, score: int) -> str:
        result = self.score_service.save_score(player, score)
        return f"Game finished. {result}"


if __name__ == "__main__":
    print("=== GRASP Low Coupling ===\n")

    print("✅ Low Coupling (ze ScoreService):")
    service = ScoreService()
    game = Game(service)
    print(game.finish_game("Alice", 150))
    print()

    print("Low Coupling: Game nie zna Database, tylko ScoreService")
    print("Zmiana Database nie wpływa na Game")
    print()

    print("❌ High Coupling (bez pośrednika):")
    print("class Game:")
    print("    def finish_game(self, player, score):")
    print("        Database().connect()  # Bezpośrednia zależność!")
    print("        Database().save(player, score)")

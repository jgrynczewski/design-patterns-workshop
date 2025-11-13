"""
Testy dla GRASP Low Coupling - Game System
"""

import pytest
from starter import ScoreService, Game


class TestLowCoupling:
    """Testy GRASP Low Coupling"""

    def test_score_service_save(self):
        service = ScoreService()
        result = service.save_score("player1", 100)

        assert "player1" in result
        assert "100" in result

    def test_game_with_score_service(self):
        """Low Coupling: Game używa ScoreService"""
        service = ScoreService()
        game = Game(service)

        result = game.finish_game("Alice", 150)

        assert "Alice" in result
        assert "150" in result
        assert "Game finished" in result

    def test_game_depends_on_service_not_database(self):
        """
        Low Coupling: Game zależy od ScoreService, nie od Database

        Game nie powinien mieć bezpośredniej referencji do Database
        """
        service = ScoreService()
        game = Game(service)

        # Game ma score_service
        assert hasattr(game, 'score_service')
        assert game.score_service is service

        # Game NIE MA bezpośredniego dostępu do Database
        assert not hasattr(game, 'database')

    def test_can_replace_score_service(self):
        """Low Coupling: Można łatwo podmienić ScoreService"""

        class MockScoreService:
            def save_score(self, player, score):
                return f"Mock saved {player}: {score}"

        mock_service = MockScoreService()
        game = Game(mock_service)

        result = game.finish_game("Bob", 200)
        assert "Mock saved" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

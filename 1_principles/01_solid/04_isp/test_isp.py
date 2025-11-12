"""
Testy dla ISP - Worker System
"""

import pytest
from starter import Workable, Eatable, Sleepable, Human, Robot


class TestISP:
    """Testy Interface Segregation Principle"""

    def test_human_work(self):
        human = Human("Alice")
        assert human.work() == "Alice is working"

    def test_human_eat(self):
        human = Human("Bob")
        assert human.eat() == "Bob is eating"

    def test_human_sleep(self):
        human = Human("Charlie")
        assert human.sleep() == "Charlie is sleeping"

    def test_human_implements_all_interfaces(self):
        human = Human("Dave")
        assert isinstance(human, Workable)
        assert isinstance(human, Eatable)
        assert isinstance(human, Sleepable)

    def test_robot_work(self):
        robot = Robot("R2D2")
        assert robot.work() == "R2D2 is working"

    def test_robot_implements_only_workable(self):
        robot = Robot("C3PO")
        assert isinstance(robot, Workable)
        assert not isinstance(robot, Eatable)
        assert not isinstance(robot, Sleepable)

    def test_robot_does_not_have_eat_method(self):
        """ISP: Robot nie musi implementować eat()"""
        robot = Robot("R2D2")
        assert not hasattr(robot, 'eat') or not callable(getattr(robot, 'eat', None))

    def test_robot_does_not_have_sleep_method(self):
        """ISP: Robot nie musi implementować sleep()"""
        robot = Robot("C3PO")
        assert not hasattr(robot, 'sleep') or not callable(getattr(robot, 'sleep', None))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [Player("Semenko", "EDM", 4, 12),
                Player("Lemieux", "PIT", 45, 54),
                Player("Kurri",   "EDM", 37, 53),
                Player("Yzerman", "DET", 42, 56),
                Player("Gretzky", "EDM", 35, 89)]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.s = StatisticsService(PlayerReaderStub())

    def test_search(self):
        self.assertIsNone(self.s.search('Qwerty'))
        self.assertIsNotNone(self.s.search('Gretzky'))

    def test_team(self):
        self.assertEqual(len(self.s.team('EDM')), 3)
        self.assertEqual(len(self.s.team('PIT')), 1)
        self.assertEqual(len(self.s.team('DET')), 1)
        self.assertEqual(len(self.s.team('AAA')), 0)

    def test_top(self):
        top = list(map(lambda player: player.name, self.s.top(0)))
        self.assertListEqual(top, ['Gretzky'])
